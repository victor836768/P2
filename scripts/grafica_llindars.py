from pathlib import Path
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

if len(sys.argv) != 2:
    sys.exit('Ús: python3 scripts/grafica_llindars.py resultats/prova.tsv')
fitxer = Path(sys.argv[1])
dades = np.loadtxt(fitxer, ndmin=2)
if dades.shape[1] != 2 or len(dades) == 0:
    sys.exit('Calen dues columnes: marge i puntuació.')
llindars = dades[:, 0]
puntuacions = dades[:, 1]
millor = np.argmax(puntuacions)

plt.figure(figsize=(9, 4))
plt.plot(llindars, puntuacions, '.-', linewidth=1)
plt.scatter(llindars[millor], puntuacions[millor], color='green', zorder=3)
etiqueta = f'{llindars[millor]:.2f} dB: {puntuacions[millor]:.3f} %'
plt.annotate(etiqueta, (llindars[millor], puntuacions[millor]), xytext=(8, -22), textcoords='offset points')
plt.xlabel('Marge sobre el soroll (dB)')
plt.ylabel('Puntuació TOTAL (%)')
plt.title('Ajust del llindar de veu')
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig(fitxer.with_suffix('.png'), dpi=160)
plt.close()
print('Millor valor provat:', etiqueta)
print('Gràfica:', fitxer.with_suffix('.png'))
