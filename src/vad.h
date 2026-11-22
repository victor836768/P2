#ifndef VAD_H
#define VAD_H
#include <stdio.h>

// Distingeixo els estats confirmats dels dos estats provisionals.
typedef enum {ST_UNDEF, ST_SILENCE, ST_VOICE, ST_INIT, ST_MAYBE_VOICE, ST_MAYBE_SILENCE} VAD_STATE;

typedef struct {
    VAD_STATE state;
    float sampling_rate;
    unsigned int frame_length;
    int initial_frames;
    float initial_max;
    float initial_sum;
    float noise;
    float margin_db;
    int count;
    float last_feature;
} VAD_DATA;

const char *state2str(VAD_STATE state);
VAD_DATA *vad_open(float sampling_rate);
unsigned int vad_frame_size(VAD_DATA *data);
VAD_STATE vad(VAD_DATA *data, float *x);
VAD_STATE vad_close(VAD_DATA *data);
void vad_show_state(const VAD_DATA *data, FILE *out);
#endif
