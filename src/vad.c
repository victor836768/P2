#include <math.h>  // Faig servir log10f i powf.
#include <stdlib.h>  // Reservo i allibero la memòria del detector.
#include "vad.h"
#include "pav_analysis.h"  // Reutilitzo el càlcul de potència de P1.

const int INIT_FRAMES = 10;  // Estimo el soroll amb els primers 100 ms.
const int MIN_VOICE = 8;  // Exigeixo 80 ms seguits per confirmar la veu.
const int MIN_SILENCE = 15;  // Exigeixo 150 ms seguits per confirmar el silenci.
const float MARGIN_DB = 6.0f;  // Demano 6 dB més que el soroll per detectar veu.
const float NOISE_ALPHA = 0.02f;  // Actualitzo lentament la referència durant el silenci.

const char *state2str(VAD_STATE state) {
    const char *names[] = {"UNDEF", "S", "V", "INIT", "MAYBE_V", "MAYBE_S"};  // Assigno un nom a cada estat.
    return names[state];  // Retorno el nom de l'estat rebut.
}

VAD_DATA *vad_open(float rate) {
    if (rate < 100) return NULL;  // Necessito almenys una mostra per bloc de 10 ms.
    VAD_DATA *data = malloc(sizeof(VAD_DATA));  // Reservo les dades del detector.
    if (data == NULL) return NULL;  // Comprovo que he pogut reservar memòria.
    data->state = ST_INIT;  // Començo estimant el soroll inicial.
    data->sampling_rate = rate;  // Guardo la freqüència del fitxer.
    data->frame_length = (unsigned int) (rate * 0.010);  // Calculo les mostres de 10 ms.
    data->initial_frames = 0;  // Encara no he llegit cap bloc inicial.
    data->initial_sum = 0.0f;  // Inicialitzo la suma de potències.
    data->noise = -100.0f;  // Preparo un valor finit per al silenci absolut.
    data->count = 0;  // Encara no tinc blocs provisionals.
    data->last_feature = -100.0f;  // Inicialitzo el valor que mostraré amb --verbose.
    return data;  // Retorno el detector preparat.
}

unsigned int vad_frame_size(VAD_DATA *data) {
    return data->frame_length;  // Retorno quantes mostres necessita cada bloc.
}

VAD_STATE vad(VAD_DATA *data, float *x) {
    float power = compute_power(x, data->frame_length);  // Calculo la potència del bloc en dB.
    if (power < -100.0f) power = -100.0f;  // Evito treballar amb menys infinit.
    data->last_feature = power;  // Conservo la potència per poder revisar-la.

    if (data->state == ST_INIT) {  // Estimo el soroll abans de prendre decisions.
        data->initial_sum += powf(10.0f, power / 10.0f);  // Sumo potències lineals, no decibels.
        data->initial_frames++;  // Compto aquest bloc inicial.
        if (data->initial_frames < INIT_FRAMES) return ST_UNDEF;  // Espero prou blocs per fer la mitjana.
        data->noise = 10.0f * log10f(data->initial_sum / data->initial_frames);  // Passo la mitjana a dB.
        data->state = ST_SILENCE;  // Considero silenci el període d'inicialització.
        return ST_SILENCE;  // Resolc també els blocs inicials que havia deixat pendents.
    }

    float threshold = data->noise + MARGIN_DB;  // Sitúo el llindar per sobre del soroll estimat.
    switch (data->state) {
    case ST_SILENCE:
        if (power > threshold) {  // Detecto un possible inici de veu.
            data->state = ST_MAYBE_VOICE;  // Espero abans de donar la veu per segura.
            data->count = 1;  // Compto el primer bloc candidat.
        } else {
            data->noise += NOISE_ALPHA * (power - data->noise);  // Adapto el soroll mentre continuo en silenci.
        }
        break;
    case ST_MAYBE_VOICE:
        if (power > threshold) {  // Comprovo si el nivell continua sent prou alt.
            data->count++;  // Afegeixo un altre bloc candidat.
            if (data->count >= MIN_VOICE) data->state = ST_VOICE;  // Confirmo la veu si dura prou.
        } else {
            data->state = ST_SILENCE;  // Descarto un pic massa curt.
            data->count = 0;  // Reinicio el recompte.
        }
        break;
    case ST_VOICE:
        if (power <= threshold) {  // Detecto una possible pausa.
            data->state = ST_MAYBE_SILENCE;  // Espero abans de tallar el segment de veu.
            data->count = 1;  // Compto el primer bloc de nivell baix.
        }
        break;
    case ST_MAYBE_SILENCE:
        if (power <= threshold) {  // Comprovo si la pausa continua.
            data->count++;  // Compto un altre bloc de nivell baix.
            if (data->count >= MIN_SILENCE) data->state = ST_SILENCE;  // Confirmo el silenci si dura prou.
        } else {
            data->state = ST_VOICE;  // Mantinc dins de la veu una pausa massa curta.
            data->count = 0;  // Reinicio el recompte.
        }
        break;
    default:
        break;
    }

    if (data->state == ST_SILENCE || data->state == ST_VOICE) return data->state;  // Retorno una decisió confirmada.
    return ST_UNDEF;  // Deixo pendents els blocs provisionals.
}

VAD_STATE vad_close(VAD_DATA *data) {
    VAD_STATE state = ST_SILENCE;  // Resolc com a silenci un inici incomplet o una veu no confirmada.
    if (data->state == ST_VOICE || data->state == ST_MAYBE_SILENCE) state = ST_VOICE;  // Mantinc la veu si la pausa final és massa curta.
    free(data);  // Allibero la memòria del detector.
    return state;  // Retorno la decisió per als darrers blocs.
}

void vad_show_state(const VAD_DATA *data, FILE *out) {
    fprintf(out, "%s\t%.3f\t%.3f\n", state2str(data->state), data->last_feature, data->noise + MARGIN_DB);  // Mostro estat, potència i llindar.
}
