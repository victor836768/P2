# P2 — Detecció d'activitat vocal

Jordi Albareda Fortuny · Grup 41 · Lloc XX

## Prova d’histèresi

Branca `jordi-albareda-canvis-classe-histeresi`, creada des de `jordi-albareda` (commit `2de00cb`).

Comparo dos llindars mantenint la inicialització, les duracions mínimes i l’actualització del soroll. He provat 14 combinacions sobre les mateixes 115 gravacions.

| Configuració | Entrada en veu | Sortida de veu | Sensibilitat V | Precisió V | TOTAL |
|---|---:|---:|---:|---:|---:|
| Base | soroll + 6 dB | soroll + 6 dB | 97,86 % | 92,18 % | **95,474 %** |
| Millor amb histèresi | soroll + 6 dB | soroll + 5 dB | **98,33 %** | 90,59 % | 95,376 % |
| Prova 6/4 | soroll + 6 dB | soroll + 4 dB | 98,60 % | 88,05 % | 94,651 % |
| Prova 6/3 | soroll + 6 dB | soroll + 3 dB | 98,88 % | 85,08 % | 93,587 % |

Conservo més veu, però també classifico més soroll com a veu. Cap combinació provada supera el TOTAL de la base; no faig la fusió. Deixo 6/5 dB en aquesta branca per poder revisar la millor prova.

[Resultats de les 14 configuracions](resultats/comparacio_histeresi.csv).

## Compilació i execució

Necessito Meson, Ninja i `libsndfile`.

```sh
meson setup bin
ninja -C bin
bin/vad -i pav_41XX1.wav -o pav_41XX1.vad
```

`meson bin` és la forma antiga de `meson setup bin`. Amb `-v` mostro temps, estat intern, potència, llindar d’entrada i llindar de sortida. Les etiquetes del fitxer de sortida són només `S` i `V`.

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

Faig servir **soroll + 6 dB** per passar de silenci a veu i **soroll + 5 dB** per passar de veu a silenci. Els llindars inicials són **−47,60 dB** i **−48,60 dB**. Durant el silenci actualitzo la referència amb `soroll = 0.98 * soroll + 0.02 * potència`.

### Duracions mínimes

- Veu: **80 ms** per descartar pics curts.
- Silenci: **150 ms** per no tallar pauses breus dins de les paraules.

Les dues pauses internes de la referència duren 490 i 920 ms.

### Creuaments per zero

El ZCR mitjà del silenci inicial és **346 Hz** i el màxim de la gravació és **4377 Hz**. Augmenta en alguns sons de poca amplitud, però no separa sempre veu i silenci. El represento per analitzar-lo; el detector decideix amb potència i duració.

## Detector

Reutilitzo `compute_power()` de P1. Processo blocs de 10 ms amb cinc estats:

1. **INIT:** estimo el soroll amb la mitjana de potències lineals dels primers 100 ms.
2. **SILENCE:** espero que la potència superi el llindar alt.
3. **MAYBE_VOICE:** confirmo la veu després de 80 ms seguits per sobre del llindar alt.
4. **VOICE:** espero que la potència baixi del llindar baix.
5. **MAYBE_SILENCE:** confirmo el silenci després de 150 ms seguits per sota del llindar baix.

Si una candidatura és massa curta, mantinc l'estat anterior. Quan confirmo un canvi, situo el límit al primer bloc provisional. Al final del fitxer resolc els blocs pendents amb l'última decisió confirmada i incloc les mostres del darrer bloc incomplet.

Només guardo les mostres d'un bloc i els comptadors de l'autòmat. No llegeixo blocs futurs ni les etiquetes de referència per detectar la veu.

### Comparació amb la referència

![Comparació entre referència i detector](img/comparacio_vad.png)

| Segment de veu | Referència (s) | Detector (s) |
|---|---|---|
| 1 | 1,410–2,850 | 1,410–2,860 |
| 2 | 3,340–4,700 | 3,400–4,720 |
| 3 | 5,620–8,150 | 5,610–8,240 |

El detector perd 60 ms a l'inici poc potent del segon fragment i n'allarga el final 20 ms. Allarga 90 ms el final del tercer, on la veu es confon amb el soroll. La resta de diferències són de 10 ms.

En aquesta gravació obtinc **98,87 % de sensibilitat de veu**, **97,59 % de precisió de veu** i **98,416 % de puntuació**. Resultat complet: [evaluacio_personal.txt](resultats/evaluacio_personal.txt).

```sh
perl scripts/vad_evaluation.pl pav_41XX1.lab
```

## Ajust i avaluació de `db.v4`

Per a la versió base sense histèresi vaig comparar **27 combinacions** canviant les constants de `src/vad.c`. Mantinc el mateix algoritme en tots els casos. No he fet servir la gravació personal per triar els paràmetres.

| Prova | Inicialització | Veu mínima | Silenci mínim | Marge | Actualització del soroll | TOTAL |
|---|---:|---:|---:|---:|---:|---:|
| Inicial | 200 ms | 50 ms | 150 ms | 8 dB | 0,02 | 95,038 % |
| Marge més baix | 200 ms | 50 ms | 150 ms | 6 dB | 0,02 | 95,174 % |
| Veu mínima més llarga | 200 ms | 80 ms | 150 ms | 6 dB | 0,02 | 95,250 % |
| **Base sense histèresi** | **100 ms** | **80 ms** | **150 ms** | **6 dB** | **0,02** | **95,474 %** |

Totes les proves: [ajust_parametres.csv](resultats/ajust_parametres.csv).

Executo:

```sh
scripts/run_vad.sh
```

El script analitza les 115 gravacions i guarda les prediccions a `resultats/db`. Copio les referències sense modificar-les i les comparo amb el script proporcionat `vad_evaluation.pl`.

| Estat | Sensibilitat (*recall*) | Precisió |
|---|---:|---:|
| Veu | **98,33 %** | **90,59 %** |
| Silenci | **84,07 %** | **96,99 %** |

**TOTAL de la branca amb histèresi: 95,376 %.** El script calcula `sqrt(F2(veu) * F0.5(silenci))`, no una F1 simple.

L'avaluador afegeix silenci al final de tres referències més curtes que l'àudio. He mantingut les etiquetes originals. [Resultat complet](resultats/evaluacio_db.txt).

Els paràmetres s'han triat sobre `db.v4`; aquesta puntuació és de desenvolupament. El detector pot fallar si la veu comença durant la inicialització o si el soroll canvia bruscament.

## Comprovacions

- Compilació sense avisos i recompilació de les dependències amb Ninja.
- Sortides amb només `S` i `V`, contínues i amb la durada real dels 115 àudios.
- Clics curts, pauses dins de la veu, decisions pendents al final i blocs incomplets.
- Àudios curts, silenci absolut, 8/16/48 kHz i errors d'entrada o sortida.

[Registre de proves](resultats/proves.txt).

[Proves específiques d’histèresi](resultats/proves_histeresi.txt): a 8, 16 i 48 kHz, un nivell entre els dos llindars manté la veu ja iniciada però no inicia un segment nou.

## Extres

No implementats: cancel·lació del silenci i paràmetres del detector configurables des de la línia d'ordres. Mantinc el lector bàsic d'arguments `docopt_c` que ja venia amb la pràctica.

## Figures

Per regenerar les figures en aquest Mac, amb l'entorn Python de P1:

```sh
../P1/.venv/bin/python scripts/grafiques.py
../P1/.venv/bin/python scripts/visualitza_wavesurfer.py --export
```

Sense `--export`, el segon script obre els panells interactius de WaveSurfer. Els scripts de figures necessiten NumPy, Matplotlib i SoundFile.

## Entrega

Branca local de proves: `jordi-albareda-canvis-classe-histeresi`. La versió base es conserva a `jordi-albareda`. El repositori remot configurat és `victor836768/P2`.

Per a l’entrega mantinc la versió base de `jordi-albareda`, que obté millor TOTAL. Aquesta branca queda com a prova. El pull request d’entrega i la pujada de l’àudio i les etiquetes a Atenea queden pendents.

## Referències

- [Enunciat de P2](p2_vad.pdf).
- Codi inicial i avaluador proporcionats al repositori de la pràctica.
- Funcions d'anàlisi i gravació reutilitzades de P1.
