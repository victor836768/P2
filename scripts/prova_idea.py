"""Provo una idea amb la base de dades i amb alguns àudios petits."""
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil
import numpy as np
import soundfile as sf

IDEA = 'dc'
carpeta = Path(__file__).resolve().parent.parent
base_dades = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else carpeta / 'db.v4'
programa = carpeta / 'bin/vad'
fitxers = sorted(base_dades.glob('*/*.wav'))
if len(fitxers) != 115:
    raise SystemExit('Cal la base db.v4 amb les 115 gravacions.')
if not programa.is_file():
    raise SystemExit('Primer cal compilar: meson setup bin; ninja -C bin')

def executar(audio, sortida, verbose=False):
    ordre = [str(programa), '-i', str(audio), '-o', str(sortida)]
    if verbose:
        ordre.append('-v')
    return subprocess.run(ordre, check=True, capture_output=True, text=True).stdout

def llegir_etiquetes(fitxer):
    return [(float(a), float(b), c) for a, b, c in
            (linia.split() for linia in fitxer.read_text().splitlines())]

comprovacions = []
with tempfile.TemporaryDirectory(prefix='p2-prova-') as temporal:
    temporal = Path(temporal)
    referencies = []
    for audio in fitxers:
        desti = temporal / audio.parent.name
        desti.mkdir(exist_ok=True)
        referencia = desti / audio.with_suffix('.lab').name
        shutil.copyfile(audio.with_suffix('.lab'), referencia)
        sortida = referencia.with_suffix('.vad')
        executar(audio, sortida)
        segments = llegir_etiquetes(sortida)
        assert segments[0][0] == 0
        assert abs(segments[-1][1] - sf.info(audio).duration) <= 0.000001
        assert all(b > a and c in ('S', 'V') for a, b, c in segments)
        assert all(segments[i][1] == segments[i + 1][0] for i in range(len(segments) - 1))
        referencies.append(str(referencia.relative_to(temporal)))
    ordre = ['perl', str(carpeta / 'scripts/vad_evaluation.pl'), *referencies]
    avaluacio = subprocess.run(ordre, cwd=temporal, check=True, capture_output=True, text=True).stdout
    comprovacions.append('115 gravacions: etiquetes S/V, sense buits i fins al final real.')

    shutil.copyfile(carpeta / 'pav_41XX1.lab', temporal / 'personal.lab')
    executar(carpeta / 'pav_41XX1.wav', temporal / 'personal.vad')
    personal = subprocess.run(['perl', str(carpeta / 'scripts/vad_evaluation.pl'), 'personal.lab'],
                              cwd=temporal, check=True, capture_output=True, text=True).stdout
    (carpeta / ('resultats/personal_' + IDEA + '.txt')).write_text(
        personal.rstrip() + '\n' + (temporal / 'personal.vad').read_text())

    for fm in (8000, 16000, 48000):
        n = fm // 100
        def provar(blocs):
            x = np.repeat(np.asarray(blocs), n)
            # Canvio el signe a cada mostra per tenir mitjana zero dins de cada bloc.
            x[1::2] *= -1
            audio = temporal / 'petit.wav'
            sf.write(audio, x, fm, subtype='PCM_16')
            text = executar(audio, temporal / 'petit.vad', True)
            return text, llegir_etiquetes(temporal / 'petit.vad')

        for quantitat in (1, 4, 20):
            _, segments = provar([0.] * quantitat)
            assert segments == [(0., quantitat / 100, 'S')]

        if IDEA == 'soroll':
            text, _ = provar([.5] + [.001] * 8 + [.001] * 20)
            soroll = float(text.splitlines()[8].split()[-1]) - 5.94
            assert -61 < soroll < -59, soroll
            # També comprovo el cas extrem: un pic seguit de silenci absolut.
            text, _ = provar([.5] + [0.] * 28)
            soroll = float(text.splitlines()[8].split()[-1]) - 5.94
            assert np.isfinite(soroll) and -101 < soroll < -99, soroll
            comprovacions.append(f'{fm} Hz: el pic inicial queda fora de la mitjana; el soroll no dona infinit.')
        elif IDEA == 'baixada':
            _, segments = provar([.001] * 20 + [.1] * 4 + [.001] + [.1] * 4 + [.001] * 30)
            veu = [(a, b) for a, b, c in segments if c == 'V']
            assert len(veu) == 1 and veu[0] == (.20, .29), veu
            _, segments = provar([.001] * 20 + [.1] * 4 + [.001] * 2 + [.1] * 4 + [.001] * 30)
            assert all(c == 'S' for _, _, c in segments)
            _, segments = provar([.001] * 20 + [.1] * 7 + [.001] * 30)
            assert all(c == 'S' for _, _, c in segments)
            comprovacions.append(f'{fm} Hz: permeto una baixada, però rebutjo dues baixades i set blocs de veu.')
        elif IDEA == 'dc':
            audio = temporal / 'constant.wav'
            sf.write(audio, np.full(fm // 2, .25), fm, subtype='PCM_16')
            text = executar(audio, temporal / 'constant.vad', True)
            assert all(float(linia.split()[2]) == -100 for linia in text.splitlines())
            assert llegir_etiquetes(temporal / 'constant.vad') == [(0., .5, 'S')]
            # Una veu amb un desplaçament constant ha de donar els mateixos límits.
            blocs = [.001] * 20 + [.1] * 30 + [.001] * 30
            _, esperat = provar(blocs)
            x = np.repeat(np.asarray(blocs), n)
            x[1::2] *= -1
            sf.write(audio, x + .125, fm, subtype='PCM_16')
            executar(audio, temporal / 'constant.vad')
            assert llegir_etiquetes(temporal / 'constant.vad') == esperat
            comprovacions.append(f'{fm} Hz: trec un valor constant i mantinc els límits amb veu desplaçada.')

sortida = carpeta / ('resultats/prova_' + IDEA + '.txt')
sortida.write_text(avaluacio.rstrip() + '\n\nComprovacions\n' + '\n'.join(comprovacions) + '\n')
print(avaluacio[avaluacio.index('**************** Summary'):].strip())
print(personal.strip())
for comprovacio in comprovacions:
    print('OK:', comprovacio)
