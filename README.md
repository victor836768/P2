# P2 — Permetre una baixada curta

Jordi Albareda Fortuny · Grup 41 · Lloc XX

Aquesta és una branca de prova: `jordi-albareda-prova-baixada`. Surt de `ac4e32a`, igual que les altres dues proves. La versió que dona millor resultat continua a `jordi-albareda`.

## Què he canviat

Permeto un sol bloc baix mentre confirmo l’inici de la veu. Continuo exigint vuit blocs alts. Si hi ha dues baixades, descarto l’intent. Per tant, espero 80 ms o 90 ms segons si hi ha una baixada.

El canvi és a `src/vad.c i src/vad.h`. Totes les idees, incloses les que ja havia fet servir, estan explicades a [IDEES.md](IDEES.md).

## Resultat

| Versió | Sensibilitat de veu | Precisió de veu | TOTAL de db.v4 | Gravació personal |
|---|---:|---:|---:|---:|
| Base actual | 98,08 % | 92,54 % | **95,829 %** | 98,335 % |
| Aquesta prova | 98,17 % | 92,17 % | 95,791 % | 99,014 % |

La prova troba una mica més de veu, però també confon més soroll amb veu. El TOTAL baixa. Per això no l’he afegit a la versió base.

He provat les 115 gravacions de `db.v4` i la gravació personal. No he tornat a ajustar els valors ni he barrejat aquesta idea amb les altres.

- [Resultat de les 115 gravacions i comprovacions](resultats/prova_baixada.txt).
- [Resultat i segments de la gravació personal](resultats/personal_baixada.txt).
- [Comparació de les tres idees](IDEES.md#resultats-de-les-proves).

Els altres fitxers de resultats i les figures ja venien de la base. No són els resultats d’aquesta prova.

## Com ho executo

Necessito Meson, Ninja i libsndfile per compilar.

```sh
meson setup bin
ninja -C bin
bin/vad -i pav_41XX1.wav -o prova.vad
```

Per repetir l’avaluació i les comprovacions petites, necessito també Python amb NumPy i SoundFile:

```sh
python3 scripts/prova_idea.py /cami/a/db.v4
```

Si tinc `db.v4` dins de P2, no cal escriure el camí. No cal passar `-l`: el marge per defecte continua sent 5,94 dB.

## Què he mantingut igual

Llegeixo blocs de 10 ms. Començo amb 90 ms per calcular el soroll. Demano vuit blocs alts per confirmar veu i 170 ms baixos per confirmar silenci. El soroll es va actualitzant amb `soroll += 0.00615 * (potència - soroll)` quan hi ha silenci.

La sortida només té `S` i `V`. Quan confirmo un canvi, el límit torna al primer bloc pendent. No miro blocs futurs ni les etiquetes de referència per decidir.

Reutilitzo la gravació personal de P1. Les marques manuals continuen a [pav_41XX1.lab](pav_41XX1.lab). Els resultats d’aquesta prova es calculen amb aquestes mateixes marques, sense modificar-les.

## Abans d’entregar

Aquesta branca és per guardar la prova. Mantinc `jordi-albareda` per a l’entrega perquè té millor TOTAL. El pull request d’entrega i la pujada de l’àudio i les marques a Atenea són passos separats.
