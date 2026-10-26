#ifndef VAD_H
#define VAD_H
#include <stdio.h>

// Distingeixo els estats confirmats dels dos estats provisionals.
typedef enum {ST_UNDEF, ST_SILENCE, ST_VOICE, ST_INIT, ST_MAYBE_VOICE, ST_MAYBE_SILENCE} VAD_STATE;

typedef struct {
    VAD_STATE state;  // Guardo l'estat actual de l'autòmat.
    float sampling_rate;  // Guardo la freqüència de mostreig.
    unsigned int frame_length;  // Guardo les mostres de cada bloc de 10 ms.
    int initial_frames;  // Compto els blocs que uso per estimar el soroll inicial.
    float initial_sum;  // Acumulo la potència lineal dels blocs inicials.
    float noise;  // Guardo la potència estimada del soroll en dB.
    float margin_db;  // Guardo el marge que he rebut per argument.
    int count;  // Compto els blocs consecutius d'un estat provisional.
    float last_feature;  // Guardo la potència actual per a --verbose.
} VAD_DATA;

const char *state2str(VAD_STATE state);  // Converteixo els estats a text.
VAD_DATA *vad_open(float sampling_rate);  // Reservo i inicialitzo el detector.
unsigned int vad_frame_size(VAD_DATA *data);  // Consulto la mida d'un bloc.
VAD_STATE vad(VAD_DATA *data, float *x);  // Analitzo un bloc nou.
VAD_STATE vad_close(VAD_DATA *data);  // Resolc els blocs pendents i allibero la memòria.
void vad_show_state(const VAD_DATA *data, FILE *out);  // Mostro dades de comprovació.
#endif
