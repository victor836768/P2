#include <math.h>
#include "pav_analysis.h"

float compute_power(const float *x, unsigned int N) {
    float suma = 0.0f;

    if (N == 0) return 0.0f;

    float mitjana = 0.0f;
    for (unsigned int i = 0; i < N; i++) mitjana += x[i];
    mitjana /= N;

    for (unsigned int i = 0; i < N; i++) {
        float mostra = x[i] - mitjana;
        suma += mostra * mostra;
    }

    return 10.0f * log10(suma / N);
}

float compute_am(const float *x, unsigned int N) {
    float suma = 0.0f;

    if (N == 0) return 0.0f;

    for (unsigned int i = 0; i < N; i++) {
        if (x[i] < 0) {
            suma += -x[i];
        } else {
            suma += x[i];
        }
    }

    return suma / N;
}

float compute_zcr(const float *x, unsigned int N, float fm) {
    unsigned int creuaments = 0;

    if (N < 2) return 0.0f;

    for (unsigned int i = 1; i < N; i++) {
        if ((x[i - 1] < 0 && x[i] >= 0) ||
            (x[i - 1] >= 0 && x[i] < 0)) {
            creuaments++;
        }
    }

    return fm * creuaments / (2.0f * (N - 1));
}
