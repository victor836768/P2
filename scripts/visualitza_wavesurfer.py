from pathlib import Path  # Localitzo els fitxers de la pràctica.
import sys  # Comprovo si he d'exportar la vista.
import subprocess  # Converteixo la vista de WaveSurfer a una imatge.
import tkinter as tk  # Faig servir els panells de WaveSurfer basats en Tcl/Tk.

carpeta = Path(__file__).resolve().parent.parent  # Localitzo el directori P2.
resultats = carpeta / 'resultats'  # Guardo el PostScript temporal de la vista.
resultats.mkdir(exist_ok=True)  # Creo la carpeta si no existeix.
app = Path('/Applications/WaveSurfer.app/Contents')  # Localitzo WaveSurfer en aquest Mac.
finestra = tk.Tk()  # Creo la finestra del visor.
finestra.title('P2 - Referència i detecció de veu')  # Identifico la pràctica.
finestra.geometry('1050x700')  # Deixo espai per veure tots els panells.
finestra.tk.eval('proc bgerror {missatge} {puts stderr $::errorInfo}')  # Mostro els errors de Tcl al terminal.
finestra.tk.call('lappend', 'auto_path', str(app / 'lib/snack2.2'))  # Localitzo el motor d'àudio.
finestra.tk.call('lappend', 'auto_path', str(app / 'Resources/Scripts/wsurf'))  # Localitzo els panells de WaveSurfer.
finestra.tk.call('package', 'require', 'wsurf')  # Carrego WaveSurfer.
finestra.tk.call('wsurf::Initialize')  # Carrego els connectors de representació i transcripció.
finestra.tk.call('wsurf', '.audio')  # Creo el visor.
finestra.tk.call('pack', '.audio', '-fill', 'both', '-expand', 1)  # Omplo la finestra amb el visor.
finestra.tk.call('.audio', 'openFile', str(carpeta / 'pav_41XX1.wav'))  # Obro la gravació personal.
finestra.tk.setvar('widget', '.audio')  # Indico quin visor ha de configurar el fitxer següent.
finestra.tk.call('source', str(carpeta / 'scripts/p2_wavesurfer.conf'))  # Creo els panells comentats.
finestra.update_idletasks()  # Ajusto les mides dels panells abans de mostrar-los.

if '--export' in sys.argv:  # Comprovo si només vull desar la vista.
    finestra.tk.setvar('::wsurf::Info(PrintSelection)', 0)  # Incloc tota la gravació.
    finestra.tk.setvar('::wsurf::Info(FirstPage)', 1)  # Començo per la primera pàgina.
    finestra.tk.setvar('::wsurf::Info(LastPage)', 1)  # Deso una única vista completa.
    finestra.tk.setvar('::wsurf::Info(PrintFile)', str(resultats / 'wavesurfer.ps'))  # Indico el fitxer de sortida.
    finestra.tk.setvar('::wsurf::Info(Prefs,tmpDir)', str(resultats))  # Guardo els temporals dins de P2.
    finestra.tk.call('.audio', 'print', 'save')  # Exporto els panells reals de WaveSurfer.
    finestra.destroy()  # Tanco el visor després d'exportar.
    subprocess.run(['gs', '-q', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-dEPSCrop', '-dAutoRotatePages=/All', '-sDEVICE=pdfwrite', '-sOutputFile=' + str(resultats / 'wavesurfer.pdf'), str(resultats / 'wavesurfer.ps')], check=True)  # Conservo l'orientació de la vista.
    subprocess.run(['gs', '-q', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-sDEVICE=png16m', '-r160', '-sOutputFile=' + str(carpeta / 'img/wavesurfer.png'), str(resultats / 'wavesurfer.pdf')], check=True)  # Creo la imatge que inclouré al README.
else:  # Mantinc una vista interactiva si no he demanat una exportació.
    finestra.mainloop()  # Espero fins que tanqui la finestra.
