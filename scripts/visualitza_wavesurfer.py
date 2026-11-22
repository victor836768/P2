from pathlib import Path
import sys
import subprocess
import tkinter as tk

carpeta = Path(__file__).resolve().parent.parent
resultats = carpeta / 'resultats'
resultats.mkdir(exist_ok=True)
app = Path('/Applications/WaveSurfer.app/Contents')
finestra = tk.Tk()
finestra.title('P2 - Referència i detecció de veu')
finestra.geometry('1050x700')
finestra.tk.eval('proc bgerror {missatge} {puts stderr $::errorInfo}')
finestra.tk.call('lappend', 'auto_path', str(app / 'lib/snack2.2'))
finestra.tk.call('lappend', 'auto_path', str(app / 'Resources/Scripts/wsurf'))
finestra.tk.call('package', 'require', 'wsurf')
finestra.tk.call('wsurf::Initialize')
finestra.tk.call('wsurf', '.audio')
finestra.tk.call('pack', '.audio', '-fill', 'both', '-expand', 1)
finestra.tk.call('.audio', 'openFile', str(carpeta / 'pav_41XX1.wav'))
finestra.tk.setvar('widget', '.audio')
finestra.tk.call('source', str(carpeta / 'scripts/p2_wavesurfer.conf'))
finestra.update_idletasks()

if '--export' in sys.argv:
    finestra.tk.setvar('::wsurf::Info(PrintSelection)', 0)
    finestra.tk.setvar('::wsurf::Info(FirstPage)', 1)
    finestra.tk.setvar('::wsurf::Info(LastPage)', 1)
    finestra.tk.setvar('::wsurf::Info(PrintFile)', str(resultats / 'wavesurfer.ps'))
    finestra.tk.setvar('::wsurf::Info(Prefs,tmpDir)', str(resultats))
    finestra.tk.call('.audio', 'print', 'save')
    finestra.destroy()
    subprocess.run(['gs', '-q', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-dEPSCrop', '-dAutoRotatePages=/All', '-sDEVICE=pdfwrite', '-sOutputFile=' + str(resultats / 'wavesurfer.pdf'), str(resultats / 'wavesurfer.ps')], check=True)
    subprocess.run(['gs', '-q', '-dSAFER', '-dBATCH', '-dNOPAUSE', '-sDEVICE=png16m', '-r160', '-sOutputFile=' + str(carpeta / 'img/wavesurfer.png'), str(resultats / 'wavesurfer.pdf')], check=True)
else:
    finestra.mainloop()
