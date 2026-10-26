# P2 — Detecció d'activitat vocal

Jordi Albareda Fortuny · Grup 41 · Lloc XX

## Script de proves de classe

Branca `jordi-albareda-canvis-classe-bash-script`, creada a partir de `jordi-albareda`. Faig servir el detector base amb un sol llindar.

```sh
ninja -C bin
./cardem-li
```

`cardem-li` prova els marges 7, 8 i 9 dB amb un bucle Bash. Crida `scripts/run_vad.sh`, filtra el `TOTAL` i desa el resum a [resultats/cardem-li.txt](resultats/cardem-li.txt).

| Marge | TOTAL |
|---:|---:|
| 7 dB | 95,472 % |
| 8 dB | 95,340 % |
| 9 dB | 94,433 % |

El valor per defecte continua sent 6 dB: 95,474 %. Per canviar les proves, edito la llista `7 8 9` de `cardem-li`.

Per provar un sol marge sobre tota la base de dades:

```sh
scripts/run_vad.sh 8 | grep TOTAL
```

Per passar-lo directament al programa:

```sh
bin/vad -i pav_41XX1.wav -o resultats/prova_8.vad -l 8
```

`-l` i `--llindar` indiquen el **marge sobre el soroll**, no un nivell absolut. Puc passar decimals, com `-l 6.5`. No he de recompilar entre proves.

Si modifico la definició de les opcions, regenero la capçalera amb l'eina que inclou la pràctica:

```sh
python3 docopt_c/docopt_c.py src/vad.docopt -o src/vad_docopt.h
ninja -C bin
```

## Compilació i execució

Necessito Meson, Ninja i `libsndfile`.

```sh
meson setup bin
ninja -C bin
bin/vad -i pav_41XX1.wav -o pav_41XX1.vad
```

`meson bin` és la forma antiga de `meson setup bin`. Amb `-v` mostro temps, estat intern, potència i llindar. Les etiquetes del fitxer de sortida són només `S` i `V`.

## Etiquetatge de veu i silenci

Reutilitzo la gravació de P1: 9,536 s, mono, PCM de 16 bits i 16 kHz. El nom és `pav_41XX1.wav`: grup 41, lloc XX i gravació 1.

Fixo els límits per inspecció visual de la forma d'ona i la potència, abans de comparar-los amb el detector. Són aproximats; no marco les pauses curtes dins d'una frase.

| Inici (s) | Final (s) | Etiqueta |
|---:|---:|:---:|
| 0,000 | 1,410 | S |
| 1,410 | 2,850 | V |
| 2,850 | 3,340 | S |
| 3,340 | 4,700 | V |
| 4,700 | 5,620 | S |
| 5,620 | 8,150 | V |
| 8,150 | 9,536 | S |

Cada fila de [pav_41XX1.lab](pav_41XX1.lab) conté inici, final i etiqueta.

![WaveSurfer: senyal, potència, ZCR, referència i detector](img/wavesurfer.png)

De dalt a baix: forma d'ona, potència, ZCR, referència visual en negre i detecció automàtica en blau.

### Llindar de potència

El silenci inicial complet té una potència mitjana de **−52,40 dB**. Els primers 100 ms, que faig servir per inicialitzar el detector, donen **−53,60 dB**.

Trio un marge de **6 dB** sobre el soroll: el llindar inicial és aproximadament **−47,60 dB**. Durant el silenci actualitzo la referència amb `soroll = 0.98 * soroll + 0.02 * potència`.

### Duracions mínimes

- Veu: **80 ms** per descartar pics curts.
- Silenci: **150 ms** per no tallar pauses breus dins de les paraules.

Les dues pauses internes de la referència duren 490 i 920 ms.

### Creuaments per zero

El ZCR mitjà del silenci inicial és **346 Hz** i el màxim de la gravació és **4377 Hz**. Augmenta en alguns sons de poca amplitud, però no separa sempre veu i silenci. El represento per analitzar-lo; el detector decideix amb potència i duració.

## Detector

Reutilitzo `compute_power()` de P1. Processo blocs de 10 ms amb cinc estats:

1. **INIT:** estimo el soroll amb la mitjana de potències lineals dels primers 100 ms.
2. **SILENCE:** espero que la potència superi el llindar.
3. **MAYBE_VOICE:** confirmo la veu després de 80 ms seguits per sobre del llindar.
4. **VOICE:** espero una baixada de potència.
5. **MAYBE_SILENCE:** confirmo el silenci després de 150 ms seguits per sota del llindar.

Si una candidatura és massa curta, mantinc l'estat anterior. Quan confirmo un canvi, situo el límit al primer bloc provisional. Al final del fitxer resolc els blocs pendents amb l'última decisió confirmada i incloc les mostres del darrer bloc incomplet.

Només guardo les mostres d'un bloc i els comptadors de l'autòmat. No llegeixo blocs futurs ni les etiquetes de referència per detectar la veu.

### Comparació amb la referència

![Comparació entre referència i detector](img/comparacio_vad.png)

| Segment de veu | Referència (s) | Detector (s) |
|---|---|---|
| 1 | 1,410–2,850 | 1,410–2,860 |
| 2 | 3,340–4,700 | 3,400–4,690 |
| 3 | 5,620–8,150 | 5,610–8,240 |

El detector perd 60 ms a l'inici poc potent del segon fragment. Allarga 90 ms el final del tercer, on la veu es confon amb el soroll. La resta de diferències són de 10 ms.

En aquesta gravació obtinc **98,69 % de sensibilitat de veu**, **97,95 % de precisió de veu** i **98,335 % de puntuació**. Resultat complet: [evaluacio_personal.txt](resultats/evaluacio_personal.txt).

```sh
perl scripts/vad_evaluation.pl pav_41XX1.lab
```

## Ajust i avaluació de `db.v4`

He comparat **27 combinacions** canviant les constants de `src/vad.c`. Mantinc el mateix algoritme en tots els casos. No he fet servir la gravació personal per triar els paràmetres.

| Prova | Inicialització | Veu mínima | Silenci mínim | Marge | Actualització del soroll | TOTAL |
|---|---:|---:|---:|---:|---:|---:|
| Inicial | 200 ms | 50 ms | 150 ms | 8 dB | 0,02 | 95,038 % |
| Marge més baix | 200 ms | 50 ms | 150 ms | 6 dB | 0,02 | 95,174 % |
| Veu mínima més llarga | 200 ms | 80 ms | 150 ms | 6 dB | 0,02 | 95,250 % |
| **Final** | **100 ms** | **80 ms** | **150 ms** | **6 dB** | **0,02** | **95,474 %** |

Totes les proves: [ajust_parametres.csv](resultats/ajust_parametres.csv).

Executo:

```sh
scripts/run_vad.sh
```

El script analitza les 115 gravacions i guarda cada prova a `resultats/db/llindar_N`. Copio les referències sense modificar-les i les comparo amb el script proporcionat `vad_evaluation.pl`. El resum complet queda a `resultats/evaluacio_llindar_N.txt`.

| Estat | Sensibilitat (*recall*) | Precisió |
|---|---:|---:|
| Veu | **97,86 %** | **92,18 %** |
| Silenci | **87,05 %** | **96,30 %** |

**TOTAL: 95,474 %.** El script calcula `sqrt(F2(veu) * F0.5(silenci))`, no una F1 simple.

L'avaluador afegeix silenci al final de tres referències més curtes que l'àudio. He mantingut les etiquetes originals. [Resultat complet amb 6 dB](resultats/evaluacio_llindar_6.txt).

Els paràmetres s'han triat sobre `db.v4`; aquesta puntuació és de desenvolupament. El detector pot fallar si la veu comença durant la inicialització o si el soroll canvia bruscament.

## Comprovacions

- Compilació sense avisos i recompilació de les dependències amb Ninja.
- Sortides amb només `S` i `V`, contínues i amb la durada real dels 115 àudios.
- Clics curts, pauses dins de la veu, decisions pendents al final i blocs incomplets.
- Àudios curts, silenci absolut, 8/16/48 kHz i errors d'entrada o sortida.

[Registre de proves](resultats/proves.txt).

[Comprovacions de `-l`, `run_vad.sh` i `cardem-li`](resultats/proves_bash.txt).

## Extres

En aquesta branca afegeixo el marge configurable amb `-l` mitjançant el `docopt_c` del codi base. Les duracions continuen definides al codi. La cancel·lació del silenci no està implementada.

## Figures

Per regenerar les figures en aquest Mac, amb l'entorn Python de P1:

```sh
../P1/.venv/bin/python scripts/grafiques.py
../P1/.venv/bin/python scripts/visualitza_wavesurfer.py --export
```

Sense `--export`, el segon script obre els panells interactius de WaveSurfer. Els scripts de figures necessiten NumPy, Matplotlib i SoundFile.

## Entrega

Branca local: `jordi-albareda-canvis-classe-bash-script`. La branca base `jordi-albareda` es conserva separada. El repositori remot configurat és `victor836768/P2`.

Per entregar, cal pujar la branca, fer el pull request indicat al repositori de la pràctica i pujar `pav_41XX1.wav` i `pav_41XX1.lab` a Atenea.

## Referències

- [Enunciat de P2](p2_vad.pdf).
- Codi inicial i avaluador proporcionats al repositori de la pràctica.
- Funcions d'anàlisi i gravació reutilitzades de P1.
