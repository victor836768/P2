from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf

carpeta = Path(__file__).resolve().parent.parent
audio = carpeta / 'pav_41XX1.wav'
img = carpeta / 'img'
resultats = carpeta / 'resultats'
img.mkdir(exist_ok=True)
resultats.mkdir(exist_ok=True)
x, fm = sf.read(audio)
N = int(fm * 0.010)
blocs = len(x) // N
potencia = np.zeros(blocs)
zcr = np.zeros(blocs)
for i in range(blocs):
    tram = x[i * N:(i + 1) * N]
    mitjana = np.mean(tram * tram)
    potencia[i] = 10 * np.log10(max(mitjana, 1e-10))
    canvis = np.count_nonzero((tram[1:] < 0) != (tram[:-1] < 0))
    zcr[i] = fm * canvis / (2 * (N - 1))
temps = (np.arange(blocs) + 0.5) * N / fm
np.savetxt(audio.with_suffix('.features'), np.column_stack((potencia, zcr)), fmt='%.6f')

manual = []
with audio.with_suffix('.lab').open() as fitxer:
    for linia in fitxer:
        inici, final, etiqueta = linia.split()
        manual.append((float(inici), float(final), etiqueta))
automatic = []
with audio.with_suffix('.vad').open() as fitxer:
    for linia in fitxer:
        inici, final, etiqueta = linia.split()
        automatic.append((float(inici), float(final), etiqueta))

def etiquetes(ax, segments, nom):
    for inici, final, etiqueta in segments:
        color = '#b9d9ed' if etiqueta == 'V' else '#eeeeee'
        ax.axvspan(inici, final, color=color)
        ax.text((inici + final) / 2, 0.5, etiqueta, ha='center', va='center')
        ax.axvline(final, color='gray', linewidth=0.5)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    ax.set_ylabel(nom)
    ax.set_xlim(0, len(x) / fm)

fig, axes = plt.subplots(4, 1, figsize=(11, 7), sharex=True, gridspec_kw={'height_ratios': [2, 2, 2, 1]})
axes[0].plot(np.arange(len(x)) / fm, x, linewidth=0.5)
axes[0].set_ylabel('Amplitud')
axes[0].set_title('Gravació i etiquetatge de referència')
axes[1].plot(temps, potencia, linewidth=0.8)
axes[1].set_ylabel('Potència (dB)')
axes[2].plot(temps, zcr, linewidth=0.8, color='tab:green')
axes[2].set_ylabel('ZCR (Hz)')
etiquetes(axes[3], manual, 'Referència')
axes[3].set_xlabel('Temps (s)')
plt.tight_layout()
plt.savefig(img / 'etiquetatge.png', dpi=160)
plt.close()

fig, axes = plt.subplots(3, 1, figsize=(11, 5), sharex=True, gridspec_kw={'height_ratios': [3, 1, 1]})
axes[0].plot(np.arange(len(x)) / fm, x, linewidth=0.5)
axes[0].set_ylabel('Amplitud')
axes[0].set_title('Referència visual i detecció automàtica')
etiquetes(axes[1], manual, 'Referència')
etiquetes(axes[2], automatic, 'Detector')
axes[2].set_xlabel('Temps (s)')
plt.tight_layout()
plt.savefig(img / 'comparacio_vad.png', dpi=160)
plt.close()

primer_silenci = int(manual[0][1] * fm)
mesures = {
    'durada': len(x) / fm,
    'soroll_inicial_db': float(10 * np.log10(np.mean(x[:primer_silenci] ** 2))),
    'referencia_90ms_db': float(10 * np.log10(np.mean(x[:int(0.09 * fm)] ** 2))),
    'zcr_silenci_mitja': float(np.mean(zcr[temps < manual[0][1]])),
    'zcr_maxim': float(np.max(zcr))
}
(resultats / 'gravacio_personal.json').write_text(json.dumps(mesures, indent=2) + '\n')
print(mesures)
