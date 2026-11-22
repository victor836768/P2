# P2 — Prova de totes les idees juntes

Jordi Albareda Fortuny · Grup 41 · Lloc 05

En aquesta branca he provat les idees del detector juntes i per separat. És `jordi-albareda-combinacions`; la base d’entrega continua a `jordi-albareda`.

Les idees i els resultats estan explicats amb paraules senzilles a [IDEES.md](IDEES.md). També hi ha la [matriu completa](IDEES.md#matriu-de-totes-les-combinacions).

Les proves posteriors són a [`jordi-albareda-proves-pendents`](https://github.com/victor836768/P2/tree/jordi-albareda-proves-pendents): arriben a **96,910 % amb blocs de 20 ms** i **96,838 % amb blocs de 10 ms**. El resum és a [IDEES.md](IDEES.md#proves-que-quedaven-pendents).


## Què he afegit

A més de les vuit idees que ja havia provat, ara hi ha tres opcions més:

| Opció | Què prova | D’on surt |
|---|---|---|
| `--rescat-zcr` | Acceptar veu una mica més fluixa si el ZCR és alt i hi ha prou potència | [Pegueroles–Riera, PR #4](https://github.com/albino-pav/P2/pull/4) |
| `--confirma-alt` | Exigir que la veu arribi a un llindar alt abans d’un temps màxim | [Arbelo–Moreno, PR #7](https://github.com/albino-pav/P2/pull/7) i [Galvan–Fernandez, PR #3](https://github.com/albino-pav/P2/pull/3) |
| `--limita-soroll` | Actualitzar el soroll només amb blocs prou propers al soroll estimat | [Pegueroles–Riera](https://github.com/falgarspegueroles/P2/blob/Pegueroles-Riera/src/vad.c) |

Les he afegit al detector que ja tenia. Encara que un bloc arribi al llindar alt, espero la duració mínima de veu. Les tres opcions estan apagades per defecte.

Les altres vuit idees continuen a les proves: esperes de veu i silenci, seguiment del soroll, histèresi, retorn al primer bloc pendent, treure el pic inicial, permetre una baixada i treure la mitjana del bloc.

## Com ho busco

Ara hi ha **2.048 combinacions**. Per a cadascuna faig tres inicis amb valors normals. Si millora el TOTAL, hi moc el centre. Si no millora, redueixo el pas. També ajusto els valors de les tres idees noves.

Els valors que havia provat abans els guardo per comparar. La cerca comença amb tres grups de valors normals.

## Resultat

| Versió | TOTAL |
|---|---:|
| Base d’entrega | 95,829 % |
| Millor de l’estudi amb vuit idees | 95,891 % |
| Millor de l’estudi amb onze idees | **96,186 %** |

La millor configuració combina **rescat ZCR i confirmació amb llindar alt** amb les esperes de veu i silenci, el seguiment del soroll, una baixada permesa, treure la mitjana i tornar al primer bloc pendent. La histèresi, treure el pic inicial i el límit d’actualització del soroll queden apagats.

Els valors trobats són 100 ms inicials, 80 ms de veu mínima, 160 ms de silenci mínim, marge de **5,875 dB** i alfa d’aproximadament **0,005233**. El ZCR es compara amb **2.500 Hz**, amb una rebaixa de potència de **2,125 dB**. La confirmació exigeix arribar **7 dB** per sobre del llindar d’entrada abans de **250 ms**.

Guanya uns **0,295 punts** respecte de l’estudi amb vuit idees i **0,357 punts** respecte de la base d’entrega. Les puntuacions són de desenvolupament, amb `db.v4`.

El límit d’actualització del soroll també s’ha provat: la millor configuració que l’activa arriba a **96,182 %**. És molt propera a la guanyadora. No vol dir que aquesta idea sigui dolenta; només que aquí el millor resultat trobat la deixa apagada.

Si executo el programa sense les opcions noves, continua fent servir la base. A sota hi ha la comanda per repetir el 96,186 %.

## Compilar i executar

Necessito Meson, Ninja i libsndfile.

```sh
meson setup bin
ninja -C bin
bin/vad -i pav_41XX1.wav -o prova.vad
```

Per activar les tres idees noves a mà:

```sh
bin/vad -i pav_41XX1.wav -o prova.vad --rescat-zcr --confirma-alt --limita-soroll
bin/vad --help
```

Per repetir la millor configuració trobada:

```sh
bin/vad -i pav_41XX1.wav -o prova.vad \
    --inici=10 --veu=8 --silenci=16 -l5.875 \
    --alfa=0.0052329911 --histeresi=0 --permet-baixada --treu-dc \
    --rescat-zcr --confirma-alt --zcr=2500 --rebaixa-zcr=2.125 \
    --pujada=7 --espera=25 --marge-soroll=2
```

Els nombres d’aquesta última ordre són el resultat de la cerca.

## Repetir les proves

Necessito també un compilador C, Python, NumPy i SoundFile. La base de dades no es puja al repositori.

```sh
python3 scripts/prova_combinacions.py /cami/a/db.v4 --verifica
python3 scripts/comprova_metodes.py
python3 scripts/comprova_metodes_nous.py
```

Si `db.v4` és dins de P2, no cal passar el camí. La primera ordre prova les combinacions i comprova les millors i els controls amb el programa normal i el Perl. Les altres dues comproven casos petits a 8, 16 i 48 kHz.

Per regenerar la matriu a partir dels CSV, sense repetir les proves:

```sh
python3 scripts/actualitza_matriu.py
```

## Fitxers de resultats

- [Combinacions amb valors fixos](resultats/combinacions/combinacions_amb_valors_fixos.csv).
- [Parelles on només canvia una idea](resultats/combinacions/canvis_per_parelles.csv).
- [Estudi anterior amb vuit idees](resultats/combinacions/combinacions_vuit_metodes.csv).
- [Millor ajust de cada combinació nova](resultats/combinacions/combinacions_ajustades.csv).
- [Recorregut de la cerca](resultats/combinacions/recorregut_cerca.csv).
- [Verificació amb el programa normal i el Perl](resultats/combinacions/verificacio.csv).
- [Avaluació completa del millor resultat](resultats/combinacions/avaluacio_millor.txt).
- [Comprovacions dels mètodes nous](resultats/combinacions/comprovacions_nous.txt).

La gravació personal no es fa servir per triar la millor combinació. Les puntuacions són sobre les 115 gravacions de `db.v4`, que ja havia fet servir per ajustar la base. Caldrien àudios nous per veure com funciona fora d’aquest conjunt.

Els altres resultats i figures es conserven com a historial de les proves anteriors.
