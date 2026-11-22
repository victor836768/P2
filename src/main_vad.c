#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <math.h>
#include <sndfile.h>
#include "vad.h"
#include "vad_docopt.h"

int main(int argc, char *argv[]) {
    DocoptArgs args = docopt(argc, argv, 1, "2.0");
    char *number_end;
    errno = 0;
    float margin = strtof(args.llindar, &number_end);
    if (number_end == args.llindar || *number_end != '\0' || errno != 0 || !isfinite(margin) || margin <= 0) {
        fprintf(stderr, "El llindar ha de ser un marge positiu en dB.\n");
        return 1;
    }
    if (args.input_wav == NULL || args.output_vad == NULL) {
        fprintf(stderr, "%s\n", args.usage_pattern);
        return 1;
    }
    if (strcmp(args.input_wav, args.output_vad) == 0) {
        fprintf(stderr, "L'entrada i la sortida han de tenir noms diferents.\n");
        return 1;
    }

    SF_INFO info = {0};
    SNDFILE *audio = sf_open(args.input_wav, SFM_READ, &info);
    if (audio == NULL) {
        fprintf(stderr, "No puc obrir l'àudio: %s\n", sf_strerror(NULL));
        return 1;
    }
    if (info.channels != 1 || info.frames == 0) {
        fprintf(stderr, "Cal un àudio mono que no sigui buit.\n");
        sf_close(audio);
        return 1;
    }

    VAD_DATA *data = vad_open(info.samplerate);
    if (data == NULL) {
        fprintf(stderr, "No puc inicialitzar el detector.\n");
        sf_close(audio);
        return 1;
    }
    unsigned int frame_size = vad_frame_size(data);
    data->margin_db = margin;
    float *buffer = malloc(frame_size * sizeof(float));
    if (buffer == NULL) {
        fprintf(stderr, "No hi ha prou memòria.\n");
        vad_close(data);
        sf_close(audio);
        return 1;
    }
    FILE *labels = fopen(args.output_vad, "w");
    if (labels == NULL) {
        perror("No puc obrir el fitxer d'etiquetes");
        free(buffer);
        vad_close(data);
        sf_close(audio);
        return 1;
    }

    double frame_time = (double) frame_size / info.samplerate;
    unsigned int t = 0, last_t = 0, pending = 0;
    VAD_STATE last_state = ST_UNDEF;
    sf_count_t n_read;

    while ((n_read = sf_read_float(audio, buffer, frame_size)) == frame_size) {
        VAD_STATE state = vad(data, buffer);
        if (args.verbose) {
            printf("%.5f\t", t * frame_time);
            vad_show_state(data, stdout);
        }
        // Guardo els blocs dubtosos fins que el detector es decideix.
        if (state == ST_UNDEF) {
            pending++;
        } else {
            unsigned int start = t - pending;
            if (last_state == ST_UNDEF) {
                last_state = state;
            } else if (state != last_state) {
                if (start > last_t) {
                    fprintf(labels, "%.6f\t%.6f\t%s\n", last_t * frame_time, start * frame_time, state2str(last_state));
                }
                last_t = start;
                last_state = state;
            }
            pending = 0;
        }
        t++;
    }

    int result = 0;
    if (sf_error(audio) != SF_ERR_NO_ERROR) result = 1;
    VAD_STATE final_state = vad_close(data);
    if (last_state == ST_UNDEF) last_state = final_state;
    // Incloc també les mostres que no omplen un bloc sencer.
    double end = ((double) t * frame_size + n_read) / info.samplerate;
    if (end > last_t * frame_time) {
        fprintf(labels, "%.6f\t%.6f\t%s\n", last_t * frame_time, end, state2str(last_state));
    }
    if (ferror(labels)) result = 1;
    if (fclose(labels) != 0) result = 1;
    free(buffer);
    sf_close(audio);
    if (result != 0) fprintf(stderr, "Error en llegir o escriure les dades.\n");
    return result;
}
