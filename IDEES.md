# Idees que he fet servir a P2

## Què vull comparar

No miro només les tres últimes idees. També miro les coses que ja tenia el detector: l’espera de veu i silenci, el seguiment del soroll, els dos llindars i el retorn al primer bloc pendent. També provo diferents valors dels paràmetres.

He guardat el programa de proves a [jordi-albareda-combinacions](https://github.com/victor836768/P2/tree/jordi-albareda-combinacions). La versió d’entrega continua a `jordi-albareda`.

## Com decideixo si hi ha veu

Llegeixo blocs de 10 ms i en calculo la potència. Comparo cada bloc amb el soroll més un marge. Si passa del llindar, pot ser veu.

El soroll del començament és la mitjana de potències lineals dels primers blocs. He provat diversos temps: no és el mateix fer servir 50, 90 o 200 ms. El marge tampoc és sempre el mateix: he provat, entre altres, 6, 6,63 i 5,94 dB.

Aquest càlcul de potència i els blocs de 10 ms són el punt de partida de totes les proves. No els he canviat per un altre tipus de detector.

## Les vuit idees que activo o desactivo

### 1. Esperar abans de confirmar la veu

Demano uns quants blocs alts seguits abans de dir que hi ha veu. Així puc descartar un cop curt. A la base són vuit blocs, és a dir, 80 ms.

Per veure si ajuda, també ho provo sense espera: un sol bloc alt ja confirma veu. Quan l’espera està activada, provo diferents duracions.

### 2. Esperar abans de confirmar el silenci

No tallo la veu per una baixada molt curta. Espero uns quants blocs baixos. A la base són 17 blocs, és a dir, 170 ms.

També ho provo sense aquesta espera i amb altres duracions. Això pot ajudar una idea i perjudicar-ne una altra.

### 3. Anar canviant el soroll

Quan hi ha silenci, faig `soroll += alfa * (potència - soroll)`. Si alfa és petit, el soroll canvia a poc a poc.

Provo diferents valors d’alfa i també alfa zero. Amb zero, el soroll es queda al valor inicial durant tot el fitxer.

### 4. Fer servir dos llindars

Puc demanar més potència per començar la veu que per mantenir-la. Això és la histèresi que ja havia provat.

Quan l’activo, provo diferències de 0,5, 1, 1,5 i 2 dB. Quan la desactivo, faig servir el mateix llindar per començar i acabar.

### 5. Tornar al primer bloc pendent

Quan confirmo veu després de vuit blocs, puc posar l’inici al primer d’aquests blocs. Això ja ho feia la base. Faig el mateix amb el silenci.

També provo de posar el canvi just quan el confirmo. Així veig què passa si no torno enrere. No miro blocs futurs: espero la confirmació abans d’escriure el límit.

### 6. Deixar fora el pic inicial

Si hi ha un cop al començament, el soroll inicial pot sortir massa alt. Provo de deixar fora el bloc més fort i fer la mitjana dels altres.

Guardo el màxim per separat i sumo els altres blocs. No cal guardar tot el començament de l’àudio.

### 7. Permetre una baixada mentre confirmo veu

Permeto un bloc baix entremig dels blocs alts. Continuo demanant el mateix nombre de blocs alts. El bloc baix no compta per arribar a aquest nombre.

Si confirmo la veu, la baixada queda dins del mateix segment. Si hi ha una segona baixada abans de confirmar-la, descarto l’intent.

Si he desactivat l’espera de veu, aquesta idea no canvia res: ja confirmo la veu amb el primer bloc alt.

### 8. Treure el valor mitjà del bloc

Calculo la mitjana de les mostres i la resto abans de calcular la potència. Així un desplaçament constant respecte de zero no compta com a energia del so.

L’àudio original no canvia. Només canvia el càlcul de la potència.

## Quines combinacions he provat

Hi ha vuit idees amb dues opcions cadascuna: activada o desactivada. Per això hi ha **256 combinacions d’interruptors**. Algunes fan el mateix, com permetre una baixada quan no hi ha espera de veu.

Primer provo les 256 combinacions amb quatre grups de valors:

| Grup | Blocs inicials | Blocs de veu | Blocs de silenci | Marge | Alfa |
|---|---:|---:|---:|---:|---:|
| Primer ajust | 20 | 5 | 15 | 8 dB | 0,02 |
| Base de 6 dB | 10 | 8 | 15 | 6 dB | 0,02 |
| Ajust de 6,63 dB | 10 | 8 | 15 | 6,63 dB | 0,02 |
| Base actual | 9 | 8 | 17 | 5,94 dB | 0,00615 |

Si una espera està desactivada, faig servir un bloc. Si el seguiment del soroll està desactivat, faig servir alfa zero. Si hi ha histèresi, en aquesta primera passada separo els llindars 1 dB.

Això dona **1.024 files amb valors fixos**. Després faig un ajust curt per a cadascuna de les 256 combinacions. Començo pel millor dels quatre grups i canvio un valor cada vegada, durant dues passades. Provo el temps inicial, les dues esperes, el marge, alfa i la diferència entre llindars. Al final miro alguns valors propers.

Aplico la mateixa llista de valors a totes les combinacions, excepte quan una idea està desactivada. També conservo la configuració de partida, perquè una passada d’ajust no la faci perdre.

En total he calculat **11.201 configuracions diferents**. No he provat tots els nombres possibles ni totes les barreges possibles dels paràmetres.

## Com miro si dues idees es porten bé

Comparo files on només canvia un interruptor. Les altres idees i els valors són iguals. Per exemple, miro què passa en activar la histèresi amb cada grup de les altres set idees.

Hi ha 128 parelles per idea i per grup de valors. Les he guardat a `canvis_per_parelles.csv`. Els zeros i uns d’`abans` i `despres` segueixen l’ordre de les vuit columnes de mètodes del CSV.

Amb els valors de la base actual, això és el que passa en activar cada idea en diferents combinacions:

| Idea | Pitjor canvi en el TOTAL | Millor canvi en el TOTAL |
|---|---:|---:|
| Espera de veu | −10,283 punts | +1,234 punts |
| Espera de silenci | −1,953 punts | +7,995 punts |
| Seguiment del soroll | −0,791 punts | +0,413 punts |
| Dos llindars | −0,836 punts | +1,050 punts |
| Treure el pic inicial | −0,847 punts | +0,697 punts |
| Permetre una baixada | −0,082 punts | +0,340 punts |
| Treure la mitjana | −0,336 punts | +0,344 punts |
| Tornar al primer bloc pendent | 0,000 punts | +9,913 punts |

No són els guanys respecte de la base actual. Cada parella pot tenir altres idees activades o desactivades. La taula serveix per veure que el mateix canvi pot anar bé en un cas i malament en un altre.

## Quin resultat ha sortit

| Prova | TOTAL |
|---|---:|
| Base actual | 95,829 % |
| Totes les idees activades amb els valors de la base actual | 95,223 % |
| Millor combinació trobada amb l’ajust curt | **95,831 %** |

La millor combinació trobada manté l’espera de veu, l’espera de silenci, el seguiment del soroll i el retorn al primer bloc pendent. També treu la mitjana. No treu el pic inicial, no permet la baixada i no fa servir histèresi.

Fa servir nou blocs inicials, vuit blocs de veu, 17 de silenci, marge de **6,63 dB** i alfa de **0,00615**.

És un exemple del que volia comprovar: treure la mitjana amb marge de 5,94 dB donava 95,771 %, pitjor que la base. Amb marge de 6,63 dB arriba a 95,831 %.

La diferència respecte del 95,829 % és d’uns **0,002 punts**. És molt petita. De moment mantinc la base d’entrega i deixo aquesta combinació a la branca de proves.

## Com ho he comprovat

La prova ràpida calcula les potències amb el codi C i fa servir el mateix autòmat del detector. Les referències només serveixen per calcular la puntuació.

Després he comprovat **26 configuracions** amb el programa normal, llegint els WAVE originals, i amb el `vad_evaluation.pl` original. Hi ha la base, cada idea sola, cada idea canviada respecte de la base i les deu millors combinacions ajustades. Les puntuacions coincideixen amb les de la prova ràpida dins de l’arrodoniment del Perl.

També he comprovat àudios petits a 8, 16 i 48 kHz: silenci, cops, baixades, desplaçament respecte de zero, els dos llindars, les esperes i els límits dels segments. He provat totes les idees juntes i opcions mal escrites.

Tot això és sobre `db.v4`, que ja havia fet servir per ajustar la base. No és una prova amb dades noves ni una garantia del millor resultat possible.

## On són les proves

A la branca [jordi-albareda-combinacions](https://github.com/victor836768/P2/tree/jordi-albareda-combinacions):

- `scripts/prova_combinacions.py`: combinacions i ajust de valors.
- `scripts/comprova_metodes.py`: àudios petits amb casos coneguts.
- `resultats/combinacions/combinacions_amb_valors_fixos.csv`: les 1.024 files inicials.
- `resultats/combinacions/canvis_per_parelles.csv`: què passa quan només activo una idea.
- `resultats/combinacions/combinacions_ajustades.csv`: el millor trobat per a cadascun dels 256 grups.
- `resultats/combinacions/verificacio.csv`: comparació amb el programa normal i el Perl.
- `resultats/combinacions/avaluacio_millor.txt`: resultat complet de la millor configuració trobada.

Les tres proves inicials per separat també es conserven a `jordi-albareda-prova-soroll`, `jordi-albareda-prova-baixada` i `jordi-albareda-prova-dc`.

## Altres coses del treball

He dibuixat el ZCR i he calculat l’amplitud mitjana, però no hi ha cap regla del detector que els faci servir. Per això no els poso com si fossin mètodes ja provats. Afegir-los com a decisió seria una prova nova.

Les opcions de `docopt_c`, `cardem-li`, els rànquings i les gràfiques ajuden a fer i explicar les proves. No són canvis en la manera de detectar veu. Tampoc he implementat la cancel·lació del silenci.

La lectura correcta del fitxer, la durada final, les etiquetes S/V i el tractament dels errors es mantenen a totes les proves. No els desactivo per intentar pujar la puntuació.
