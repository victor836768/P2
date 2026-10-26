from pathlib import Path  # Localitzo el fitxer de puntuacions.
import sys  # Llegeixo el nom del fitxer indicat.
import matplotlib  # Preparo una gràfica que es pugui desar sense finestra.
matplotlib.use('Agg')  # Deso la figura directament en PNG.
import matplotlib.pyplot as plt  # Dibuixo la puntuació de cada marge.
import numpy as np  # Llegeixo les dues columnes del fitxer TSV.

if len(sys.argv) != 2:  # Comprovo que he rebut el nom d'un fitxer.
    sys.exit('Ús: python3 scripts/grafica_llindars.py resultats/prova.tsv')  # Mostro com executar l'script.
fitxer = Path(sys.argv[1])  # Selecciono el resum generat per cardem-li.
dades = np.loadtxt(fitxer, ndmin=2)  # Llegeixo marge i puntuació TOTAL.
if dades.shape[1] != 2 or len(dades) == 0:  # Comprovo les dues columnes esperades.
    sys.exit('Calen dues columnes: marge i puntuació.')  # Explico el format necessari.
llindars = dades[:, 0]  # Selecciono els marges provats.
puntuacions = dades[:, 1]  # Selecciono les puntuacions corresponents.
millor = np.argmax(puntuacions)  # Localitzo la puntuació més alta.

plt.figure(figsize=(9, 4))  # Preparo una figura llegible.
plt.plot(llindars, puntuacions, '.-', linewidth=1)  # Connecto els resultats en ordre de marge.
plt.scatter(llindars[millor], puntuacions[millor], color='green', zorder=3)  # Destaco el millor valor provat.
etiqueta = f'{llindars[millor]:.2f} dB: {puntuacions[millor]:.3f} %'  # Preparo el text del resultat.
plt.annotate(etiqueta, (llindars[millor], puntuacions[millor]), xytext=(8, -22), textcoords='offset points')  # Escric el millor valor al costat del punt.
plt.xlabel('Marge sobre el soroll (dB)')  # Identifico el paràmetre que he variat.
plt.ylabel('Puntuació TOTAL (%)')  # Identifico el resultat de l'avaluador.
plt.title('Ajust del llindar de veu')  # Identifico la comparació.
plt.grid(alpha=0.25)  # Facilito la lectura de la corba.
plt.tight_layout()  # Ajusto els marges del dibuix.
plt.savefig(fitxer.with_suffix('.png'), dpi=160)  # Deso la figura al costat de les dades.
plt.close()  # Tanco la figura.
print('Millor valor provat:', etiqueta)  # Mostro també el resultat al terminal.
print('Gràfica:', fitxer.with_suffix('.png'))  # Indico on he desat la figura.
