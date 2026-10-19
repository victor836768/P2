#include <math.h>
#include "pav_analysis.h"

float compute_power(const float *x, unsigned int N) {
    float suma = 0.0f;  // Guardo la suma dels quadrats de les mostres.

    if (N == 0) return 0.0f;  // Evito dividir per zero si el bloc és buit.

    for (unsigned int i = 0; i < N; i++) {  // Recorro totes les mostres del bloc.
        suma += x[i] * x[i];  // Sumo el quadrat de cada mostra.
    }

    return 10.0f * log10(suma / N);  // Faig la mitjana i la passo a decibels.
}

float compute_am(const float *x, unsigned int N) {
    float suma = 0.0f;  // Guardo la suma dels valors absoluts.

    if (N == 0) return 0.0f;  // Evito dividir per zero si el bloc és buit.

    for (unsigned int i = 0; i < N; i++) {  // Recorro totes les mostres del bloc.
        if (x[i] < 0) {  // Si la mostra és negativa, li canvio el signe.
            suma += -x[i];  // Així sumo el seu valor absolut.
        } else {  // Si és zero o positiva, ja té el signe correcte.
            suma += x[i];  // La sumo tal com és.
        }
    }

    return suma / N;  // Divideixo la suma pel nombre de mostres.
}

float compute_zcr(const float *x, unsigned int N, float fm) {
    unsigned int creuaments = 0;  // Compto els canvis de signe.

    if (N < 2) return 0.0f;  // Necessito dues mostres per detectar un canvi.

    for (unsigned int i = 1; i < N; i++) {  // Comparo cada mostra amb l'anterior.
        if ((x[i - 1] < 0 && x[i] >= 0) ||
            (x[i - 1] >= 0 && x[i] < 0)) {  // Tracto el zero com a signe positiu.
            creuaments++;  // Afegeixo un creuament si el signe ha canviat.
        }
    }

    return fm * creuaments / (2.0f * (N - 1));  // Normalitzo segons la fórmula de l'enunciat.
}
