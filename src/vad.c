#include <math.h>
#include <stdlib.h>
#include "vad.h"
#include "pav_analysis.h"

// Treballo amb blocs de 10 ms. Els marges són en dB.
const int INIT_FRAMES = 9;
const int MIN_VOICE = 8;
const int MIN_SILENCE = 17;
const float MARGIN_DB = 5.94f;
const float NOISE_ALPHA = 0.00615f;

const char *state2str(VAD_STATE state) {
    const char *names[] = {"UNDEF", "S", "V", "INIT", "MAYBE_V", "MAYBE_S"};
    return names[state];
}

VAD_DATA *vad_open(float rate) {
    if (rate < 100) return NULL;
    VAD_DATA *data = malloc(sizeof(VAD_DATA));
    if (data == NULL) return NULL;
    data->state = ST_INIT;
    data->sampling_rate = rate;
    data->frame_length = (unsigned int) (rate * 0.010);
    data->initial_frames = 0;
    data->initial_sum = 0.0f;
    data->noise = -100.0f;
    data->margin_db = MARGIN_DB;
    data->count = 0;
    data->last_feature = -100.0f;
    return data;
}

unsigned int vad_frame_size(VAD_DATA *data) {
    return data->frame_length;
}

VAD_STATE vad(VAD_DATA *data, float *x) {
    float power = compute_power(x, data->frame_length);
    if (power < -100.0f) power = -100.0f;
    data->last_feature = power;

    // Faig la mitjana en potència lineal i després passo a dB.
    if (data->state == ST_INIT) {
        data->initial_sum += powf(10.0f, power / 10.0f);
        data->initial_frames++;
        if (data->initial_frames < INIT_FRAMES) return ST_UNDEF;
        data->noise = 10.0f * log10f(data->initial_sum / data->initial_frames);
        data->state = ST_SILENCE;
        return ST_SILENCE;
    }

    float threshold = data->noise + data->margin_db;
    switch (data->state) {
    case ST_SILENCE:
        if (power > threshold) {
            data->state = ST_MAYBE_VOICE;
            data->count = 1;
        } else {
            data->noise += NOISE_ALPHA * (power - data->noise);
        }
        break;
    // Els estats MAYBE esperen abans de confirmar el canvi.
    case ST_MAYBE_VOICE:
        if (power > threshold) {
            data->count++;
            if (data->count >= MIN_VOICE) data->state = ST_VOICE;
        } else {
            data->state = ST_SILENCE;
            data->count = 0;
        }
        break;
    case ST_VOICE:
        if (power <= threshold) {
            data->state = ST_MAYBE_SILENCE;
            data->count = 1;
        }
        break;
    case ST_MAYBE_SILENCE:
        if (power <= threshold) {
            data->count++;
            if (data->count >= MIN_SILENCE) data->state = ST_SILENCE;
        } else {
            data->state = ST_VOICE;
            data->count = 0;
        }
        break;
    default:
        break;
    }

    if (data->state == ST_SILENCE || data->state == ST_VOICE) return data->state;
    return ST_UNDEF;
}

VAD_STATE vad_close(VAD_DATA *data) {
    VAD_STATE state = ST_SILENCE;
    if (data->state == ST_VOICE || data->state == ST_MAYBE_SILENCE) state = ST_VOICE;
    free(data);
    return state;
}

void vad_show_state(const VAD_DATA *data, FILE *out) {
    fprintf(out, "%s\t%.3f\t%.3f\n", state2str(data->state), data->last_feature, data->noise + data->margin_db);
}
