from pathlib import Path  # Localitzo els fitxers de la pràctica.
import json  # Deso les mesures que faré servir al README.
import matplotlib  # Preparo les figures sense obrir finestres.
matplotlib.use('Agg')  # Guardo les gràfiques directament en fitxers.
import matplotlib.pyplot as plt  # Dibuixo el senyal i les etiquetes.
import numpy as np  # Llegeixo i calculo els valors de cada bloc.
import soundfile as sf  # Llegeixo la gravació personal.

carpeta = Path(__file__).resolve().parent.parent  # Localitzo P2 encara que executi l'script des d'un altre lloc.
audio = carpeta / 'pav_41XX1.wav'  # Selecciono la gravació reutilitzada de P1.
img = carpeta / 'img'  # Guardo les figures que inclouré al README.
resultats = carpeta / 'resultats'  # Guardo les mesures de l'anàlisi.
img.mkdir(exist_ok=True)  # Creo la carpeta d'imatges si no existeix.
resultats.mkdir(exist_ok=True)  # Creo la carpeta de resultats si no existeix.
x, fm = sf.read(audio)  # Llegeixo el senyal normalitzat i la freqüència real.
N = int(fm * 0.010)  # Calculo les mostres d'un bloc de 10 ms.
blocs = len(x) // N  # Compto els blocs complets.
potencia = np.zeros(blocs)  # Reservo un valor de potència per bloc.
zcr = np.zeros(blocs)  # Reservo un valor de creuaments per bloc.
for i in range(blocs):  # Recorro els blocs en ordre.
    tram = x[i * N:(i + 1) * N]  # Selecciono les mostres del bloc.
    mitjana = np.mean(tram * tram)  # Calculo la potència lineal mitjana.
    potencia[i] = 10 * np.log10(max(mitjana, 1e-10))  # Passo a dB i limito el silenci absolut a -100 dB.
    canvis = np.count_nonzero((tram[1:] < 0) != (tram[:-1] < 0))  # Compto els canvis de signe.
    zcr[i] = fm * canvis / (2 * (N - 1))  # Aplico la normalització de P1.
temps = (np.arange(blocs) + 0.5) * N / fm  # Sitúo cada valor al centre del bloc.
np.savetxt(audio.with_suffix('.features'), np.column_stack((potencia, zcr)), fmt='%.6f')  # Preparo les columnes que llegirà WaveSurfer.

manual = []  # Preparo la llista dels segments de referència.
with audio.with_suffix('.lab').open() as fitxer:  # Llegeixo les marques fixades per inspecció visual.
    for linia in fitxer:  # Recorro les etiquetes del fitxer.
        inici, final, etiqueta = linia.split()  # Separo els temps i l'etiqueta.
        manual.append((float(inici), float(final), etiqueta))  # Guardo el segment de referència.
automatic = []  # Preparo la llista dels segments del detector.
with audio.with_suffix('.vad').open() as fitxer:  # Llegeixo la detecció automàtica.
    for linia in fitxer:  # Recorro la sortida del programa.
        inici, final, etiqueta = linia.split()  # Separo els tres camps.
        automatic.append((float(inici), float(final), etiqueta))  # Guardo el segment detectat.

def etiquetes(ax, segments, nom):  # Dibuixo una fila amb els segments S i V.
    for inici, final, etiqueta in segments:  # Recorro cada interval.
        color = '#b9d9ed' if etiqueta == 'V' else '#eeeeee'  # Distingeixo la veu del silenci.
        ax.axvspan(inici, final, color=color)  # Pinto l'interval.
        ax.text((inici + final) / 2, 0.5, etiqueta, ha='center', va='center')  # Escric S o V al centre.
        ax.axvline(final, color='gray', linewidth=0.5)  # Marco el final del segment.
    ax.set_ylim(0, 1)  # Mantinc una alçada constant.
    ax.set_yticks([])  # Amago els valors verticals que no representen cap magnitud.
    ax.set_ylabel(nom)  # Identifico el tipus d'etiquetatge.
    ax.set_xlim(0, len(x) / fm)  # Mostro tota la gravació.

fig, axes = plt.subplots(4, 1, figsize=(11, 7), sharex=True, gridspec_kw={'height_ratios': [2, 2, 2, 1]})  # Preparo el senyal i els paràmetres.
axes[0].plot(np.arange(len(x)) / fm, x, linewidth=0.5)  # Dibuixo la forma d'ona.
axes[0].set_ylabel('Amplitud')  # Indico les unitats normalitzades.
axes[0].set_title('Gravació i etiquetatge de referència')  # Identifico la figura.
axes[1].plot(temps, potencia, linewidth=0.8)  # Dibuixo la potència.
axes[1].set_ylabel('Potència (dB)')  # Indico les unitats.
axes[2].plot(temps, zcr, linewidth=0.8, color='tab:green')  # Dibuixo els creuaments per zero.
axes[2].set_ylabel('ZCR (Hz)')  # Indico la normalització usada.
etiquetes(axes[3], manual, 'Referència')  # Afegeixo els segments manuals.
axes[3].set_xlabel('Temps (s)')  # Identifico l'eix temporal.
plt.tight_layout()  # Ajusto els marges.
plt.savefig(img / 'etiquetatge.png', dpi=160)  # Deso la figura del primer exercici.
plt.close()  # Tanco la figura abans de crear la següent.

fig, axes = plt.subplots(3, 1, figsize=(11, 5), sharex=True, gridspec_kw={'height_ratios': [3, 1, 1]})  # Preparo la comparació de segments.
axes[0].plot(np.arange(len(x)) / fm, x, linewidth=0.5)  # Dibuixo la mateixa gravació.
axes[0].set_ylabel('Amplitud')  # Identifico el senyal.
axes[0].set_title('Referència visual i detecció automàtica')  # Identifico la comparació.
etiquetes(axes[1], manual, 'Referència')  # Dibuixo les etiquetes de referència.
etiquetes(axes[2], automatic, 'Detector')  # Dibuixo les etiquetes del programa.
axes[2].set_xlabel('Temps (s)')  # Identifico l'eix temporal.
plt.tight_layout()  # Ajusto l'espai entre panells.
plt.savefig(img / 'comparacio_vad.png', dpi=160)  # Deso la comparació per al README.
plt.close()  # Tanco la figura.

primer_silenci = int(manual[0][1] * fm)  # Localitzo les mostres del silenci inicial de referència.
mesures = {  # Recullo les mesures de la gravació personal.
    'durada': len(x) / fm,  # Deso la durada real.
    'soroll_inicial_db': float(10 * np.log10(np.mean(x[:primer_silenci] ** 2))),  # Mesuro el silenci inicial complet.
    'referencia_100ms_db': float(10 * np.log10(np.mean(x[:int(0.1 * fm)] ** 2))),  # Mesuro el període d'inicialització del detector.
    'zcr_silenci_mitja': float(np.mean(zcr[temps < manual[0][1]])),  # Resumeixo els creuaments al silenci inicial.
    'zcr_maxim': float(np.max(zcr))  # Deso el màxim observat.
}
(resultats / 'gravacio_personal.json').write_text(json.dumps(mesures, indent=2) + '\n')  # Deso els valors per poder comprovar el README.
print(mesures)  # Mostro les mesures calculades.
