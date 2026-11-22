# Idees que he fet servir a P2

Aquí apunto les idees que he fet servir, d’on surten i què ha passat quan les he provat. Algunes són part de la pràctica i altres són proves que he anat afegint.

El codi de les combinacions és a [jordi-albareda-combinacions](https://github.com/victor836768/P2/tree/jordi-albareda-combinacions). La versió d’entrega continua a `jordi-albareda`.

## D’on surt cada idea

### El que ja proposa la pràctica

Al [README original de la pràctica](https://github.com/victor836768/P2/blob/main/README.md) es demana mirar la potència, posar un llindar respecte del silenci inicial i triar duracions mínimes de veu i silenci. També es demana mirar el ZCR i comentar què se’n pot treure.

L’enunciat també proposa ampliacions, com les opcions amb `docopt_c` i la cancel·lació del silenci. No són el mateix que la part bàsica. He fet servir les opcions, però no he fet la cancel·lació del silenci.

Ajustar els valors i mirar el TOTAL també forma part de la pràctica. Els nombres que he acabat fent servir surten de les proves; no són valors fixats per l’enunciat.

### Les proves que he anat afegint

He provat de treure el pic inicial, permetre una baixada curta i restar la mitjana del bloc. Són proves addicionals, no coses que el README demani fer.

També he fet el programa que prova les combinacions i va ajustant els valors. És la manera que he fet servir per comparar-les i buscar una configuració que vagi millor.

Hi ha tres casos que deixo amb l’origen per confirmar: el seguiment del soroll, la histèresi i tornar al primer bloc pendent. No surten demanats explícitament al README original. Els marco com a decisions del programa; falta confirmar si s’havien proposat a classe. Així no els atribueixo al profe ni els poso com a idees pròpies sense saber-ho.

| Idea | D’on surt | Què n’he fet |
|---|---|---|
| Potència i llindar respecte del silenci inicial | Part bàsica de l’enunciat | És la base del detector |
| Duracions mínimes de veu i silenci | Part bàsica de l’enunciat | Les faig servir i en provo els valors |
| Mirar el ZCR | Part bàsica de l’enunciat | El dibuixo; fer-lo servir per al rescat és una prova a part |
| Ajustar valors i avaluar el TOTAL | Enunciat | Ho comprovo amb `db.v4` i l’avaluador de la pràctica |
| Opcions amb `docopt_c` | Ampliació de l’enunciat | Fet |
| Cancel·lació del silenci | Ampliació de l’enunciat | No fet |
| Anar actualitzant el soroll | Decisió del programa; origen de classe per confirmar | Ho provo activat i desactivat |
| Histèresi | Decisió del programa; origen de classe per confirmar | Ho provo amb un llindar o amb dos |
| Tornar al primer bloc pendent | Decisió del programa; origen de classe per confirmar | Ho comparo amb posar el límit quan es confirma |
| Treure el pic inicial | Prova addicional | Provada sola i en combinacions |
| Permetre una baixada curta | Prova addicional | Provada sola i en combinacions |
| Treure la mitjana del bloc | Prova addicional | Provada sola i en combinacions |
| Rescat amb ZCR | Inspirat en Pegueroles–Riera, PR #4 | El provo com a decisió, a més de dibuixar-lo |
| Confirmació amb llindar alt i temps màxim | Inspirat en Arbelo–Moreno i Galvan–Fernandez, PR #7 i #3 | Ho provo mantenint la duració mínima de veu |
| Limitar l’actualització del soroll | Inspirat en Pegueroles–Riera, PR #4 | Només actualitzo amb blocs prou propers al soroll |
| Script de combinacions i cerca dels valors | Forma addicional de fer les proves | Fet; guardo els resultats i el recorregut |

D’on surt una idea i si funciona bé són dues coses diferents. A les proves barrejo les que ja venien de la pràctica amb les que he afegit, per veure quines ajuden juntes.

## Com decideixo si hi ha veu

Llegeixo blocs de 10 ms i en calculo la potència. Comparo cada bloc amb el soroll més un marge. Si passa del llindar, pot ser veu.

El soroll del començament és la mitjana de potències lineals dels primers blocs. He provat diversos temps: no és el mateix fer servir 50, 90 o 200 ms. El marge tampoc és sempre el mateix: he provat, entre altres, 6, 6,63 i 5,94 dB.

Aquest càlcul de potència i els blocs de 10 ms són el punt de partida de totes les proves. No els he canviat per un altre tipus de detector.

## Les onze idees que activo o desactivo

### 1. Esperar abans de confirmar la veu

Això ve de les duracions mínimes que demana l’enunciat.

Demano uns quants blocs alts seguits abans de dir que hi ha veu. Així puc descartar un cop curt. A la base són vuit blocs, és a dir, 80 ms.

Per veure si ajuda, també ho provo sense espera: un sol bloc alt ja confirma veu. Quan l’espera està activada, provo diferents duracions.

### 2. Esperar abans de confirmar el silenci

Això també ve de les duracions mínimes de l’enunciat.

No tallo la veu per una baixada molt curta. Espero uns quants blocs baixos. A la base són 17 blocs, és a dir, 170 ms.

També ho provo sense aquesta espera i amb altres duracions. Això pot ajudar una idea i perjudicar-ne una altra.

### 3. Anar canviant el soroll

És una decisió del programa. Deixo per confirmar si es va proposar a classe.

Quan hi ha silenci, faig `soroll += alfa * (potència - soroll)`. Si alfa és petit, el soroll canvia a poc a poc.

Provo diferents valors d’alfa i també alfa zero. Amb zero, el soroll es queda al valor inicial durant tot el fitxer.

### 4. Fer servir dos llindars

És una prova amb histèresi. Deixo per confirmar si es va proposar a classe.

Puc demanar més potència per començar la veu que per mantenir-la. Això és la histèresi que ja havia provat.

Quan l’activo, la cerca també va canviant la diferència entre els dos llindars. Quan la desactivo, faig servir el mateix llindar per començar i acabar.

### 5. Tornar al primer bloc pendent

És una manera de posar els límits dels segments. L’origen de classe queda per confirmar.

Quan confirmo veu després de vuit blocs, puc posar l’inici al primer d’aquests blocs. Això ja ho feia la base. Faig el mateix amb el silenci.

També provo de posar el canvi just quan el confirmo. Així veig què passa si no torno enrere. No miro blocs futurs: espero la confirmació abans d’escriure el límit.

### 6. Deixar fora el pic inicial

Aquesta és una de les proves addicionals.

Si hi ha un cop al començament, el soroll inicial pot sortir massa alt. Provo de deixar fora el bloc més fort i fer la mitjana dels altres.

Guardo el màxim per separat i sumo els altres blocs. No cal guardar tot el començament de l’àudio.

### 7. Permetre una baixada mentre confirmo veu

Aquesta també és una prova addicional.

Permeto un bloc baix entremig dels blocs alts. Continuo demanant el mateix nombre de blocs alts. El bloc baix no compta per arribar a aquest nombre.

Si confirmo la veu, la baixada queda dins del mateix segment. Si hi ha una segona baixada abans de confirmar-la, descarto l’intent.

Si he desactivat l’espera de veu, aquesta idea no canvia res: ja confirmo la veu amb el primer bloc alt.

### 8. Treure el valor mitjà del bloc

És la tercera prova addicional.

Calculo la mitjana de les mostres i la resto abans de calcular la potència. Així un desplaçament constant respecte de zero no compta com a energia del so.

L’àudio original no canvia. Només canvia el càlcul de la potència.

### 9. Rescatar veu fluixa amb el ZCR

M’he fixat en [Pegueroles–Riera, PR #4](https://github.com/albino-pav/P2/pull/4). Si el bloc no arriba al llindar normal, encara el puc acceptar si té ZCR alt i supera un llindar una mica més baix.

No accepto qualsevol bloc amb ZCR alt: també demano prou potència. Faig servir aquesta ajuda tant per començar la veu com per mantenir-la. La cerca prova el llindar de ZCR i quants dB puc rebaixar la potència. El ZCR es calcula sobre les mostres originals; l’opció DC continua canviant només la potència.

### 10. Arribar a un llindar alt abans que passi massa temps

La idea surt d’[Arbelo–Moreno, PR #7](https://github.com/albino-pav/P2/pull/7) i [Galvan–Fernandez, PR #3](https://github.com/albino-pav/P2/pull/3). Un primer llindar deixa començar un intent de veu. Per confirmar-lo, algun bloc ha d’arribar a un segon llindar més alt.

A la meva prova continuo exigint el nombre mínim de blocs de veu. Un únic pic fort no se salta aquesta espera. Si no he confirmat la veu dins del temps màxim, descarto l’intent.

La cerca ajusta la pujada fins al segon llindar i el temps màxim. Això és diferent de la histèresi que ja tenia: la histèresi canvia el llindar per acabar la veu; aquesta idea canvia com la confirmo al començament.

### 11. Actualitzar el soroll només amb blocs propers

També m’he fixat en [Pegueroles–Riera](https://github.com/falgarspegueroles/P2/blob/Pegueroles-Riera/src/vad.c). Quan estic en silenci, no incorporo qualsevol bloc al valor del soroll. Demano que la seva potència sigui menor que el soroll estimat més un marge.

La idea és no confondre una mica de veu fluixa amb el soroll normal. La cerca va ajustant aquest marge. Si he desactivat el seguiment del soroll, aquesta opció no canvia res.

Aquestes són idees que he vist en altres entregues. Les he adaptat al meu detector i les comparo amb la mateixa base de dades. No dono per fet que els seus valors siguin els millors per a mi.

## Quines combinacions he provat

Hi ha onze idees amb dues opcions cadascuna: activada o desactivada. Per això ara hi ha **2.048 combinacions d’interruptors**. Algunes fan el mateix, com permetre una baixada quan no hi ha espera de veu.

### Com comença la cerca

La cerca nova no llegeix els guanyadors anteriors per decidir on comença. Parteixo d’uns valors normals: 100 ms inicials, 50 ms de veu, 150 ms de silenci, marge de 6 dB, alfa de 0,01 i diferència d’1 dB entre llindars.

Per no dependre d’un sol començament, faig tres inicis. El primer surt una mica per sota d’aquests valors, el segon al centre i el tercer una mica per sobre. Els altres dos inicis surten de sumar o restar el pas inicial.

| Inici | Temps inicial | Veu mínima | Silenci mínim | Marge | Alfa aproximat | Diferència |
|---|---:|---:|---:|---:|---:|---:|
| Per sota | 50 ms | 20 ms | 100 ms | 4 dB | 0,0032 | 0,5 dB |
| Centre | 100 ms | 50 ms | 150 ms | 6 dB | 0,01 | 1 dB |
| Per sobre | 150 ms | 80 ms | 200 ms | 8 dB | 0,0316 | 1,5 dB |

Si una idea està desactivada, el seu valor queda fix: un bloc per a les esperes, alfa zero per al soroll fix i diferència zero si no hi ha histèresi.

### Com es va acostant als valors bons

1. Provo un valor una mica més baix i un una mica més alt que el que tinc.
2. Si algun dona millor TOTAL, hi moc el centre i continuo amb el mateix pas.
3. Si ja no millora, divideixo el pas per dos i torno a mirar els voltants.
4. Paro quan els passos són petits i ja no trobo cap millora.

També miro quatre punts on canvien marge i alfa alhora. Així puc sortir d’alguns casos en què canviar només un dels dos no ajuda.

Per a alfa faig servir passos proporcionals: al principi puc provar valors força diferents i després cada vegada més propers. Al fitxer del recorregut, `pas_log10_alfa` guarda aquest pas en escala logarítmica.

Els passos finals són un bloc de 10 ms per a les duracions, 0,01 dB per al marge i la histèresi, i aproximadament un 1 % per a alfa. No afegeixo expressament decimals rodons ni valors com 5,94 o 6,63 dB. Si apareixen, és perquè el recorregut hi arriba.

Poso límits amplis per no anar cap a valors absurds: 20–400 ms inicials, 20–200 ms de veu, 20–500 ms de silenci, marge de 2–14 dB, alfa entre 0,0001 i 0,1 i diferència entre llindars de 0,01–4 dB. La diferència ha de ser menor que el marge. Són els límits dins dels quals deixo que es mogui el programa.

Hi ha un màxim de 60 voltes per inici com a límit de temps. Amb les onze idees hi ha 6.144 inicis. Cap dels 6.144 inicis ha arribat al límit: tots han acabat amb el pas mínim i sense trobar més millora.

### Valors de les tres proves noves

També comencen amb valors normals i es mouen segons el resultat. Al centre faig servir 3.000 Hz de ZCR, una rebaixa de 2 dB, una pujada de confirmació de 3 dB, una espera màxima de 250 ms i un marge de 2 dB per actualitzar el soroll.

La cerca pot moure el ZCR entre 500 i 6.000 Hz, la rebaixa entre 0,1 i 6 dB, la pujada entre 0,1 i 8 dB, l’espera entre 20 i 600 ms i el marge del soroll entre 0 i 6 dB. La rebaixa ha de ser menor que el marge de veu, i l’espera no pot ser més curta que la duració mínima de veu.

Els passos finals són 25 Hz per al ZCR, 0,02 dB per a la rebaixa, 0,01 dB per als altres marges i un bloc per a l’espera.

### Què conservo de les proves anteriors

Els quatre grups històrics continuen servint per comparar les idees amb valors fixos. No serveixen per iniciar o orientar la cerca adaptativa.

| Grup històric | Blocs inicials | Blocs de veu | Blocs de silenci | Marge | Alfa |
|---|---:|---:|---:|---:|---:|
| Primer ajust | 20 | 5 | 15 | 8 dB | 0,02 |
| Base de 6 dB | 10 | 8 | 15 | 6 dB | 0,02 |
| Ajust de 6,63 dB | 10 | 8 | 15 | 6,63 dB | 0,02 |
| Base actual | 9 | 8 | 17 | 5,94 dB | 0,00615 |

Si hi ha histèresi, en aquestes comparacions fixes separo els llindars 1 dB. Ara són 8.192 files fixes: quatre grups de valors per a cadascuna de les 2.048 combinacions. Per als mètodes nous faig servir els valors centrals explicats abans.

La cerca amb onze idees ha calculat **676.929 configuracions diferents**. El recorregut queda guardat a `recorregut_cerca.csv`.

Conservo l’estudi amb vuit idees a `combinacions_vuit_metodes.csv`. La columna anterior de la matriu només té resultat quan les tres idees noves estan apagades. No hi poso una puntuació antiga en una combinació que abans no existia.

Pot ser que hi hagi valors millors que aquests tres inicis no trobin. A més, tot s’ha ajustat amb `db.v4`, no amb àudios nous.

## Com miro si dues idees es porten bé

Comparo files on només canvia un interruptor. Les altres idees i els valors són iguals. Hi ha 1.024 parelles per idea i per grup de valors. Les guardo a `canvis_per_parelles.csv`.

| Idea | Pitjor canvi en el TOTAL | Millor canvi en el TOTAL |
|---|---:|---:|
| Espera de veu | -10,283 punts | +1,441 punts |
| Espera de silenci | -2,962 punts | +8,034 punts |
| Seguiment del soroll | -1,470 punts | +1,107 punts |
| Histèresi | -0,951 punts | +1,054 punts |
| Treure el pic | -0,848 punts | +0,701 punts |
| Permetre una baixada | -0,092 punts | +0,349 punts |
| Treure la mitjana | -0,399 punts | +0,344 punts |
| Tornar al primer bloc | +0,000 punts | +9,928 punts |
| Rescat ZCR | -0,184 punts | +0,245 punts |
| Confirmació alta | -0,511 punts | +1,652 punts |
| Limitar el soroll | -0,815 punts | +0,887 punts |

Aquests canvis no són directament respecte de la base actual. Cada parella pot tenir altres idees activades. La taula serveix per veure si una idea ajuda més o menys segons amb què la barrejo.

## Quin resultat ha sortit

| Prova | TOTAL |
|---|---:|
| Base d’entrega | 95,829 % |
| Millor de l’estudi amb vuit idees | 95,891 % |
| Millor de l’estudi amb onze idees | **96,186 %** |

La millor configuració combina **rescat ZCR i confirmació amb llindar alt** amb les esperes de veu i silenci, el seguiment del soroll, una baixada permesa, treure la mitjana i tornar al primer bloc pendent. La histèresi, treure el pic inicial i el límit d’actualització del soroll queden apagats.

Els valors trobats són 100 ms inicials, 80 ms de veu mínima, 160 ms de silenci mínim, marge de **5,875 dB** i alfa d’aproximadament **0,005233**. El ZCR es compara amb **2.500 Hz**, amb una rebaixa de potència de **2,125 dB**. La confirmació exigeix arribar **7 dB** per sobre del llindar d’entrada abans de **250 ms**.

Guanya uns **0,295 punts** respecte de l’estudi amb vuit idees i **0,357 punts** respecte de la base d’entrega. Les puntuacions són de desenvolupament, amb `db.v4`.

El límit d’actualització del soroll també s’ha provat: la millor configuració que l’activa arriba a **96,182 %**. És molt propera a la guanyadora. No vol dir que aquesta idea sigui dolenta; només que aquí el millor resultat trobat la deixa apagada.

El detector per defecte de l’entrega no ha canviat. Les opcions noves són a la branca de combinacions i estan apagades per defecte.

<!-- inici-matriu-combinacions -->
## Matriu de totes les combinacions

Cada fila és una combinació. **✓** vol dir activat i **—** vol dir desactivat.

**Veu** i **Sil.** són les esperes; **Sor.** és el seguiment del soroll; **Hist.** són els dos llindars; **Pic** deixa fora el pic inicial; **Baix.** permet una baixada; **DC** treu la mitjana; **Ret.** torna al primer bloc pendent. **ZCR** rescata veu fluixa; **Conf.** exigeix arribar al llindar alt a temps; **Lím.** limita quins blocs actualitzen el soroll.

**Fix** fa servir els valors de la base i els valors inicials dels mètodes nous. **Anterior** és la cerca amb vuit idees; només hi ha resultat quan les tres noves estan apagades. **Adaptativa** és la cerca amb les onze idees. Els ajustos poden ser diferents a cada fila. Tots els resultats són sobre les mateixes 115 gravacions de `db.v4`.

La **C1800** és la base. La millor cerca nova és a **C1854**. Amb onze interruptors hi ha 2.048 files, de C0000 a C2047. Els números de l’estudi de vuit idees ja no són els mateixos.

| Combinació | Veu | Sil. | Sor. | Hist. | Pic | Baix. | DC | Ret. | ZCR | Conf. | Lím. | Fix (%) | Anterior (%) | Adaptativa (%) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---:|---:|---:|
| C0000 | — | — | — | — | — | — | — | — | — | — | — | 90,943 | 91,690 | 91,690 |
| C0001 | — | — | — | — | — | — | — | — | — | — | ✓ | 90,943 | — | 91,690 |
| C0002 | — | — | — | — | — | — | — | — | — | ✓ | — | 90,508 | — | 92,618 |
| C0003 | — | — | — | — | — | — | — | — | — | ✓ | ✓ | 90,508 | — | 92,618 |
| C0004 | — | — | — | — | — | — | — | — | ✓ | — | — | 91,125 | — | 91,747 |
| C0005 | — | — | — | — | — | — | — | — | ✓ | — | ✓ | 91,125 | — | 91,747 |
| C0006 | — | — | — | — | — | — | — | — | ✓ | ✓ | — | 90,614 | — | 93,079 |
| C0007 | — | — | — | — | — | — | — | — | ✓ | ✓ | ✓ | 90,614 | — | 93,079 |
| C0008 | — | — | — | — | — | — | — | ✓ | — | — | — | 90,943 | 91,690 | 91,690 |
| C0009 | — | — | — | — | — | — | — | ✓ | — | — | ✓ | 90,943 | — | 91,690 |
| C0010 | — | — | — | — | — | — | — | ✓ | — | ✓ | — | 91,000 | — | 93,438 |
| C0011 | — | — | — | — | — | — | — | ✓ | — | ✓ | ✓ | 91,000 | — | 93,438 |
| C0012 | — | — | — | — | — | — | — | ✓ | ✓ | — | — | 91,125 | — | 91,747 |
| C0013 | — | — | — | — | — | — | — | ✓ | ✓ | — | ✓ | 91,125 | — | 91,747 |
| C0014 | — | — | — | — | — | — | — | ✓ | ✓ | ✓ | — | 91,110 | — | 93,691 |
| C0015 | — | — | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,110 | — | 93,691 |
| C0016 | — | — | — | — | — | — | ✓ | — | — | — | — | 91,063 | 91,612 | 91,612 |
| C0017 | — | — | — | — | — | — | ✓ | — | — | — | ✓ | 91,063 | — | 91,612 |
| C0018 | — | — | — | — | — | — | ✓ | — | — | ✓ | — | 90,709 | — | 92,531 |
| C0019 | — | — | — | — | — | — | ✓ | — | — | ✓ | ✓ | 90,709 | — | 92,531 |
| C0020 | — | — | — | — | — | — | ✓ | — | ✓ | — | — | 91,211 | — | 91,701 |
| C0021 | — | — | — | — | — | — | ✓ | — | ✓ | — | ✓ | 91,211 | — | 91,701 |
| C0022 | — | — | — | — | — | — | ✓ | — | ✓ | ✓ | — | 90,794 | — | 92,863 |
| C0023 | — | — | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 90,794 | — | 92,863 |
| C0024 | — | — | — | — | — | — | ✓ | ✓ | — | — | — | 91,063 | 91,612 | 91,612 |
| C0025 | — | — | — | — | — | — | ✓ | ✓ | — | — | ✓ | 91,063 | — | 91,612 |
| C0026 | — | — | — | — | — | — | ✓ | ✓ | — | ✓ | — | 91,153 | — | 93,354 |
| C0027 | — | — | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,153 | — | 93,354 |
| C0028 | — | — | — | — | — | — | ✓ | ✓ | ✓ | — | — | 91,211 | — | 91,701 |
| C0029 | — | — | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,211 | — | 91,701 |
| C0030 | — | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 91,245 | — | 93,750 |
| C0031 | — | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,245 | — | 93,750 |
| C0032 | — | — | — | — | — | ✓ | — | — | — | — | — | 90,943 | 91,690 | 91,690 |
| C0033 | — | — | — | — | — | ✓ | — | — | — | — | ✓ | 90,943 | — | 91,690 |
| C0034 | — | — | — | — | — | ✓ | — | — | — | ✓ | — | 90,508 | — | 92,618 |
| C0035 | — | — | — | — | — | ✓ | — | — | — | ✓ | ✓ | 90,508 | — | 92,618 |
| C0036 | — | — | — | — | — | ✓ | — | — | ✓ | — | — | 91,125 | — | 91,747 |
| C0037 | — | — | — | — | — | ✓ | — | — | ✓ | — | ✓ | 91,125 | — | 91,747 |
| C0038 | — | — | — | — | — | ✓ | — | — | ✓ | ✓ | — | 90,614 | — | 93,079 |
| C0039 | — | — | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 90,614 | — | 93,079 |
| C0040 | — | — | — | — | — | ✓ | — | ✓ | — | — | — | 90,943 | 91,690 | 91,690 |
| C0041 | — | — | — | — | — | ✓ | — | ✓ | — | — | ✓ | 90,943 | — | 91,690 |
| C0042 | — | — | — | — | — | ✓ | — | ✓ | — | ✓ | — | 91,137 | — | 93,534 |
| C0043 | — | — | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,137 | — | 93,534 |
| C0044 | — | — | — | — | — | ✓ | — | ✓ | ✓ | — | — | 91,125 | — | 91,747 |
| C0045 | — | — | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,125 | — | 91,747 |
| C0046 | — | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 91,245 | — | 93,830 |
| C0047 | — | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,245 | — | 93,830 |
| C0048 | — | — | — | — | — | ✓ | ✓ | — | — | — | — | 91,063 | 91,612 | 91,612 |
| C0049 | — | — | — | — | — | ✓ | ✓ | — | — | — | ✓ | 91,063 | — | 91,612 |
| C0050 | — | — | — | — | — | ✓ | ✓ | — | — | ✓ | — | 90,709 | — | 92,531 |
| C0051 | — | — | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 90,709 | — | 92,531 |
| C0052 | — | — | — | — | — | ✓ | ✓ | — | ✓ | — | — | 91,211 | — | 91,701 |
| C0053 | — | — | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 91,211 | — | 91,701 |
| C0054 | — | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 90,794 | — | 92,863 |
| C0055 | — | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 90,794 | — | 92,863 |
| C0056 | — | — | — | — | — | ✓ | ✓ | ✓ | — | — | — | 91,063 | 91,612 | 91,612 |
| C0057 | — | — | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,063 | — | 91,612 |
| C0058 | — | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 91,248 | — | 93,402 |
| C0059 | — | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,248 | — | 93,402 |
| C0060 | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,211 | — | 91,701 |
| C0061 | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,211 | — | 91,701 |
| C0062 | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,341 | — | 93,874 |
| C0063 | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,341 | — | 93,874 |
| C0064 | — | — | — | — | ✓ | — | — | — | — | — | — | 91,180 | 91,674 | 91,674 |
| C0065 | — | — | — | — | ✓ | — | — | — | — | — | ✓ | 91,180 | — | 91,674 |
| C0066 | — | — | — | — | ✓ | — | — | — | — | ✓ | — | 90,869 | — | 92,776 |
| C0067 | — | — | — | — | ✓ | — | — | — | — | ✓ | ✓ | 90,869 | — | 92,776 |
| C0068 | — | — | — | — | ✓ | — | — | — | ✓ | — | — | 91,339 | — | 91,759 |
| C0069 | — | — | — | — | ✓ | — | — | — | ✓ | — | ✓ | 91,339 | — | 91,759 |
| C0070 | — | — | — | — | ✓ | — | — | — | ✓ | ✓ | — | 90,982 | — | 92,704 |
| C0071 | — | — | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 90,982 | — | 92,704 |
| C0072 | — | — | — | — | ✓ | — | — | ✓ | — | — | — | 91,180 | 91,674 | 91,674 |
| C0073 | — | — | — | — | ✓ | — | — | ✓ | — | — | ✓ | 91,180 | — | 91,674 |
| C0074 | — | — | — | — | ✓ | — | — | ✓ | — | ✓ | — | 91,302 | — | 93,598 |
| C0075 | — | — | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 91,302 | — | 93,598 |
| C0076 | — | — | — | — | ✓ | — | — | ✓ | ✓ | — | — | 91,339 | — | 91,759 |
| C0077 | — | — | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 91,339 | — | 91,759 |
| C0078 | — | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 91,418 | — | 93,737 |
| C0079 | — | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 91,418 | — | 93,737 |
| C0080 | — | — | — | — | ✓ | — | ✓ | — | — | — | — | 91,214 | 91,610 | 91,610 |
| C0081 | — | — | — | — | ✓ | — | ✓ | — | — | — | ✓ | 91,214 | — | 91,610 |
| C0082 | — | — | — | — | ✓ | — | ✓ | — | — | ✓ | — | 90,977 | — | 92,696 |
| C0083 | — | — | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 90,977 | — | 92,696 |
| C0084 | — | — | — | — | ✓ | — | ✓ | — | ✓ | — | — | 91,360 | — | 91,724 |
| C0085 | — | — | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 91,360 | — | 91,724 |
| C0086 | — | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 91,089 | — | 92,905 |
| C0087 | — | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 91,089 | — | 92,905 |
| C0088 | — | — | — | — | ✓ | — | ✓ | ✓ | — | — | — | 91,214 | 91,610 | 91,610 |
| C0089 | — | — | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 91,214 | — | 91,610 |
| C0090 | — | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 91,382 | — | 93,392 |
| C0091 | — | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 91,382 | — | 93,392 |
| C0092 | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 91,360 | — | 91,724 |
| C0093 | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 91,360 | — | 91,724 |
| C0094 | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 91,516 | — | 93,564 |
| C0095 | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,516 | — | 93,564 |
| C0096 | — | — | — | — | ✓ | ✓ | — | — | — | — | — | 91,180 | 91,674 | 91,674 |
| C0097 | — | — | — | — | ✓ | ✓ | — | — | — | — | ✓ | 91,180 | — | 91,674 |
| C0098 | — | — | — | — | ✓ | ✓ | — | — | — | ✓ | — | 90,869 | — | 92,776 |
| C0099 | — | — | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 90,869 | — | 92,776 |
| C0100 | — | — | — | — | ✓ | ✓ | — | — | ✓ | — | — | 91,339 | — | 91,759 |
| C0101 | — | — | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 91,339 | — | 91,759 |
| C0102 | — | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 90,982 | — | 92,704 |
| C0103 | — | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 90,982 | — | 92,704 |
| C0104 | — | — | — | — | ✓ | ✓ | — | ✓ | — | — | — | 91,180 | 91,674 | 91,674 |
| C0105 | — | — | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 91,180 | — | 91,674 |
| C0106 | — | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 91,381 | — | 93,669 |
| C0107 | — | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 91,381 | — | 93,669 |
| C0108 | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 91,339 | — | 91,759 |
| C0109 | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 91,339 | — | 91,759 |
| C0110 | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 91,503 | — | 93,877 |
| C0111 | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,503 | — | 93,877 |
| C0112 | — | — | — | — | ✓ | ✓ | ✓ | — | — | — | — | 91,214 | 91,610 | 91,610 |
| C0113 | — | — | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 91,214 | — | 91,610 |
| C0114 | — | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 90,977 | — | 92,696 |
| C0115 | — | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 90,977 | — | 92,696 |
| C0116 | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 91,360 | — | 91,724 |
| C0117 | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 91,360 | — | 91,724 |
| C0118 | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 91,089 | — | 92,905 |
| C0119 | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,089 | — | 92,905 |
| C0120 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 91,214 | 91,610 | 91,610 |
| C0121 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 91,214 | — | 91,610 |
| C0122 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 91,461 | — | 93,458 |
| C0123 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,461 | — | 93,458 |
| C0124 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 91,360 | — | 91,724 |
| C0125 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,360 | — | 91,724 |
| C0126 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,595 | — | 93,784 |
| C0127 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,595 | — | 93,784 |
| C0128 | — | — | — | ✓ | — | — | — | — | — | — | — | 91,408 | 92,551 | 92,551 |
| C0129 | — | — | — | ✓ | — | — | — | — | — | — | ✓ | 91,408 | — | 92,551 |
| C0130 | — | — | — | ✓ | — | — | — | — | — | ✓ | — | 91,113 | — | 93,239 |
| C0131 | — | — | — | ✓ | — | — | — | — | — | ✓ | ✓ | 91,113 | — | 93,239 |
| C0132 | — | — | — | ✓ | — | — | — | — | ✓ | — | — | 91,570 | — | 92,559 |
| C0133 | — | — | — | ✓ | — | — | — | — | ✓ | — | ✓ | 91,570 | — | 92,559 |
| C0134 | — | — | — | ✓ | — | — | — | — | ✓ | ✓ | — | 91,233 | — | 93,245 |
| C0135 | — | — | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 91,233 | — | 93,245 |
| C0136 | — | — | — | ✓ | — | — | — | ✓ | — | — | — | 91,408 | 92,551 | 92,551 |
| C0137 | — | — | — | ✓ | — | — | — | ✓ | — | — | ✓ | 91,408 | — | 92,551 |
| C0138 | — | — | — | ✓ | — | — | — | ✓ | — | ✓ | — | 91,508 | — | 93,798 |
| C0139 | — | — | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 91,508 | — | 93,798 |
| C0140 | — | — | — | ✓ | — | — | — | ✓ | ✓ | — | — | 91,570 | — | 92,559 |
| C0141 | — | — | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 91,570 | — | 92,559 |
| C0142 | — | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 91,632 | — | 93,782 |
| C0143 | — | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,632 | — | 93,782 |
| C0144 | — | — | — | ✓ | — | — | ✓ | — | — | — | — | 91,440 | 92,511 | 92,511 |
| C0145 | — | — | — | ✓ | — | — | ✓ | — | — | — | ✓ | 91,440 | — | 92,511 |
| C0146 | — | — | — | ✓ | — | — | ✓ | — | — | ✓ | — | 91,196 | — | 93,092 |
| C0147 | — | — | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 91,196 | — | 93,092 |
| C0148 | — | — | — | ✓ | — | — | ✓ | — | ✓ | — | — | 91,572 | — | 92,535 |
| C0149 | — | — | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 91,572 | — | 92,535 |
| C0150 | — | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 91,300 | — | 93,127 |
| C0151 | — | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 91,300 | — | 93,127 |
| C0152 | — | — | — | ✓ | — | — | ✓ | ✓ | — | — | — | 91,440 | 92,511 | 92,511 |
| C0153 | — | — | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 91,440 | — | 92,511 |
| C0154 | — | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 91,568 | — | 93,683 |
| C0155 | — | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,568 | — | 93,683 |
| C0156 | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 91,572 | — | 92,535 |
| C0157 | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,572 | — | 92,535 |
| C0158 | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 91,680 | — | 93,768 |
| C0159 | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,680 | — | 93,768 |
| C0160 | — | — | — | ✓ | — | ✓ | — | — | — | — | — | 91,408 | 92,551 | 92,551 |
| C0161 | — | — | — | ✓ | — | ✓ | — | — | — | — | ✓ | 91,408 | — | 92,551 |
| C0162 | — | — | — | ✓ | — | ✓ | — | — | — | ✓ | — | 91,113 | — | 93,239 |
| C0163 | — | — | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 91,113 | — | 93,239 |
| C0164 | — | — | — | ✓ | — | ✓ | — | — | ✓ | — | — | 91,570 | — | 92,559 |
| C0165 | — | — | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 91,570 | — | 92,559 |
| C0166 | — | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 91,233 | — | 93,245 |
| C0167 | — | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 91,233 | — | 93,245 |
| C0168 | — | — | — | ✓ | — | ✓ | — | ✓ | — | — | — | 91,408 | 92,551 | 92,551 |
| C0169 | — | — | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 91,408 | — | 92,551 |
| C0170 | — | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 91,620 | — | 93,877 |
| C0171 | — | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,620 | — | 93,877 |
| C0172 | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 91,570 | — | 92,559 |
| C0173 | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,570 | — | 92,559 |
| C0174 | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 91,749 | — | 93,849 |
| C0175 | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,749 | — | 93,849 |
| C0176 | — | — | — | ✓ | — | ✓ | ✓ | — | — | — | — | 91,440 | 92,511 | 92,511 |
| C0177 | — | — | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 91,440 | — | 92,511 |
| C0178 | — | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 91,196 | — | 93,092 |
| C0179 | — | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,196 | — | 93,092 |
| C0180 | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 91,572 | — | 92,535 |
| C0181 | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 91,572 | — | 92,535 |
| C0182 | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 91,300 | — | 93,127 |
| C0183 | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,300 | — | 93,127 |
| C0184 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 91,440 | 92,511 | 92,511 |
| C0185 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,440 | — | 92,511 |
| C0186 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 91,643 | — | 93,730 |
| C0187 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,643 | — | 93,730 |
| C0188 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,572 | — | 92,535 |
| C0189 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,572 | — | 92,535 |
| C0190 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,756 | — | 93,779 |
| C0191 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,756 | — | 93,779 |
| C0192 | — | — | — | ✓ | ✓ | — | — | — | — | — | — | 91,567 | 92,560 | 92,560 |
| C0193 | — | — | — | ✓ | ✓ | — | — | — | — | — | ✓ | 91,567 | — | 92,560 |
| C0194 | — | — | — | ✓ | ✓ | — | — | — | — | ✓ | — | 91,421 | — | 93,281 |
| C0195 | — | — | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 91,421 | — | 93,281 |
| C0196 | — | — | — | ✓ | ✓ | — | — | — | ✓ | — | — | 91,704 | — | 92,586 |
| C0197 | — | — | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 91,704 | — | 92,586 |
| C0198 | — | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 91,524 | — | 93,294 |
| C0199 | — | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 91,524 | — | 93,294 |
| C0200 | — | — | — | ✓ | ✓ | — | — | ✓ | — | — | — | 91,567 | 92,560 | 92,560 |
| C0201 | — | — | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 91,567 | — | 92,560 |
| C0202 | — | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 91,783 | — | 93,848 |
| C0203 | — | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 91,783 | — | 93,848 |
| C0204 | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 91,704 | — | 92,586 |
| C0205 | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 91,704 | — | 92,586 |
| C0206 | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 91,902 | — | 93,874 |
| C0207 | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 91,902 | — | 93,874 |
| C0208 | — | — | — | ✓ | ✓ | — | ✓ | — | — | — | — | 91,524 | 92,476 | 92,476 |
| C0209 | — | — | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 91,524 | — | 92,476 |
| C0210 | — | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 91,436 | — | 93,080 |
| C0211 | — | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 91,436 | — | 93,080 |
| C0212 | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 91,650 | — | 92,504 |
| C0213 | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 91,650 | — | 92,504 |
| C0214 | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 91,543 | — | 93,145 |
| C0215 | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 91,543 | — | 93,145 |
| C0216 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 91,524 | 92,476 | 92,476 |
| C0217 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 91,524 | — | 92,476 |
| C0218 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 91,798 | — | 93,638 |
| C0219 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 91,798 | — | 93,638 |
| C0220 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 91,650 | — | 92,504 |
| C0221 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 91,650 | — | 92,504 |
| C0222 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 91,907 | — | 93,669 |
| C0223 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,907 | — | 93,669 |
| C0224 | — | — | — | ✓ | ✓ | ✓ | — | — | — | — | — | 91,567 | 92,560 | 92,560 |
| C0225 | — | — | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 91,567 | — | 92,560 |
| C0226 | — | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 91,421 | — | 93,281 |
| C0227 | — | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 91,421 | — | 93,281 |
| C0228 | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 91,704 | — | 92,586 |
| C0229 | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 91,704 | — | 92,586 |
| C0230 | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 91,524 | — | 93,294 |
| C0231 | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 91,524 | — | 93,294 |
| C0232 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 91,567 | 92,560 | 92,560 |
| C0233 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 91,567 | — | 92,560 |
| C0234 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 91,835 | — | 93,891 |
| C0235 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 91,835 | — | 93,891 |
| C0236 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 91,704 | — | 92,586 |
| C0237 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 91,704 | — | 92,586 |
| C0238 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 91,963 | — | 93,926 |
| C0239 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,963 | — | 93,926 |
| C0240 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 91,524 | 92,476 | 92,476 |
| C0241 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 91,524 | — | 92,476 |
| C0242 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 91,436 | — | 93,080 |
| C0243 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 91,436 | — | 93,080 |
| C0244 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 91,650 | — | 92,504 |
| C0245 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 91,650 | — | 92,504 |
| C0246 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 91,543 | — | 93,145 |
| C0247 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,543 | — | 93,145 |
| C0248 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 91,524 | 92,476 | 92,476 |
| C0249 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 91,524 | — | 92,476 |
| C0250 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 91,860 | — | 93,572 |
| C0251 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,860 | — | 93,572 |
| C0252 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 91,650 | — | 92,504 |
| C0253 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,650 | — | 92,504 |
| C0254 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,970 | — | 93,763 |
| C0255 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,970 | — | 93,763 |
| C0256 | — | — | ✓ | — | — | — | — | — | — | — | — | 91,244 | 91,827 | 91,827 |
| C0257 | — | — | ✓ | — | — | — | — | — | — | — | ✓ | 91,388 | — | 91,840 |
| C0258 | — | — | ✓ | — | — | — | — | — | — | ✓ | — | 90,813 | — | 92,990 |
| C0259 | — | — | ✓ | — | — | — | — | — | — | ✓ | ✓ | 91,199 | — | 92,987 |
| C0260 | — | — | ✓ | — | — | — | — | — | ✓ | — | — | 91,422 | — | 91,943 |
| C0261 | — | — | ✓ | — | — | — | — | — | ✓ | — | ✓ | 91,523 | — | 91,917 |
| C0262 | — | — | ✓ | — | — | — | — | — | ✓ | ✓ | — | 90,960 | — | 93,071 |
| C0263 | — | — | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | 91,306 | — | 93,145 |
| C0264 | — | — | ✓ | — | — | — | — | ✓ | — | — | — | 91,244 | 91,827 | 91,827 |
| C0265 | — | — | ✓ | — | — | — | — | ✓ | — | — | ✓ | 91,388 | — | 91,840 |
| C0266 | — | — | ✓ | — | — | — | — | ✓ | — | ✓ | — | 91,268 | — | 93,702 |
| C0267 | — | — | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | 91,614 | — | 93,721 |
| C0268 | — | — | ✓ | — | — | — | — | ✓ | ✓ | — | — | 91,422 | — | 91,943 |
| C0269 | — | — | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | 91,523 | — | 91,917 |
| C0270 | — | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | 91,407 | — | 93,973 |
| C0271 | — | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,717 | — | 94,043 |
| C0272 | — | — | ✓ | — | — | — | ✓ | — | — | — | — | 91,257 | 91,769 | 91,769 |
| C0273 | — | — | ✓ | — | — | — | ✓ | — | — | — | ✓ | 91,387 | — | 91,762 |
| C0274 | — | — | ✓ | — | — | — | ✓ | — | — | ✓ | — | 90,889 | — | 92,968 |
| C0275 | — | — | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | 91,264 | — | 92,968 |
| C0276 | — | — | ✓ | — | — | — | ✓ | — | ✓ | — | — | 91,446 | — | 91,885 |
| C0277 | — | — | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | 91,526 | — | 91,889 |
| C0278 | — | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | 91,052 | — | 92,954 |
| C0279 | — | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 91,361 | — | 92,989 |
| C0280 | — | — | ✓ | — | — | — | ✓ | ✓ | — | — | — | 91,257 | 91,769 | 91,769 |
| C0281 | — | — | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | 91,387 | — | 91,762 |
| C0282 | — | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | 91,330 | — | 93,630 |
| C0283 | — | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,670 | — | 93,630 |
| C0284 | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | 91,446 | — | 91,885 |
| C0285 | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,526 | — | 91,889 |
| C0286 | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 91,471 | — | 93,931 |
| C0287 | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,767 | — | 94,012 |
| C0288 | — | — | ✓ | — | — | ✓ | — | — | — | — | — | 91,244 | 91,827 | 91,827 |
| C0289 | — | — | ✓ | — | — | ✓ | — | — | — | — | ✓ | 91,388 | — | 91,840 |
| C0290 | — | — | ✓ | — | — | ✓ | — | — | — | ✓ | — | 90,817 | — | 92,986 |
| C0291 | — | — | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | 91,197 | — | 92,986 |
| C0292 | — | — | ✓ | — | — | ✓ | — | — | ✓ | — | — | 91,422 | — | 91,943 |
| C0293 | — | — | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | 91,523 | — | 91,917 |
| C0294 | — | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | 90,963 | — | 93,064 |
| C0295 | — | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 91,306 | — | 93,139 |
| C0296 | — | — | ✓ | — | — | ✓ | — | ✓ | — | — | — | 91,244 | 91,827 | 91,827 |
| C0297 | — | — | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | 91,388 | — | 91,840 |
| C0298 | — | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | 91,396 | — | 93,827 |
| C0299 | — | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,715 | — | 93,827 |
| C0300 | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | 91,422 | — | 91,943 |
| C0301 | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,523 | — | 91,917 |
| C0302 | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 91,521 | — | 94,066 |
| C0303 | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,828 | — | 94,185 |
| C0304 | — | — | ✓ | — | — | ✓ | ✓ | — | — | — | — | 91,257 | 91,769 | 91,769 |
| C0305 | — | — | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | 91,387 | — | 91,762 |
| C0306 | — | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | 90,929 | — | 92,924 |
| C0307 | — | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,267 | — | 92,953 |
| C0308 | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | 91,446 | — | 91,885 |
| C0309 | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 91,526 | — | 91,889 |
| C0310 | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 91,089 | — | 92,944 |
| C0311 | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,365 | — | 93,001 |
| C0312 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | 91,257 | 91,769 | 91,769 |
| C0313 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,387 | — | 91,762 |
| C0314 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 91,450 | — | 93,694 |
| C0315 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,717 | — | 93,694 |
| C0316 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,446 | — | 91,885 |
| C0317 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,526 | — | 91,889 |
| C0318 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,591 | — | 94,025 |
| C0319 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,842 | — | 94,154 |
| C0320 | — | — | ✓ | — | ✓ | — | — | — | — | — | — | 91,371 | 91,853 | 91,853 |
| C0321 | — | — | ✓ | — | ✓ | — | — | — | — | — | ✓ | 91,473 | — | 91,853 |
| C0322 | — | — | ✓ | — | ✓ | — | — | — | — | ✓ | — | 90,993 | — | 93,046 |
| C0323 | — | — | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | 91,363 | — | 93,069 |
| C0324 | — | — | ✓ | — | ✓ | — | — | — | ✓ | — | — | 91,530 | — | 91,966 |
| C0325 | — | — | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | 91,608 | — | 91,966 |
| C0326 | — | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | 91,135 | — | 93,113 |
| C0327 | — | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 91,467 | — | 93,215 |
| C0328 | — | — | ✓ | — | ✓ | — | — | ✓ | — | — | — | 91,371 | 91,853 | 91,853 |
| C0329 | — | — | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | 91,473 | — | 91,853 |
| C0330 | — | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | 91,448 | — | 93,693 |
| C0331 | — | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 91,731 | — | 93,696 |
| C0332 | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | 91,530 | — | 91,966 |
| C0333 | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 91,608 | — | 91,966 |
| C0334 | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 91,587 | — | 93,967 |
| C0335 | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 91,839 | — | 94,075 |
| C0336 | — | — | ✓ | — | ✓ | — | ✓ | — | — | — | — | 91,396 | 91,830 | 91,830 |
| C0337 | — | — | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | 91,453 | — | 91,780 |
| C0338 | — | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | 91,110 | — | 93,035 |
| C0339 | — | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 91,407 | — | 93,035 |
| C0340 | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | 91,560 | — | 91,923 |
| C0341 | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 91,580 | — | 91,924 |
| C0342 | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 91,232 | — | 93,005 |
| C0343 | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 91,495 | — | 93,091 |
| C0344 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | 91,396 | 91,830 | 91,830 |
| C0345 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 91,453 | — | 91,780 |
| C0346 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 91,542 | — | 93,625 |
| C0347 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 91,752 | — | 93,625 |
| C0348 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 91,560 | — | 91,923 |
| C0349 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 91,580 | — | 91,924 |
| C0350 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 91,658 | — | 93,873 |
| C0351 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,841 | — | 94,041 |
| C0352 | — | — | ✓ | — | ✓ | ✓ | — | — | — | — | — | 91,371 | 91,853 | 91,853 |
| C0353 | — | — | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | 91,473 | — | 91,853 |
| C0354 | — | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | 91,026 | — | 93,057 |
| C0355 | — | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 91,358 | — | 93,087 |
| C0356 | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | 91,530 | — | 91,966 |
| C0357 | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 91,608 | — | 91,966 |
| C0358 | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 91,159 | — | 93,106 |
| C0359 | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 91,466 | — | 93,235 |
| C0360 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | 91,371 | 91,853 | 91,853 |
| C0361 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 91,473 | — | 91,853 |
| C0362 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 91,563 | — | 93,805 |
| C0363 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 91,781 | — | 93,805 |
| C0364 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 91,530 | — | 91,966 |
| C0365 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 91,608 | — | 91,966 |
| C0366 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 91,690 | — | 94,036 |
| C0367 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,906 | — | 94,181 |
| C0368 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | 91,396 | 91,830 | 91,830 |
| C0369 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 91,453 | — | 91,780 |
| C0370 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 91,139 | — | 93,035 |
| C0371 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 91,405 | — | 93,035 |
| C0372 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 91,560 | — | 91,923 |
| C0373 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 91,580 | — | 91,924 |
| C0374 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 91,263 | — | 92,955 |
| C0375 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,493 | — | 93,053 |
| C0376 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 91,396 | 91,830 | 91,830 |
| C0377 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 91,453 | — | 91,780 |
| C0378 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 91,626 | — | 93,695 |
| C0379 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,774 | — | 93,695 |
| C0380 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 91,560 | — | 91,923 |
| C0381 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,580 | — | 91,924 |
| C0382 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,748 | — | 94,030 |
| C0383 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,893 | — | 94,156 |
| C0384 | — | — | ✓ | ✓ | — | — | — | — | — | — | — | 91,722 | 92,739 | 92,739 |
| C0385 | — | — | ✓ | ✓ | — | — | — | — | — | — | ✓ | 91,714 | — | 92,751 |
| C0386 | — | — | ✓ | ✓ | — | — | — | — | — | ✓ | — | 91,448 | — | 93,455 |
| C0387 | — | — | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | 91,704 | — | 93,463 |
| C0388 | — | — | ✓ | ✓ | — | — | — | — | ✓ | — | — | 91,864 | — | 92,891 |
| C0389 | — | — | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | 91,847 | — | 92,909 |
| C0390 | — | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | 91,542 | — | 93,470 |
| C0391 | — | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 91,794 | — | 93,375 |
| C0392 | — | — | ✓ | ✓ | — | — | — | ✓ | — | — | — | 91,722 | 92,739 | 92,739 |
| C0393 | — | — | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | 91,714 | — | 92,751 |
| C0394 | — | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | 91,839 | — | 93,928 |
| C0395 | — | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 92,035 | — | 93,949 |
| C0396 | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | 91,864 | — | 92,891 |
| C0397 | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 91,847 | — | 92,909 |
| C0398 | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 91,924 | — | 93,974 |
| C0399 | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 92,123 | — | 93,996 |
| C0400 | — | — | ✓ | ✓ | — | — | ✓ | — | — | — | — | 91,691 | 92,767 | 92,767 |
| C0401 | — | — | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | 91,665 | — | 92,771 |
| C0402 | — | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | 91,451 | — | 93,316 |
| C0403 | — | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 91,688 | — | 93,286 |
| C0404 | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | 91,823 | — | 93,012 |
| C0405 | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 91,781 | — | 92,973 |
| C0406 | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 91,551 | — | 93,341 |
| C0407 | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 91,763 | — | 93,365 |
| C0408 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | 91,691 | 92,767 | 92,767 |
| C0409 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 91,665 | — | 92,771 |
| C0410 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 91,820 | — | 93,887 |
| C0411 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 92,015 | — | 93,910 |
| C0412 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 91,823 | — | 93,012 |
| C0413 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,781 | — | 92,973 |
| C0414 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 91,908 | — | 93,951 |
| C0415 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 92,091 | — | 93,987 |
| C0416 | — | — | ✓ | ✓ | — | ✓ | — | — | — | — | — | 91,722 | 92,739 | 92,739 |
| C0417 | — | — | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | 91,714 | — | 92,751 |
| C0418 | — | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | 91,459 | — | 93,469 |
| C0419 | — | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 91,705 | — | 93,471 |
| C0420 | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | 91,864 | — | 92,891 |
| C0421 | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 91,847 | — | 92,909 |
| C0422 | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 91,552 | — | 93,484 |
| C0423 | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 91,795 | — | 93,486 |
| C0424 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | 91,722 | 92,739 | 92,739 |
| C0425 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 91,714 | — | 92,751 |
| C0426 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 91,929 | — | 93,985 |
| C0427 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 92,112 | — | 93,973 |
| C0428 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 91,864 | — | 92,891 |
| C0429 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,847 | — | 92,909 |
| C0430 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 92,012 | — | 93,997 |
| C0431 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 92,217 | — | 94,055 |
| C0432 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | 91,691 | 92,767 | 92,767 |
| C0433 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 91,665 | — | 92,771 |
| C0434 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 91,484 | — | 93,289 |
| C0435 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,686 | — | 93,289 |
| C0436 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 91,823 | — | 93,012 |
| C0437 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 91,781 | — | 92,973 |
| C0438 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 91,580 | — | 93,351 |
| C0439 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,761 | — | 93,313 |
| C0440 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 91,691 | 92,767 | 92,767 |
| C0441 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,665 | — | 92,771 |
| C0442 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 91,911 | — | 93,947 |
| C0443 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 92,061 | — | 93,979 |
| C0444 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,823 | — | 93,012 |
| C0445 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,781 | — | 92,973 |
| C0446 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 92,005 | — | 94,044 |
| C0447 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 92,158 | — | 94,055 |
| C0448 | — | — | ✓ | ✓ | ✓ | — | — | — | — | — | — | 91,762 | 92,778 | 92,778 |
| C0449 | — | — | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | 91,749 | — | 92,780 |
| C0450 | — | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | 91,573 | — | 93,452 |
| C0451 | — | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 91,774 | — | 93,470 |
| C0452 | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | 91,895 | — | 92,908 |
| C0453 | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 91,875 | — | 92,858 |
| C0454 | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 91,671 | — | 93,445 |
| C0455 | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 91,849 | — | 93,423 |
| C0456 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | 91,762 | 92,778 | 92,778 |
| C0457 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 91,749 | — | 92,780 |
| C0458 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 91,950 | — | 94,003 |
| C0459 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 92,093 | — | 93,973 |
| C0460 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 91,895 | — | 92,908 |
| C0461 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 91,875 | — | 92,858 |
| C0462 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 92,051 | — | 94,037 |
| C0463 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 92,183 | — | 94,037 |
| C0464 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | 91,752 | 92,738 | 92,738 |
| C0465 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 91,697 | — | 92,729 |
| C0466 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 91,579 | — | 93,292 |
| C0467 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 91,752 | — | 93,290 |
| C0468 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 91,871 | — | 92,775 |
| C0469 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 91,795 | — | 92,782 |
| C0470 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 91,662 | — | 93,292 |
| C0471 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 91,817 | — | 93,325 |
| C0472 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 91,752 | 92,738 | 92,738 |
| C0473 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 91,697 | — | 92,729 |
| C0474 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 91,935 | — | 93,844 |
| C0475 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 92,068 | — | 93,850 |
| C0476 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 91,871 | — | 92,775 |
| C0477 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 91,795 | — | 92,782 |
| C0478 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 92,021 | — | 93,895 |
| C0479 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 92,140 | — | 93,879 |
| C0480 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | 91,762 | 92,778 | 92,778 |
| C0481 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 91,749 | — | 92,780 |
| C0482 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 91,600 | — | 93,487 |
| C0483 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 91,776 | — | 93,487 |
| C0484 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 91,895 | — | 92,908 |
| C0485 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 91,875 | — | 92,858 |
| C0486 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 91,688 | — | 93,436 |
| C0487 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 91,850 | — | 93,470 |
| C0488 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 91,762 | 92,778 | 92,778 |
| C0489 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 91,749 | — | 92,780 |
| C0490 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 92,023 | — | 94,014 |
| C0491 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 92,123 | — | 94,030 |
| C0492 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 91,895 | — | 92,908 |
| C0493 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 91,875 | — | 92,858 |
| C0494 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 92,122 | — | 94,067 |
| C0495 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 92,234 | — | 94,106 |
| C0496 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 91,752 | 92,738 | 92,738 |
| C0497 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 91,697 | — | 92,729 |
| C0498 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 91,573 | — | 93,286 |
| C0499 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 91,749 | — | 93,298 |
| C0500 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 91,871 | — | 92,775 |
| C0501 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 91,795 | — | 92,782 |
| C0502 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 91,658 | — | 93,308 |
| C0503 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,814 | — | 93,316 |
| C0504 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 91,752 | 92,738 | 92,738 |
| C0505 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 91,697 | — | 92,729 |
| C0506 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 91,983 | — | 93,872 |
| C0507 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 92,095 | — | 93,872 |
| C0508 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 91,871 | — | 92,775 |
| C0509 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,795 | — | 92,782 |
| C0510 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 92,075 | — | 93,951 |
| C0511 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 92,192 | — | 93,980 |
| C0512 | — | ✓ | — | — | — | — | — | — | — | — | — | 91,736 | 94,494 | 94,494 |
| C0513 | — | ✓ | — | — | — | — | — | — | — | — | ✓ | 91,736 | — | 94,494 |
| C0514 | — | ✓ | — | — | — | — | — | — | — | ✓ | — | 92,823 | — | 94,563 |
| C0515 | — | ✓ | — | — | — | — | — | — | — | ✓ | ✓ | 92,823 | — | 94,563 |
| C0516 | — | ✓ | — | — | — | — | — | — | ✓ | — | — | 91,669 | — | 94,785 |
| C0517 | — | ✓ | — | — | — | — | — | — | ✓ | — | ✓ | 91,669 | — | 94,785 |
| C0518 | — | ✓ | — | — | — | — | — | — | ✓ | ✓ | — | 92,793 | — | 94,812 |
| C0519 | — | ✓ | — | — | — | — | — | — | ✓ | ✓ | ✓ | 92,793 | — | 94,812 |
| C0520 | — | ✓ | — | — | — | — | — | ✓ | — | — | — | 94,958 | 95,223 | 95,223 |
| C0521 | — | ✓ | — | — | — | — | — | ✓ | — | — | ✓ | 94,958 | — | 95,223 |
| C0522 | — | ✓ | — | — | — | — | — | ✓ | — | ✓ | — | 95,381 | — | 95,727 |
| C0523 | — | ✓ | — | — | — | — | — | ✓ | — | ✓ | ✓ | 95,381 | — | 95,727 |
| C0524 | — | ✓ | — | — | — | — | — | ✓ | ✓ | — | — | 94,997 | — | 95,546 |
| C0525 | — | ✓ | — | — | — | — | — | ✓ | ✓ | — | ✓ | 94,997 | — | 95,546 |
| C0526 | — | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | — | 95,433 | — | 95,767 |
| C0527 | — | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 95,433 | — | 95,767 |
| C0528 | — | ✓ | — | — | — | — | ✓ | — | — | — | — | 91,539 | 94,474 | 94,474 |
| C0529 | — | ✓ | — | — | — | — | ✓ | — | — | — | ✓ | 91,539 | — | 94,474 |
| C0530 | — | ✓ | — | — | — | — | ✓ | — | — | ✓ | — | 92,477 | — | 94,445 |
| C0531 | — | ✓ | — | — | — | — | ✓ | — | — | ✓ | ✓ | 92,477 | — | 94,445 |
| C0532 | — | ✓ | — | — | — | — | ✓ | — | ✓ | — | — | 91,449 | — | 94,740 |
| C0533 | — | ✓ | — | — | — | — | ✓ | — | ✓ | — | ✓ | 91,449 | — | 94,740 |
| C0534 | — | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | — | 92,436 | — | 94,769 |
| C0535 | — | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 92,436 | — | 94,769 |
| C0536 | — | ✓ | — | — | — | — | ✓ | ✓ | — | — | — | 94,864 | 95,229 | 95,229 |
| C0537 | — | ✓ | — | — | — | — | ✓ | ✓ | — | — | ✓ | 94,864 | — | 95,229 |
| C0538 | — | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | — | 95,201 | — | 95,477 |
| C0539 | — | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 95,201 | — | 95,477 |
| C0540 | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | — | 94,902 | — | 95,520 |
| C0541 | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 94,902 | — | 95,520 |
| C0542 | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 95,251 | — | 95,824 |
| C0543 | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 95,251 | — | 95,824 |
| C0544 | — | ✓ | — | — | — | ✓ | — | — | — | — | — | 91,736 | 94,494 | 94,494 |
| C0545 | — | ✓ | — | — | — | ✓ | — | — | — | — | ✓ | 91,736 | — | 94,494 |
| C0546 | — | ✓ | — | — | — | ✓ | — | — | — | ✓ | — | 92,823 | — | 94,563 |
| C0547 | — | ✓ | — | — | — | ✓ | — | — | — | ✓ | ✓ | 92,823 | — | 94,563 |
| C0548 | — | ✓ | — | — | — | ✓ | — | — | ✓ | — | — | 91,669 | — | 94,785 |
| C0549 | — | ✓ | — | — | — | ✓ | — | — | ✓ | — | ✓ | 91,669 | — | 94,785 |
| C0550 | — | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | — | 92,793 | — | 94,812 |
| C0551 | — | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 92,793 | — | 94,812 |
| C0552 | — | ✓ | — | — | — | ✓ | — | ✓ | — | — | — | 94,958 | 95,223 | 95,223 |
| C0553 | — | ✓ | — | — | — | ✓ | — | ✓ | — | — | ✓ | 94,958 | — | 95,223 |
| C0554 | — | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | — | 95,392 | — | 95,738 |
| C0555 | — | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 95,392 | — | 95,738 |
| C0556 | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | — | 94,997 | — | 95,546 |
| C0557 | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 94,997 | — | 95,546 |
| C0558 | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 95,440 | — | 95,763 |
| C0559 | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,440 | — | 95,763 |
| C0560 | — | ✓ | — | — | — | ✓ | ✓ | — | — | — | — | 91,539 | 94,474 | 94,474 |
| C0561 | — | ✓ | — | — | — | ✓ | ✓ | — | — | — | ✓ | 91,539 | — | 94,474 |
| C0562 | — | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | — | 92,477 | — | 94,445 |
| C0563 | — | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 92,477 | — | 94,445 |
| C0564 | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | — | 91,449 | — | 94,740 |
| C0565 | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 91,449 | — | 94,740 |
| C0566 | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 92,436 | — | 94,769 |
| C0567 | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 92,436 | — | 94,769 |
| C0568 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | — | 94,864 | 95,229 | 95,229 |
| C0569 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 94,864 | — | 95,229 |
| C0570 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 95,206 | — | 95,509 |
| C0571 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,206 | — | 95,509 |
| C0572 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 94,902 | — | 95,520 |
| C0573 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,902 | — | 95,520 |
| C0574 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,252 | — | 95,786 |
| C0575 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 95,252 | — | 95,786 |
| C0576 | — | ✓ | — | — | ✓ | — | — | — | — | — | — | 91,093 | 94,467 | 94,467 |
| C0577 | — | ✓ | — | — | ✓ | — | — | — | — | — | ✓ | 91,093 | — | 94,467 |
| C0578 | — | ✓ | — | — | ✓ | — | — | — | — | ✓ | — | 92,315 | — | 94,522 |
| C0579 | — | ✓ | — | — | ✓ | — | — | — | — | ✓ | ✓ | 92,315 | — | 94,522 |
| C0580 | — | ✓ | — | — | ✓ | — | — | — | ✓ | — | — | 90,995 | — | 94,780 |
| C0581 | — | ✓ | — | — | ✓ | — | — | — | ✓ | — | ✓ | 90,995 | — | 94,780 |
| C0582 | — | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | — | 92,272 | — | 94,715 |
| C0583 | — | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 92,272 | — | 94,715 |
| C0584 | — | ✓ | — | — | ✓ | — | — | ✓ | — | — | — | 94,708 | 95,234 | 95,234 |
| C0585 | — | ✓ | — | — | ✓ | — | — | ✓ | — | — | ✓ | 94,708 | — | 95,234 |
| C0586 | — | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | — | 95,151 | — | 95,764 |
| C0587 | — | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 95,151 | — | 95,764 |
| C0588 | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | — | 94,727 | — | 95,542 |
| C0589 | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 94,727 | — | 95,542 |
| C0590 | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 95,189 | — | 95,796 |
| C0591 | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 95,189 | — | 95,796 |
| C0592 | — | ✓ | — | — | ✓ | — | ✓ | — | — | — | — | 90,757 | 94,455 | 94,455 |
| C0593 | — | ✓ | — | — | ✓ | — | ✓ | — | — | — | ✓ | 90,757 | — | 94,455 |
| C0594 | — | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | — | 92,052 | — | 94,428 |
| C0595 | — | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 92,052 | — | 94,428 |
| C0596 | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | — | 90,648 | — | 94,742 |
| C0597 | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 90,648 | — | 94,742 |
| C0598 | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 91,992 | — | 94,675 |
| C0599 | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 91,992 | — | 94,675 |
| C0600 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | — | 94,614 | 95,202 | 95,202 |
| C0601 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 94,614 | — | 95,202 |
| C0602 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 95,055 | — | 95,630 |
| C0603 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 95,055 | — | 95,630 |
| C0604 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 94,595 | — | 95,485 |
| C0605 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 94,595 | — | 95,485 |
| C0606 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 95,054 | — | 95,754 |
| C0607 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 95,054 | — | 95,754 |
| C0608 | — | ✓ | — | — | ✓ | ✓ | — | — | — | — | — | 91,093 | 94,467 | 94,467 |
| C0609 | — | ✓ | — | — | ✓ | ✓ | — | — | — | — | ✓ | 91,093 | — | 94,467 |
| C0610 | — | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | — | 92,315 | — | 94,522 |
| C0611 | — | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 92,315 | — | 94,522 |
| C0612 | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | — | 90,995 | — | 94,780 |
| C0613 | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 90,995 | — | 94,780 |
| C0614 | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 92,272 | — | 94,715 |
| C0615 | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 92,272 | — | 94,715 |
| C0616 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | — | 94,708 | 95,234 | 95,234 |
| C0617 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 94,708 | — | 95,234 |
| C0618 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 95,156 | — | 95,776 |
| C0619 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 95,156 | — | 95,776 |
| C0620 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 94,727 | — | 95,542 |
| C0621 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 94,727 | — | 95,542 |
| C0622 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 95,193 | — | 95,822 |
| C0623 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,193 | — | 95,822 |
| C0624 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | — | 90,757 | 94,455 | 94,455 |
| C0625 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 90,757 | — | 94,455 |
| C0626 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 92,052 | — | 94,428 |
| C0627 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 92,052 | — | 94,428 |
| C0628 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 90,648 | — | 94,742 |
| C0629 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 90,648 | — | 94,742 |
| C0630 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 91,992 | — | 94,675 |
| C0631 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,992 | — | 94,675 |
| C0632 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 94,614 | 95,202 | 95,202 |
| C0633 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 94,614 | — | 95,202 |
| C0634 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 95,058 | — | 95,516 |
| C0635 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,058 | — | 95,516 |
| C0636 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 94,595 | — | 95,485 |
| C0637 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,595 | — | 95,485 |
| C0638 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,057 | — | 95,805 |
| C0639 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 95,057 | — | 95,805 |
| C0640 | — | ✓ | — | ✓ | — | — | — | — | — | — | — | 91,157 | 94,591 | 94,591 |
| C0641 | — | ✓ | — | ✓ | — | — | — | — | — | — | ✓ | 91,157 | — | 94,591 |
| C0642 | — | ✓ | — | ✓ | — | — | — | — | — | ✓ | — | 92,256 | — | 94,562 |
| C0643 | — | ✓ | — | ✓ | — | — | — | — | — | ✓ | ✓ | 92,256 | — | 94,562 |
| C0644 | — | ✓ | — | ✓ | — | — | — | — | ✓ | — | — | 91,037 | — | 94,831 |
| C0645 | — | ✓ | — | ✓ | — | — | — | — | ✓ | — | ✓ | 91,037 | — | 94,831 |
| C0646 | — | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | — | 92,200 | — | 94,728 |
| C0647 | — | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 92,200 | — | 94,728 |
| C0648 | — | ✓ | — | ✓ | — | — | — | ✓ | — | — | — | 94,519 | 95,260 | 95,260 |
| C0649 | — | ✓ | — | ✓ | — | — | — | ✓ | — | — | ✓ | 94,519 | — | 95,260 |
| C0650 | — | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | — | 95,078 | — | 95,567 |
| C0651 | — | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 95,078 | — | 95,567 |
| C0652 | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | — | 94,484 | — | 95,505 |
| C0653 | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 94,484 | — | 95,505 |
| C0654 | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 95,074 | — | 95,760 |
| C0655 | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 95,074 | — | 95,760 |
| C0656 | — | ✓ | — | ✓ | — | — | ✓ | — | — | — | — | 90,941 | 94,494 | 94,494 |
| C0657 | — | ✓ | — | ✓ | — | — | ✓ | — | — | — | ✓ | 90,941 | — | 94,494 |
| C0658 | — | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | — | 91,873 | — | 94,445 |
| C0659 | — | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 91,873 | — | 94,445 |
| C0660 | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | — | 90,812 | — | 94,777 |
| C0661 | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 90,812 | — | 94,777 |
| C0662 | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 91,802 | — | 94,766 |
| C0663 | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 91,802 | — | 94,766 |
| C0664 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | — | 94,378 | 95,269 | 95,269 |
| C0665 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 94,378 | — | 95,269 |
| C0666 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 94,794 | — | 95,687 |
| C0667 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 94,794 | — | 95,687 |
| C0668 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 94,358 | — | 95,589 |
| C0669 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 94,358 | — | 95,589 |
| C0670 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 94,783 | — | 95,772 |
| C0671 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,783 | — | 95,772 |
| C0672 | — | ✓ | — | ✓ | — | ✓ | — | — | — | — | — | 91,157 | 94,591 | 94,591 |
| C0673 | — | ✓ | — | ✓ | — | ✓ | — | — | — | — | ✓ | 91,157 | — | 94,591 |
| C0674 | — | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | — | 92,256 | — | 94,562 |
| C0675 | — | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 92,256 | — | 94,562 |
| C0676 | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | — | 91,037 | — | 94,831 |
| C0677 | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 91,037 | — | 94,831 |
| C0678 | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 92,200 | — | 94,728 |
| C0679 | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 92,200 | — | 94,728 |
| C0680 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | — | 94,519 | 95,260 | 95,260 |
| C0681 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 94,519 | — | 95,260 |
| C0682 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 95,084 | — | 95,619 |
| C0683 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 95,084 | — | 95,619 |
| C0684 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 94,484 | — | 95,505 |
| C0685 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 94,484 | — | 95,505 |
| C0686 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 95,082 | — | 95,776 |
| C0687 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,082 | — | 95,776 |
| C0688 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | — | 90,941 | 94,494 | 94,494 |
| C0689 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 90,941 | — | 94,494 |
| C0690 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 91,873 | — | 94,445 |
| C0691 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,873 | — | 94,445 |
| C0692 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 90,812 | — | 94,777 |
| C0693 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 90,812 | — | 94,777 |
| C0694 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 91,802 | — | 94,766 |
| C0695 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,802 | — | 94,766 |
| C0696 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 94,378 | 95,269 | 95,269 |
| C0697 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 94,378 | — | 95,269 |
| C0698 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 94,796 | — | 95,716 |
| C0699 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 94,796 | — | 95,716 |
| C0700 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 94,358 | — | 95,589 |
| C0701 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,358 | — | 95,589 |
| C0702 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 94,785 | — | 95,787 |
| C0703 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 94,785 | — | 95,787 |
| C0704 | — | ✓ | — | ✓ | ✓ | — | — | — | — | — | — | 90,403 | 94,549 | 94,549 |
| C0705 | — | ✓ | — | ✓ | ✓ | — | — | — | — | — | ✓ | 90,403 | — | 94,549 |
| C0706 | — | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | — | 91,613 | — | 94,521 |
| C0707 | — | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 91,613 | — | 94,521 |
| C0708 | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | — | 90,247 | — | 94,788 |
| C0709 | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 90,247 | — | 94,788 |
| C0710 | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 91,541 | — | 94,742 |
| C0711 | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 91,541 | — | 94,742 |
| C0712 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | — | 94,184 | 95,130 | 95,130 |
| C0713 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 94,184 | — | 95,130 |
| C0714 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 94,734 | — | 95,648 |
| C0715 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 94,734 | — | 95,648 |
| C0716 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 94,127 | — | 95,483 |
| C0717 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 94,127 | — | 95,483 |
| C0718 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 94,712 | — | 95,734 |
| C0719 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 94,712 | — | 95,734 |
| C0720 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | — | 90,095 | 94,474 | 94,474 |
| C0721 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 90,095 | — | 94,474 |
| C0722 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 91,368 | — | 94,467 |
| C0723 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 91,368 | — | 94,467 |
| C0724 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 89,964 | — | 94,739 |
| C0725 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 89,964 | — | 94,739 |
| C0726 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 91,300 | — | 94,743 |
| C0727 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 91,300 | — | 94,743 |
| C0728 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 94,006 | 95,236 | 95,236 |
| C0729 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 94,006 | — | 95,236 |
| C0730 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 94,586 | — | 95,597 |
| C0731 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 94,586 | — | 95,597 |
| C0732 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 93,962 | — | 95,612 |
| C0733 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 93,962 | — | 95,612 |
| C0734 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 94,551 | — | 95,671 |
| C0735 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,551 | — | 95,671 |
| C0736 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | — | 90,403 | 94,549 | 94,549 |
| C0737 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 90,403 | — | 94,549 |
| C0738 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 91,613 | — | 94,521 |
| C0739 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 91,613 | — | 94,521 |
| C0740 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 90,247 | — | 94,788 |
| C0741 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 90,247 | — | 94,788 |
| C0742 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 91,541 | — | 94,742 |
| C0743 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 91,541 | — | 94,742 |
| C0744 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 94,184 | 95,130 | 95,130 |
| C0745 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 94,184 | — | 95,130 |
| C0746 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 94,742 | — | 95,660 |
| C0747 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 94,742 | — | 95,660 |
| C0748 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 94,127 | — | 95,483 |
| C0749 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 94,127 | — | 95,483 |
| C0750 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 94,719 | — | 95,773 |
| C0751 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 94,719 | — | 95,773 |
| C0752 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 90,095 | 94,474 | 94,474 |
| C0753 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 90,095 | — | 94,474 |
| C0754 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 91,368 | — | 94,467 |
| C0755 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 91,368 | — | 94,467 |
| C0756 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 89,964 | — | 94,739 |
| C0757 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 89,964 | — | 94,739 |
| C0758 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 91,300 | — | 94,743 |
| C0759 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,300 | — | 94,743 |
| C0760 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 94,006 | 95,236 | 95,236 |
| C0761 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 94,006 | — | 95,236 |
| C0762 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 94,593 | — | 95,666 |
| C0763 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 94,593 | — | 95,666 |
| C0764 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 93,962 | — | 95,612 |
| C0765 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 93,962 | — | 95,612 |
| C0766 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 94,558 | — | 95,763 |
| C0767 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 94,558 | — | 95,763 |
| C0768 | — | ✓ | ✓ | — | — | — | — | — | — | — | — | 91,097 | 94,627 | 94,627 |
| C0769 | — | ✓ | ✓ | — | — | — | — | — | — | — | ✓ | 90,560 | — | 94,637 |
| C0770 | — | ✓ | ✓ | — | — | — | — | — | — | ✓ | — | 92,656 | — | 94,691 |
| C0771 | — | ✓ | ✓ | — | — | — | — | — | — | ✓ | ✓ | 91,949 | — | 94,660 |
| C0772 | — | ✓ | ✓ | — | — | — | — | — | ✓ | — | — | 91,025 | — | 94,921 |
| C0773 | — | ✓ | ✓ | — | — | — | — | — | ✓ | — | ✓ | 90,492 | — | 94,943 |
| C0774 | — | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | — | 92,613 | — | 94,880 |
| C0775 | — | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | 91,895 | — | 94,912 |
| C0776 | — | ✓ | ✓ | — | — | — | — | ✓ | — | — | — | 94,871 | 95,423 | 95,423 |
| C0777 | — | ✓ | ✓ | — | — | — | — | ✓ | — | — | ✓ | 94,588 | — | 95,422 |
| C0778 | — | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | — | 95,511 | — | 95,857 |
| C0779 | — | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | 95,089 | — | 95,873 |
| C0780 | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | — | 94,886 | — | 95,689 |
| C0781 | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | 94,614 | — | 95,679 |
| C0782 | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | 95,530 | — | 95,981 |
| C0783 | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 95,124 | — | 95,945 |
| C0784 | — | ✓ | ✓ | — | — | — | ✓ | — | — | — | — | 90,939 | 94,665 | 94,665 |
| C0785 | — | ✓ | ✓ | — | — | — | ✓ | — | — | — | ✓ | 90,208 | — | 94,644 |
| C0786 | — | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | — | 92,292 | — | 94,707 |
| C0787 | — | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | 91,712 | — | 94,674 |
| C0788 | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | — | 90,843 | — | 94,935 |
| C0789 | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | 90,119 | — | 94,913 |
| C0790 | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | 92,263 | — | 94,970 |
| C0791 | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 91,680 | — | 94,871 |
| C0792 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | — | 94,792 | 95,450 | 95,450 |
| C0793 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | 94,406 | — | 95,423 |
| C0794 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | 95,296 | — | 95,708 |
| C0795 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 94,942 | — | 95,761 |
| C0796 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | 94,804 | — | 95,764 |
| C0797 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 94,438 | — | 95,642 |
| C0798 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 95,331 | — | 95,966 |
| C0799 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,995 | — | 95,978 |
| C0800 | — | ✓ | ✓ | — | — | ✓ | — | — | — | — | — | 91,097 | 94,627 | 94,627 |
| C0801 | — | ✓ | ✓ | — | — | ✓ | — | — | — | — | ✓ | 90,560 | — | 94,637 |
| C0802 | — | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | — | 92,648 | — | 94,691 |
| C0803 | — | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | 91,948 | — | 94,656 |
| C0804 | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | — | 91,025 | — | 94,921 |
| C0805 | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | 90,492 | — | 94,943 |
| C0806 | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | 92,605 | — | 94,889 |
| C0807 | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 91,894 | — | 94,902 |
| C0808 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | — | 94,871 | 95,423 | 95,423 |
| C0809 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | 94,588 | — | 95,422 |
| C0810 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | 95,504 | — | 95,892 |
| C0811 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 95,095 | — | 95,874 |
| C0812 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | 94,886 | — | 95,689 |
| C0813 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 94,614 | — | 95,679 |
| C0814 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 95,522 | — | 96,006 |
| C0815 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,126 | — | 95,962 |
| C0816 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | — | 90,939 | 94,665 | 94,665 |
| C0817 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | 90,208 | — | 94,644 |
| C0818 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | 92,282 | — | 94,701 |
| C0819 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,692 | — | 94,671 |
| C0820 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | 90,843 | — | 94,935 |
| C0821 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 90,119 | — | 94,913 |
| C0822 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 92,254 | — | 94,947 |
| C0823 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,660 | — | 94,804 |
| C0824 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | 94,792 | 95,450 | 95,450 |
| C0825 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 94,406 | — | 95,423 |
| C0826 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 95,292 | — | 95,975 |
| C0827 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 94,932 | — | 95,765 |
| C0828 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 94,804 | — | 95,764 |
| C0829 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,438 | — | 95,642 |
| C0830 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,319 | — | 96,009 |
| C0831 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 94,981 | — | 96,015 |
| C0832 | — | ✓ | ✓ | — | ✓ | — | — | — | — | — | — | 90,727 | 94,621 | 94,621 |
| C0833 | — | ✓ | ✓ | — | ✓ | — | — | — | — | — | ✓ | 89,945 | — | 94,584 |
| C0834 | — | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | — | 92,295 | — | 94,643 |
| C0835 | — | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | 91,528 | — | 94,592 |
| C0836 | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | — | 90,658 | — | 94,894 |
| C0837 | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | 89,850 | — | 94,889 |
| C0838 | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | 92,230 | — | 94,823 |
| C0839 | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 91,460 | — | 94,816 |
| C0840 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | — | 94,696 | 95,362 | 95,362 |
| C0841 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | 94,268 | — | 95,299 |
| C0842 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | 95,292 | — | 95,757 |
| C0843 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 94,824 | — | 95,847 |
| C0844 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | 94,731 | — | 95,663 |
| C0845 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 94,286 | — | 95,566 |
| C0846 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 95,328 | — | 95,931 |
| C0847 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 94,851 | — | 95,913 |
| C0848 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | — | 90,528 | 94,646 | 94,646 |
| C0849 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | 89,731 | — | 94,593 |
| C0850 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | 92,022 | — | 94,654 |
| C0851 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 91,353 | — | 94,595 |
| C0852 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | 90,423 | — | 94,925 |
| C0853 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 89,646 | — | 94,901 |
| C0854 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 91,967 | — | 94,839 |
| C0855 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 91,285 | — | 94,830 |
| C0856 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | 94,614 | 95,348 | 95,348 |
| C0857 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 94,164 | — | 95,348 |
| C0858 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 95,164 | — | 95,906 |
| C0859 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 94,743 | — | 95,694 |
| C0860 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 94,638 | — | 95,678 |
| C0861 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 94,156 | — | 95,696 |
| C0862 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 95,203 | — | 95,889 |
| C0863 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,723 | — | 95,892 |
| C0864 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | — | 90,727 | 94,621 | 94,621 |
| C0865 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | 89,945 | — | 94,584 |
| C0866 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | 92,283 | — | 94,655 |
| C0867 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 91,528 | — | 94,596 |
| C0868 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | 90,658 | — | 94,894 |
| C0869 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 89,850 | — | 94,889 |
| C0870 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 92,218 | — | 94,819 |
| C0871 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 91,460 | — | 94,816 |
| C0872 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | 94,696 | 95,362 | 95,362 |
| C0873 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 94,268 | — | 95,299 |
| C0874 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 95,287 | — | 95,752 |
| C0875 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 94,824 | — | 95,906 |
| C0876 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 94,731 | — | 95,663 |
| C0877 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 94,286 | — | 95,566 |
| C0878 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 95,317 | — | 95,939 |
| C0879 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 94,850 | — | 95,928 |
| C0880 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | 90,528 | 94,646 | 94,646 |
| C0881 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 89,731 | — | 94,593 |
| C0882 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 92,015 | — | 94,655 |
| C0883 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 91,353 | — | 94,595 |
| C0884 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 90,423 | — | 94,925 |
| C0885 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 89,646 | — | 94,901 |
| C0886 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 91,961 | — | 94,842 |
| C0887 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,285 | — | 94,785 |
| C0888 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 94,614 | 95,348 | 95,348 |
| C0889 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 94,164 | — | 95,348 |
| C0890 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 95,156 | — | 95,915 |
| C0891 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 94,754 | — | 95,688 |
| C0892 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 94,638 | — | 95,678 |
| C0893 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,156 | — | 95,696 |
| C0894 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,188 | — | 95,937 |
| C0895 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 94,733 | — | 95,925 |
| C0896 | — | ✓ | ✓ | ✓ | — | — | — | — | — | — | — | 90,366 | 94,705 | 94,705 |
| C0897 | — | ✓ | ✓ | ✓ | — | — | — | — | — | — | ✓ | 89,745 | — | 94,661 |
| C0898 | — | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | — | 91,757 | — | 94,708 |
| C0899 | — | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | 91,123 | — | 94,665 |
| C0900 | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | — | 90,215 | — | 94,946 |
| C0901 | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | 89,585 | — | 94,965 |
| C0902 | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | 91,676 | — | 94,890 |
| C0903 | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 91,040 | — | 94,912 |
| C0904 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | — | 94,324 | 95,502 | 95,502 |
| C0905 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | 93,851 | — | 95,479 |
| C0906 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | 95,004 | — | 95,836 |
| C0907 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 94,495 | — | 95,850 |
| C0908 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | 94,272 | — | 95,721 |
| C0909 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 93,787 | — | 95,805 |
| C0910 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 94,989 | — | 95,987 |
| C0911 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 94,473 | — | 95,944 |
| C0912 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | — | 90,297 | 94,708 | 94,708 |
| C0913 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | 89,506 | — | 94,684 |
| C0914 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | 91,642 | — | 94,682 |
| C0915 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 91,042 | — | 94,659 |
| C0916 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | 90,145 | — | 94,957 |
| C0917 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 89,342 | — | 94,927 |
| C0918 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 91,547 | — | 94,841 |
| C0919 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 90,943 | — | 94,899 |
| C0920 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | 94,288 | 95,505 | 95,505 |
| C0921 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 93,727 | — | 95,520 |
| C0922 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 94,893 | — | 95,929 |
| C0923 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 94,421 | — | 95,696 |
| C0924 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 94,241 | — | 95,915 |
| C0925 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 93,667 | — | 95,754 |
| C0926 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 94,855 | — | 96,064 |
| C0927 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,378 | — | 95,973 |
| C0928 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | — | 90,366 | 94,705 | 94,705 |
| C0929 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | 89,745 | — | 94,661 |
| C0930 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | 91,755 | — | 94,704 |
| C0931 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 91,123 | — | 94,697 |
| C0932 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | 90,215 | — | 94,946 |
| C0933 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 89,585 | — | 94,965 |
| C0934 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 91,674 | — | 94,888 |
| C0935 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 91,040 | — | 94,886 |
| C0936 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | 94,324 | 95,502 | 95,502 |
| C0937 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 93,851 | — | 95,479 |
| C0938 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 95,004 | — | 95,850 |
| C0939 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 94,495 | — | 95,827 |
| C0940 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 94,272 | — | 95,721 |
| C0941 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 93,787 | — | 95,805 |
| C0942 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 94,990 | — | 95,961 |
| C0943 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 94,474 | — | 95,961 |
| C0944 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | 90,297 | 94,708 | 94,708 |
| C0945 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 89,506 | — | 94,684 |
| C0946 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 91,650 | — | 94,681 |
| C0947 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,042 | — | 94,636 |
| C0948 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 90,145 | — | 94,957 |
| C0949 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 89,342 | — | 94,927 |
| C0950 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 91,547 | — | 94,827 |
| C0951 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 90,943 | — | 94,930 |
| C0952 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 94,288 | 95,505 | 95,505 |
| C0953 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 93,727 | — | 95,520 |
| C0954 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 94,896 | — | 95,733 |
| C0955 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 94,427 | — | 95,713 |
| C0956 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 94,241 | — | 95,915 |
| C0957 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 93,667 | — | 95,754 |
| C0958 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 94,850 | — | 95,897 |
| C0959 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 94,382 | — | 95,986 |
| C0960 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | — | 89,891 | 94,657 | 94,657 |
| C0961 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | 89,092 | — | 94,644 |
| C0962 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | 91,392 | — | 94,658 |
| C0963 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 90,635 | — | 94,592 |
| C0964 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | 89,707 | — | 94,937 |
| C0965 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 88,913 | — | 94,914 |
| C0966 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 91,295 | — | 94,920 |
| C0967 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 90,535 | — | 94,816 |
| C0968 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | 94,044 | 95,408 | 95,408 |
| C0969 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 93,507 | — | 95,306 |
| C0970 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 94,731 | — | 95,718 |
| C0971 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 94,188 | — | 95,825 |
| C0972 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 93,966 | — | 95,723 |
| C0973 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 93,417 | — | 95,735 |
| C0974 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 94,702 | — | 95,881 |
| C0975 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 94,139 | — | 95,871 |
| C0976 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | 89,799 | 94,658 | 94,658 |
| C0977 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 88,984 | — | 94,619 |
| C0978 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 91,351 | — | 94,658 |
| C0979 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 90,577 | — | 94,638 |
| C0980 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 89,631 | — | 94,927 |
| C0981 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 88,848 | — | 94,925 |
| C0982 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 91,255 | — | 94,893 |
| C0983 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 90,484 | — | 94,839 |
| C0984 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 93,989 | 95,413 | 95,413 |
| C0985 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 93,372 | — | 95,540 |
| C0986 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 94,698 | — | 95,881 |
| C0987 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 94,135 | — | 95,859 |
| C0988 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 93,920 | — | 95,722 |
| C0989 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 93,316 | — | 95,773 |
| C0990 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 94,655 | — | 95,929 |
| C0991 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,073 | — | 95,937 |
| C0992 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | 89,891 | 94,657 | 94,657 |
| C0993 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 89,092 | — | 94,644 |
| C0994 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 91,392 | — | 94,654 |
| C0995 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 90,636 | — | 94,587 |
| C0996 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 89,707 | — | 94,937 |
| C0997 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 88,913 | — | 94,914 |
| C0998 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 91,295 | — | 94,819 |
| C0999 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 90,536 | — | 94,816 |
| C1000 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 94,044 | 95,408 | 95,408 |
| C1001 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 93,507 | — | 95,306 |
| C1002 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 94,729 | — | 95,804 |
| C1003 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 94,188 | — | 95,745 |
| C1004 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 93,966 | — | 95,723 |
| C1005 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 93,417 | — | 95,735 |
| C1006 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 94,699 | — | 95,917 |
| C1007 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 94,138 | — | 95,902 |
| C1008 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 89,799 | 94,658 | 94,658 |
| C1009 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 88,984 | — | 94,619 |
| C1010 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 91,322 | — | 94,654 |
| C1011 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 90,594 | — | 94,638 |
| C1012 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 89,631 | — | 94,927 |
| C1013 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 88,848 | — | 94,925 |
| C1014 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 91,226 | — | 94,860 |
| C1015 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 90,500 | — | 94,770 |
| C1016 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 93,989 | 95,413 | 95,413 |
| C1017 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 93,372 | — | 95,540 |
| C1018 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 94,681 | — | 95,892 |
| C1019 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 94,160 | — | 95,840 |
| C1020 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 93,920 | — | 95,722 |
| C1021 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 93,316 | — | 95,773 |
| C1022 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 94,637 | — | 95,953 |
| C1023 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 94,097 | — | 95,979 |
| C1024 | ✓ | — | — | — | — | — | — | — | — | — | — | 80,661 | 91,041 | 91,041 |
| C1025 | ✓ | — | — | — | — | — | — | — | — | — | ✓ | 80,661 | — | 91,041 |
| C1026 | ✓ | — | — | — | — | — | — | — | — | ✓ | — | 80,662 | — | 92,148 |
| C1027 | ✓ | — | — | — | — | — | — | — | — | ✓ | ✓ | 80,662 | — | 92,148 |
| C1028 | ✓ | — | — | — | — | — | — | — | ✓ | — | — | 80,848 | — | 91,088 |
| C1029 | ✓ | — | — | — | — | — | — | — | ✓ | — | ✓ | 80,848 | — | 91,088 |
| C1030 | ✓ | — | — | — | — | — | — | — | ✓ | ✓ | — | 80,807 | — | 92,685 |
| C1031 | ✓ | — | — | — | — | — | — | — | ✓ | ✓ | ✓ | 80,807 | — | 92,685 |
| C1032 | ✓ | — | — | — | — | — | — | ✓ | — | — | — | 90,494 | 92,518 | 92,518 |
| C1033 | ✓ | — | — | — | — | — | — | ✓ | — | — | ✓ | 90,494 | — | 92,518 |
| C1034 | ✓ | — | — | — | — | — | — | ✓ | — | ✓ | — | 90,491 | — | 93,435 |
| C1035 | ✓ | — | — | — | — | — | — | ✓ | — | ✓ | ✓ | 90,491 | — | 93,435 |
| C1036 | ✓ | — | — | — | — | — | — | ✓ | ✓ | — | — | 90,680 | — | 92,534 |
| C1037 | ✓ | — | — | — | — | — | — | ✓ | ✓ | — | ✓ | 90,680 | — | 92,534 |
| C1038 | ✓ | — | — | — | — | — | — | ✓ | ✓ | ✓ | — | 90,601 | — | 93,692 |
| C1039 | ✓ | — | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 90,601 | — | 93,692 |
| C1040 | ✓ | — | — | — | — | — | ✓ | — | — | — | — | 81,005 | 90,954 | 90,954 |
| C1041 | ✓ | — | — | — | — | — | ✓ | — | — | — | ✓ | 81,005 | — | 90,954 |
| C1042 | ✓ | — | — | — | — | — | ✓ | — | — | ✓ | — | 81,006 | — | 92,095 |
| C1043 | ✓ | — | — | — | — | — | ✓ | — | — | ✓ | ✓ | 81,006 | — | 92,095 |
| C1044 | ✓ | — | — | — | — | — | ✓ | — | ✓ | — | — | 81,175 | — | 91,049 |
| C1045 | ✓ | — | — | — | — | — | ✓ | — | ✓ | — | ✓ | 81,175 | — | 91,049 |
| C1046 | ✓ | — | — | — | — | — | ✓ | — | ✓ | ✓ | — | 81,131 | — | 92,669 |
| C1047 | ✓ | — | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 81,131 | — | 92,669 |
| C1048 | ✓ | — | — | — | — | — | ✓ | ✓ | — | — | — | 90,686 | 92,430 | 92,430 |
| C1049 | ✓ | — | — | — | — | — | ✓ | ✓ | — | — | ✓ | 90,686 | — | 92,430 |
| C1050 | ✓ | — | — | — | — | — | ✓ | ✓ | — | ✓ | — | 90,683 | — | 93,354 |
| C1051 | ✓ | — | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 90,683 | — | 93,354 |
| C1052 | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | — | — | 90,860 | — | 92,446 |
| C1053 | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 90,860 | — | 92,446 |
| C1054 | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 90,767 | — | 93,748 |
| C1055 | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 90,767 | — | 93,748 |
| C1056 | ✓ | — | — | — | — | ✓ | — | — | — | — | — | 80,866 | 90,976 | 90,976 |
| C1057 | ✓ | — | — | — | — | ✓ | — | — | — | — | ✓ | 80,866 | — | 90,976 |
| C1058 | ✓ | — | — | — | — | ✓ | — | — | — | ✓ | — | 80,873 | — | 92,185 |
| C1059 | ✓ | — | — | — | — | ✓ | — | — | — | ✓ | ✓ | 80,873 | — | 92,185 |
| C1060 | ✓ | — | — | — | — | ✓ | — | — | ✓ | — | — | 81,060 | — | 90,995 |
| C1061 | ✓ | — | — | — | — | ✓ | — | — | ✓ | — | ✓ | 81,060 | — | 90,995 |
| C1062 | ✓ | — | — | — | — | ✓ | — | — | ✓ | ✓ | — | 81,025 | — | 92,725 |
| C1063 | ✓ | — | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 81,025 | — | 92,725 |
| C1064 | ✓ | — | — | — | — | ✓ | — | ✓ | — | — | — | 90,779 | 92,471 | 92,471 |
| C1065 | ✓ | — | — | — | — | ✓ | — | ✓ | — | — | ✓ | 90,779 | — | 92,471 |
| C1066 | ✓ | — | — | — | — | ✓ | — | ✓ | — | ✓ | — | 90,800 | — | 93,541 |
| C1067 | ✓ | — | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 90,800 | — | 93,541 |
| C1068 | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | — | — | 90,967 | — | 92,333 |
| C1069 | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 90,967 | — | 92,333 |
| C1070 | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 90,910 | — | 93,835 |
| C1071 | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 90,910 | — | 93,835 |
| C1072 | ✓ | — | — | — | — | ✓ | ✓ | — | — | — | — | 81,192 | 90,903 | 90,903 |
| C1073 | ✓ | — | — | — | — | ✓ | ✓ | — | — | — | ✓ | 81,192 | — | 90,903 |
| C1074 | ✓ | — | — | — | — | ✓ | ✓ | — | — | ✓ | — | 81,199 | — | 92,121 |
| C1075 | ✓ | — | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 81,199 | — | 92,121 |
| C1076 | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | — | — | 81,364 | — | 91,005 |
| C1077 | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 81,364 | — | 91,005 |
| C1078 | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 81,328 | — | 92,702 |
| C1079 | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 81,328 | — | 92,702 |
| C1080 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | — | — | 90,919 | 92,379 | 92,379 |
| C1081 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 90,919 | — | 92,379 |
| C1082 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 90,935 | — | 93,404 |
| C1083 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 90,935 | — | 93,404 |
| C1084 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,110 | — | 92,305 |
| C1085 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,110 | — | 92,305 |
| C1086 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,034 | — | 93,874 |
| C1087 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,034 | — | 93,874 |
| C1088 | ✓ | — | — | — | ✓ | — | — | — | — | — | — | 81,358 | 91,059 | 91,059 |
| C1089 | ✓ | — | — | — | ✓ | — | — | — | — | — | ✓ | 81,358 | — | 91,059 |
| C1090 | ✓ | — | — | — | ✓ | — | — | — | — | ✓ | — | 81,363 | — | 92,333 |
| C1091 | ✓ | — | — | — | ✓ | — | — | — | — | ✓ | ✓ | 81,363 | — | 92,333 |
| C1092 | ✓ | — | — | — | ✓ | — | — | — | ✓ | — | — | 81,526 | — | 91,126 |
| C1093 | ✓ | — | — | — | ✓ | — | — | — | ✓ | — | ✓ | 81,526 | — | 91,126 |
| C1094 | ✓ | — | — | — | ✓ | — | — | — | ✓ | ✓ | — | 81,487 | — | 92,771 |
| C1095 | ✓ | — | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 81,487 | — | 92,771 |
| C1096 | ✓ | — | — | — | ✓ | — | — | ✓ | — | — | — | 90,822 | 92,535 | 92,535 |
| C1097 | ✓ | — | — | — | ✓ | — | — | ✓ | — | — | ✓ | 90,822 | — | 92,535 |
| C1098 | ✓ | — | — | — | ✓ | — | — | ✓ | — | ✓ | — | 90,840 | — | 93,596 |
| C1099 | ✓ | — | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 90,840 | — | 93,596 |
| C1100 | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | — | — | 91,017 | — | 92,572 |
| C1101 | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 91,017 | — | 92,572 |
| C1102 | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 90,945 | — | 93,826 |
| C1103 | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 90,945 | — | 93,826 |
| C1104 | ✓ | — | — | — | ✓ | — | ✓ | — | — | — | — | 81,585 | 90,981 | 90,981 |
| C1105 | ✓ | — | — | — | ✓ | — | ✓ | — | — | — | ✓ | 81,585 | — | 90,981 |
| C1106 | ✓ | — | — | — | ✓ | — | ✓ | — | — | ✓ | — | 81,587 | — | 92,257 |
| C1107 | ✓ | — | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 81,587 | — | 92,257 |
| C1108 | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | — | — | 81,793 | — | 91,052 |
| C1109 | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 81,793 | — | 91,052 |
| C1110 | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 81,742 | — | 92,828 |
| C1111 | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 81,742 | — | 92,828 |
| C1112 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | — | — | 90,957 | 92,432 | 92,432 |
| C1113 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 90,957 | — | 92,432 |
| C1114 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 90,962 | — | 93,392 |
| C1115 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 90,962 | — | 93,392 |
| C1116 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 91,176 | — | 92,476 |
| C1117 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 91,176 | — | 92,476 |
| C1118 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 91,115 | — | 93,632 |
| C1119 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,115 | — | 93,632 |
| C1120 | ✓ | — | — | — | ✓ | ✓ | — | — | — | — | — | 81,510 | 91,004 | 91,004 |
| C1121 | ✓ | — | — | — | ✓ | ✓ | — | — | — | — | ✓ | 81,510 | — | 91,004 |
| C1122 | ✓ | — | — | — | ✓ | ✓ | — | — | — | ✓ | — | 81,518 | — | 92,368 |
| C1123 | ✓ | — | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 81,518 | — | 92,368 |
| C1124 | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | — | — | 81,689 | — | 91,067 |
| C1125 | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 81,689 | — | 91,067 |
| C1126 | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 81,655 | — | 92,811 |
| C1127 | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 81,655 | — | 92,811 |
| C1128 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | — | — | 91,071 | 92,486 | 92,486 |
| C1129 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 91,071 | — | 92,486 |
| C1130 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 91,074 | — | 93,670 |
| C1131 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 91,074 | — | 93,670 |
| C1132 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 91,265 | — | 92,493 |
| C1133 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 91,265 | — | 92,493 |
| C1134 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 91,202 | — | 93,898 |
| C1135 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,202 | — | 93,898 |
| C1136 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | — | — | 81,722 | 90,908 | 90,908 |
| C1137 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 81,722 | — | 90,908 |
| C1138 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 81,731 | — | 92,231 |
| C1139 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 81,731 | — | 92,231 |
| C1140 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 81,933 | — | 90,991 |
| C1141 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 81,933 | — | 90,991 |
| C1142 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 81,892 | — | 92,862 |
| C1143 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 81,892 | — | 92,862 |
| C1144 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 91,157 | 92,391 | 92,391 |
| C1145 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 91,157 | — | 92,391 |
| C1146 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 91,162 | — | 93,467 |
| C1147 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,162 | — | 93,467 |
| C1148 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 91,367 | — | 92,400 |
| C1149 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,367 | — | 92,400 |
| C1150 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,319 | — | 93,785 |
| C1151 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,319 | — | 93,785 |
| C1152 | ✓ | — | — | ✓ | — | — | — | — | — | — | — | 81,639 | 91,781 | 91,781 |
| C1153 | ✓ | — | — | ✓ | — | — | — | — | — | — | ✓ | 81,639 | — | 91,781 |
| C1154 | ✓ | — | — | ✓ | — | — | — | — | — | ✓ | — | 81,641 | — | 92,828 |
| C1155 | ✓ | — | — | ✓ | — | — | — | — | — | ✓ | ✓ | 81,641 | — | 92,828 |
| C1156 | ✓ | — | — | ✓ | — | — | — | — | ✓ | — | — | 81,840 | — | 91,787 |
| C1157 | ✓ | — | — | ✓ | — | — | — | — | ✓ | — | ✓ | 81,840 | — | 91,787 |
| C1158 | ✓ | — | — | ✓ | — | — | — | — | ✓ | ✓ | — | 81,801 | — | 92,834 |
| C1159 | ✓ | — | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 81,801 | — | 92,834 |
| C1160 | ✓ | — | — | ✓ | — | — | — | ✓ | — | — | — | 90,971 | 93,189 | 93,189 |
| C1161 | ✓ | — | — | ✓ | — | — | — | ✓ | — | — | ✓ | 90,971 | — | 93,189 |
| C1162 | ✓ | — | — | ✓ | — | — | — | ✓ | — | ✓ | — | 90,969 | — | 93,795 |
| C1163 | ✓ | — | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 90,969 | — | 93,795 |
| C1164 | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | — | — | 91,162 | — | 93,230 |
| C1165 | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 91,162 | — | 93,230 |
| C1166 | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 91,104 | — | 93,804 |
| C1167 | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,104 | — | 93,804 |
| C1168 | ✓ | — | — | ✓ | — | — | ✓ | — | — | — | — | 81,810 | 91,756 | 91,756 |
| C1169 | ✓ | — | — | ✓ | — | — | ✓ | — | — | — | ✓ | 81,810 | — | 91,756 |
| C1170 | ✓ | — | — | ✓ | — | — | ✓ | — | — | ✓ | — | 81,814 | — | 92,695 |
| C1171 | ✓ | — | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 81,814 | — | 92,695 |
| C1172 | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | — | — | 82,004 | — | 91,756 |
| C1173 | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 82,004 | — | 91,756 |
| C1174 | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 81,969 | — | 92,685 |
| C1175 | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 81,969 | — | 92,685 |
| C1176 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | — | — | 91,066 | 93,029 | 93,029 |
| C1177 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 91,066 | — | 93,029 |
| C1178 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 91,066 | — | 93,686 |
| C1179 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,066 | — | 93,686 |
| C1180 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 91,241 | — | 93,064 |
| C1181 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,241 | — | 93,064 |
| C1182 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 91,178 | — | 93,765 |
| C1183 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,178 | — | 93,765 |
| C1184 | ✓ | — | — | ✓ | — | ✓ | — | — | — | — | — | 81,824 | 91,762 | 91,762 |
| C1185 | ✓ | — | — | ✓ | — | ✓ | — | — | — | — | ✓ | 81,824 | — | 91,762 |
| C1186 | ✓ | — | — | ✓ | — | ✓ | — | — | — | ✓ | — | 81,840 | — | 92,855 |
| C1187 | ✓ | — | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 81,840 | — | 92,855 |
| C1188 | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | — | — | 82,033 | — | 91,767 |
| C1189 | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 82,033 | — | 91,767 |
| C1190 | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 82,009 | — | 92,861 |
| C1191 | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 82,009 | — | 92,861 |
| C1192 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | — | — | 91,241 | 93,189 | 93,189 |
| C1193 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 91,241 | — | 93,189 |
| C1194 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 91,260 | — | 93,876 |
| C1195 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,260 | — | 93,876 |
| C1196 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 91,434 | — | 93,217 |
| C1197 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,434 | — | 93,217 |
| C1198 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 91,396 | — | 93,882 |
| C1199 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,396 | — | 93,882 |
| C1200 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | — | — | 81,995 | 91,897 | 91,897 |
| C1201 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 81,995 | — | 91,897 |
| C1202 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 82,006 | — | 92,693 |
| C1203 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 82,006 | — | 92,693 |
| C1204 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 82,192 | — | 91,905 |
| C1205 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 82,192 | — | 91,905 |
| C1206 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 82,165 | — | 92,709 |
| C1207 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 82,165 | — | 92,709 |
| C1208 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 91,305 | 93,027 | 93,027 |
| C1209 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,305 | — | 93,027 |
| C1210 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 91,321 | — | 93,727 |
| C1211 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,321 | — | 93,727 |
| C1212 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,500 | — | 93,061 |
| C1213 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,500 | — | 93,061 |
| C1214 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,451 | — | 93,779 |
| C1215 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,451 | — | 93,779 |
| C1216 | ✓ | — | — | ✓ | ✓ | — | — | — | — | — | — | 82,163 | 91,972 | 91,972 |
| C1217 | ✓ | — | — | ✓ | ✓ | — | — | — | — | — | ✓ | 82,163 | — | 91,972 |
| C1218 | ✓ | — | — | ✓ | ✓ | — | — | — | — | ✓ | — | 82,168 | — | 92,801 |
| C1219 | ✓ | — | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 82,168 | — | 92,801 |
| C1220 | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | — | — | 82,341 | — | 91,979 |
| C1221 | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 82,341 | — | 91,979 |
| C1222 | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 82,302 | — | 92,805 |
| C1223 | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 82,302 | — | 92,805 |
| C1224 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | — | — | 91,276 | 93,289 | 93,289 |
| C1225 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 91,276 | — | 93,289 |
| C1226 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 91,287 | — | 93,854 |
| C1227 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 91,287 | — | 93,854 |
| C1228 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 91,466 | — | 93,355 |
| C1229 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 91,466 | — | 93,355 |
| C1230 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 91,407 | — | 93,877 |
| C1231 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 91,407 | — | 93,877 |
| C1232 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | — | — | 82,327 | 91,828 | 91,828 |
| C1233 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 82,327 | — | 91,828 |
| C1234 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 82,338 | — | 92,667 |
| C1235 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 82,338 | — | 92,667 |
| C1236 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 82,508 | — | 91,836 |
| C1237 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 82,508 | — | 91,836 |
| C1238 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 82,480 | — | 92,776 |
| C1239 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 82,480 | — | 92,776 |
| C1240 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 91,368 | 93,023 | 93,023 |
| C1241 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 91,368 | — | 93,023 |
| C1242 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 91,379 | — | 93,633 |
| C1243 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 91,379 | — | 93,633 |
| C1244 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 91,568 | — | 93,033 |
| C1245 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 91,568 | — | 93,033 |
| C1246 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 91,514 | — | 93,670 |
| C1247 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,514 | — | 93,670 |
| C1248 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | — | — | 82,307 | 91,958 | 91,958 |
| C1249 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 82,307 | — | 91,958 |
| C1250 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 82,312 | — | 92,822 |
| C1251 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 82,312 | — | 92,822 |
| C1252 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 82,497 | — | 91,961 |
| C1253 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 82,497 | — | 91,961 |
| C1254 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 82,461 | — | 92,823 |
| C1255 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 82,461 | — | 92,823 |
| C1256 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 91,513 | 93,252 | 93,252 |
| C1257 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 91,513 | — | 93,252 |
| C1258 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 91,503 | — | 93,922 |
| C1259 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 91,503 | — | 93,922 |
| C1260 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 91,702 | — | 93,315 |
| C1261 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 91,702 | — | 93,315 |
| C1262 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 91,649 | — | 93,971 |
| C1263 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,649 | — | 93,971 |
| C1264 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 82,455 | 91,832 | 91,832 |
| C1265 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 82,455 | — | 91,832 |
| C1266 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 82,468 | — | 92,701 |
| C1267 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 82,468 | — | 92,701 |
| C1268 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 82,639 | — | 91,841 |
| C1269 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 82,639 | — | 91,841 |
| C1270 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 82,616 | — | 92,750 |
| C1271 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 82,616 | — | 92,750 |
| C1272 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 91,555 | 92,960 | 92,960 |
| C1273 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 91,555 | — | 92,960 |
| C1274 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 91,559 | — | 93,577 |
| C1275 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,559 | — | 93,577 |
| C1276 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 91,748 | — | 92,982 |
| C1277 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,748 | — | 92,982 |
| C1278 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,697 | — | 93,762 |
| C1279 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,697 | — | 93,762 |
| C1280 | ✓ | — | ✓ | — | — | — | — | — | — | — | — | 80,970 | 91,129 | 91,129 |
| C1281 | ✓ | — | ✓ | — | — | — | — | — | — | — | ✓ | 81,763 | — | 91,129 |
| C1282 | ✓ | — | ✓ | — | — | — | — | — | — | ✓ | — | 80,974 | — | 92,534 |
| C1283 | ✓ | — | ✓ | — | — | — | — | — | — | ✓ | ✓ | 81,769 | — | 92,540 |
| C1284 | ✓ | — | ✓ | — | — | — | — | — | ✓ | — | — | 81,187 | — | 91,219 |
| C1285 | ✓ | — | ✓ | — | — | — | — | — | ✓ | — | ✓ | 81,911 | — | 91,219 |
| C1286 | ✓ | — | ✓ | — | — | — | — | — | ✓ | ✓ | — | 81,166 | — | 92,937 |
| C1287 | ✓ | — | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | 81,888 | — | 92,949 |
| C1288 | ✓ | — | ✓ | — | — | — | — | ✓ | — | — | — | 90,779 | 92,587 | 92,587 |
| C1289 | ✓ | — | ✓ | — | — | — | — | ✓ | — | — | ✓ | 91,261 | — | 92,587 |
| C1290 | ✓ | — | ✓ | — | — | — | — | ✓ | — | ✓ | — | 90,789 | — | 93,699 |
| C1291 | ✓ | — | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | 91,279 | — | 93,699 |
| C1292 | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | — | — | 91,013 | — | 92,702 |
| C1293 | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | 91,425 | — | 92,707 |
| C1294 | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | 90,967 | — | 93,972 |
| C1295 | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,385 | — | 94,043 |
| C1296 | ✓ | — | ✓ | — | — | — | ✓ | — | — | — | — | 81,134 | 91,120 | 91,120 |
| C1297 | ✓ | — | ✓ | — | — | — | ✓ | — | — | — | ✓ | 81,940 | — | 91,120 |
| C1298 | ✓ | — | ✓ | — | — | — | ✓ | — | — | ✓ | — | 81,135 | — | 92,503 |
| C1299 | ✓ | — | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | 81,942 | — | 92,503 |
| C1300 | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | — | — | 81,360 | — | 91,353 |
| C1301 | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | 82,096 | — | 91,352 |
| C1302 | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | 81,338 | — | 92,752 |
| C1303 | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 82,071 | — | 92,767 |
| C1304 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | — | — | 90,871 | 92,522 | 92,522 |
| C1305 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | 91,328 | — | 92,524 |
| C1306 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | 90,871 | — | 93,629 |
| C1307 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,341 | — | 93,629 |
| C1308 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | 91,073 | — | 92,655 |
| C1309 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,493 | — | 92,655 |
| C1310 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 91,026 | — | 93,930 |
| C1311 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,448 | — | 94,012 |
| C1312 | ✓ | — | ✓ | — | — | ✓ | — | — | — | — | — | 81,199 | 91,092 | 91,092 |
| C1313 | ✓ | — | ✓ | — | — | ✓ | — | — | — | — | ✓ | 81,962 | — | 91,092 |
| C1314 | ✓ | — | ✓ | — | — | ✓ | — | — | — | ✓ | — | 81,206 | — | 92,562 |
| C1315 | ✓ | — | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | 81,971 | — | 92,601 |
| C1316 | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | — | — | 81,406 | — | 91,219 |
| C1317 | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | 82,122 | — | 91,216 |
| C1318 | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | 81,382 | — | 92,948 |
| C1319 | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 82,105 | — | 92,960 |
| C1320 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | — | — | 91,072 | 92,559 | 92,559 |
| C1321 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | 91,530 | — | 92,557 |
| C1322 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | 91,087 | — | 93,832 |
| C1323 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,554 | — | 93,832 |
| C1324 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | 91,290 | — | 92,727 |
| C1325 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,697 | — | 92,727 |
| C1326 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 91,237 | — | 94,068 |
| C1327 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,674 | — | 94,182 |
| C1328 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | — | — | 81,390 | 91,140 | 91,140 |
| C1329 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | 82,118 | — | 91,045 |
| C1330 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | 81,394 | — | 92,508 |
| C1331 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 82,126 | — | 92,525 |
| C1332 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | 81,634 | — | 91,206 |
| C1333 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 82,292 | — | 91,220 |
| C1334 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 81,613 | — | 92,847 |
| C1335 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 82,274 | — | 92,850 |
| C1336 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | 91,179 | 92,482 | 92,482 |
| C1337 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,514 | — | 92,482 |
| C1338 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 91,200 | — | 93,681 |
| C1339 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,532 | — | 93,681 |
| C1340 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,401 | — | 92,639 |
| C1341 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,695 | — | 92,639 |
| C1342 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,362 | — | 94,026 |
| C1343 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,668 | — | 94,154 |
| C1344 | ✓ | — | ✓ | — | ✓ | — | — | — | — | — | — | 81,348 | 91,144 | 91,144 |
| C1345 | ✓ | — | ✓ | — | ✓ | — | — | — | — | — | ✓ | 82,235 | — | 91,144 |
| C1346 | ✓ | — | ✓ | — | ✓ | — | — | — | — | ✓ | — | 81,352 | — | 92,616 |
| C1347 | ✓ | — | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | 82,239 | — | 92,619 |
| C1348 | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | — | — | 81,570 | — | 91,286 |
| C1349 | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | 82,386 | — | 91,287 |
| C1350 | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | 81,543 | — | 92,861 |
| C1351 | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 82,352 | — | 92,959 |
| C1352 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | — | — | 90,998 | 92,613 | 92,613 |
| C1353 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | 91,447 | — | 92,613 |
| C1354 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | 91,008 | — | 93,691 |
| C1355 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 91,462 | — | 93,694 |
| C1356 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | 91,226 | — | 92,717 |
| C1357 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 91,614 | — | 92,717 |
| C1358 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 91,174 | — | 93,967 |
| C1359 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 91,583 | — | 94,074 |
| C1360 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | — | — | 81,520 | 91,137 | 91,137 |
| C1361 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | 82,351 | — | 91,137 |
| C1362 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | 81,524 | — | 92,572 |
| C1363 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 82,356 | — | 92,572 |
| C1364 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | 81,714 | — | 91,300 |
| C1365 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 82,500 | — | 91,300 |
| C1366 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 81,689 | — | 92,659 |
| C1367 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 82,466 | — | 92,822 |
| C1368 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | 91,127 | 92,518 | 92,518 |
| C1369 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 91,498 | — | 92,518 |
| C1370 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 91,137 | — | 93,627 |
| C1371 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 91,506 | — | 93,627 |
| C1372 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 91,309 | — | 92,691 |
| C1373 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 91,643 | — | 92,691 |
| C1374 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 91,261 | — | 93,872 |
| C1375 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,600 | — | 94,041 |
| C1376 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | — | — | 81,600 | 91,123 | 91,123 |
| C1377 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | 82,367 | — | 91,123 |
| C1378 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | 81,607 | — | 92,579 |
| C1379 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 82,374 | — | 92,687 |
| C1380 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | 81,806 | — | 91,244 |
| C1381 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 82,550 | — | 91,242 |
| C1382 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 81,784 | — | 92,845 |
| C1383 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 82,522 | — | 92,989 |
| C1384 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | 91,338 | 92,572 | 92,572 |
| C1385 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 91,643 | — | 92,572 |
| C1386 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 91,357 | — | 93,788 |
| C1387 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 91,656 | — | 93,788 |
| C1388 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 91,533 | — | 92,685 |
| C1389 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 91,809 | — | 92,680 |
| C1390 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 91,486 | — | 94,126 |
| C1391 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,791 | — | 94,191 |
| C1392 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | 81,776 | 91,105 | 91,105 |
| C1393 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 82,485 | — | 91,105 |
| C1394 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 81,783 | — | 92,601 |
| C1395 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 82,498 | — | 92,603 |
| C1396 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 82,004 | — | 91,248 |
| C1397 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 82,659 | — | 91,248 |
| C1398 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 81,981 | — | 92,695 |
| C1399 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 82,636 | — | 92,779 |
| C1400 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 91,446 | 92,561 | 92,561 |
| C1401 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 91,605 | — | 92,566 |
| C1402 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 91,465 | — | 93,722 |
| C1403 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,615 | — | 93,722 |
| C1404 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 91,642 | — | 92,652 |
| C1405 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,759 | — | 92,589 |
| C1406 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,586 | — | 94,034 |
| C1407 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,733 | — | 94,165 |
| C1408 | ✓ | — | ✓ | ✓ | — | — | — | — | — | — | — | 82,020 | 92,026 | 92,026 |
| C1409 | ✓ | — | ✓ | ✓ | — | — | — | — | — | — | ✓ | 82,633 | — | 92,118 |
| C1410 | ✓ | — | ✓ | ✓ | — | — | — | — | — | ✓ | — | 82,028 | — | 92,959 |
| C1411 | ✓ | — | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | 82,642 | — | 92,941 |
| C1412 | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | — | — | 82,193 | — | 92,237 |
| C1413 | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | 82,795 | — | 92,158 |
| C1414 | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | 82,166 | — | 92,995 |
| C1415 | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 82,762 | — | 92,963 |
| C1416 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | — | — | 91,354 | 93,410 | 93,410 |
| C1417 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | 91,675 | — | 93,421 |
| C1418 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | 91,365 | — | 93,951 |
| C1419 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 91,696 | — | 93,975 |
| C1420 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | 91,522 | — | 93,435 |
| C1421 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 91,824 | — | 93,451 |
| C1422 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 91,483 | — | 93,976 |
| C1423 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,780 | — | 94,014 |
| C1424 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | — | — | 82,065 | 92,091 | 92,091 |
| C1425 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | 82,719 | — | 92,091 |
| C1426 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | 82,071 | — | 92,888 |
| C1427 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 82,723 | — | 92,888 |
| C1428 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | 82,227 | — | 92,092 |
| C1429 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 82,856 | — | 92,232 |
| C1430 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 82,204 | — | 92,772 |
| C1431 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 82,825 | — | 92,803 |
| C1432 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | 91,362 | 93,310 | 93,310 |
| C1433 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 91,719 | — | 93,285 |
| C1434 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 91,366 | — | 93,890 |
| C1435 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,733 | — | 93,919 |
| C1436 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 91,506 | — | 93,310 |
| C1437 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,860 | — | 93,285 |
| C1438 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 91,473 | — | 93,973 |
| C1439 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,818 | — | 93,986 |
| C1440 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | — | — | 82,236 | 92,096 | 92,096 |
| C1441 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | 82,826 | — | 92,007 |
| C1442 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | 82,247 | — | 92,971 |
| C1443 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 82,838 | — | 92,978 |
| C1444 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | 82,407 | — | 92,108 |
| C1445 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 83,003 | — | 92,129 |
| C1446 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 82,375 | — | 92,979 |
| C1447 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 82,974 | — | 93,048 |
| C1448 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | 91,618 | 93,393 | 93,393 |
| C1449 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 91,933 | — | 93,381 |
| C1450 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 91,630 | — | 93,998 |
| C1451 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,951 | — | 94,069 |
| C1452 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 91,802 | — | 93,421 |
| C1453 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 92,097 | — | 93,451 |
| C1454 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 91,750 | — | 94,031 |
| C1455 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 92,063 | — | 94,058 |
| C1456 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | 82,313 | 91,782 | 91,782 |
| C1457 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 82,889 | — | 91,794 |
| C1458 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 82,325 | — | 92,927 |
| C1459 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 82,904 | — | 92,884 |
| C1460 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 82,464 | — | 92,178 |
| C1461 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 83,040 | — | 91,794 |
| C1462 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 82,445 | — | 93,008 |
| C1463 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 83,021 | — | 93,026 |
| C1464 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 91,666 | 93,127 | 93,127 |
| C1465 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,875 | — | 93,127 |
| C1466 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 91,686 | — | 93,954 |
| C1467 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,892 | — | 93,986 |
| C1468 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,815 | — | 93,300 |
| C1469 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 92,028 | — | 93,190 |
| C1470 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,789 | — | 94,013 |
| C1471 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 92,000 | — | 94,055 |
| C1472 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | — | — | 82,292 | 91,784 | 91,784 |
| C1473 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | 82,907 | — | 92,154 |
| C1474 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | 82,300 | — | 92,958 |
| C1475 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 82,915 | — | 93,018 |
| C1476 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | 82,465 | — | 91,788 |
| C1477 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 83,055 | — | 92,160 |
| C1478 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 82,432 | — | 92,987 |
| C1479 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 83,023 | — | 93,001 |
| C1480 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | 91,499 | 93,424 | 93,424 |
| C1481 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 91,804 | — | 93,424 |
| C1482 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 91,509 | — | 94,008 |
| C1483 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 91,821 | — | 93,975 |
| C1484 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 91,669 | — | 93,433 |
| C1485 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 91,953 | — | 93,436 |
| C1486 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 91,623 | — | 94,024 |
| C1487 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 91,918 | — | 94,050 |
| C1488 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | 82,370 | 92,030 | 92,030 |
| C1489 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 82,992 | — | 91,724 |
| C1490 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 82,380 | — | 92,807 |
| C1491 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 83,002 | — | 92,811 |
| C1492 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 82,501 | — | 92,031 |
| C1493 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 83,126 | — | 91,738 |
| C1494 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 82,477 | — | 92,823 |
| C1495 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 83,088 | — | 92,799 |
| C1496 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 91,584 | 93,304 | 93,304 |
| C1497 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 91,842 | — | 93,215 |
| C1498 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 91,596 | — | 93,846 |
| C1499 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 91,860 | — | 93,850 |
| C1500 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 91,731 | — | 93,337 |
| C1501 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 91,984 | — | 93,306 |
| C1502 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 91,686 | — | 93,909 |
| C1503 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,935 | — | 93,938 |
| C1504 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | 82,505 | 92,159 | 92,159 |
| C1505 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 83,073 | — | 91,732 |
| C1506 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 82,517 | — | 92,977 |
| C1507 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 83,082 | — | 93,046 |
| C1508 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 82,682 | — | 92,166 |
| C1509 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 83,239 | — | 92,208 |
| C1510 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 82,654 | — | 93,047 |
| C1511 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 83,212 | — | 93,057 |
| C1512 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 91,792 | 93,389 | 93,389 |
| C1513 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 92,007 | — | 93,445 |
| C1514 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 91,807 | — | 94,046 |
| C1515 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 92,010 | — | 94,024 |
| C1516 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 91,962 | — | 93,447 |
| C1517 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 92,159 | — | 93,466 |
| C1518 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 91,920 | — | 94,105 |
| C1519 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 92,130 | — | 94,139 |
| C1520 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 82,550 | 91,821 | 91,821 |
| C1521 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 83,099 | — | 91,816 |
| C1522 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 82,569 | — | 92,831 |
| C1523 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 83,112 | — | 92,816 |
| C1524 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 82,706 | — | 91,829 |
| C1525 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 83,256 | — | 91,832 |
| C1526 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 82,692 | — | 92,877 |
| C1527 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 83,224 | — | 92,862 |
| C1528 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 91,834 | 93,172 | 93,172 |
| C1529 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 91,938 | — | 93,171 |
| C1530 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 91,848 | — | 93,977 |
| C1531 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,944 | — | 94,004 |
| C1532 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 91,975 | — | 93,225 |
| C1533 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 92,083 | — | 93,233 |
| C1534 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,936 | — | 94,015 |
| C1535 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 92,039 | — | 93,942 |
| C1536 | ✓ | ✓ | — | — | — | — | — | — | — | — | — | 88,655 | 94,030 | 94,030 |
| C1537 | ✓ | ✓ | — | — | — | — | — | — | — | — | ✓ | 88,655 | — | 94,030 |
| C1538 | ✓ | ✓ | — | — | — | — | — | — | — | ✓ | — | 88,696 | — | 94,200 |
| C1539 | ✓ | ✓ | — | — | — | — | — | — | — | ✓ | ✓ | 88,696 | — | 94,200 |
| C1540 | ✓ | ✓ | — | — | — | — | — | — | ✓ | — | — | 88,644 | — | 94,301 |
| C1541 | ✓ | ✓ | — | — | — | — | — | — | ✓ | — | ✓ | 88,644 | — | 94,301 |
| C1542 | ✓ | ✓ | — | — | — | — | — | — | ✓ | ✓ | — | 88,685 | — | 94,293 |
| C1543 | ✓ | ✓ | — | — | — | — | — | — | ✓ | ✓ | ✓ | 88,685 | — | 94,293 |
| C1544 | ✓ | ✓ | — | — | — | — | — | ✓ | — | — | — | 95,592 | 95,639 | 95,639 |
| C1545 | ✓ | ✓ | — | — | — | — | — | ✓ | — | — | ✓ | 95,592 | — | 95,639 |
| C1546 | ✓ | ✓ | — | — | — | — | — | ✓ | — | ✓ | — | 95,623 | — | 95,774 |
| C1547 | ✓ | ✓ | — | — | — | — | — | ✓ | — | ✓ | ✓ | 95,623 | — | 95,774 |
| C1548 | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | — | — | 95,653 | — | 95,835 |
| C1549 | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | — | ✓ | 95,653 | — | 95,835 |
| C1550 | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | — | 95,683 | — | 95,874 |
| C1551 | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 95,683 | — | 95,874 |
| C1552 | ✓ | ✓ | — | — | — | — | ✓ | — | — | — | — | 88,490 | 93,955 | 93,955 |
| C1553 | ✓ | ✓ | — | — | — | — | ✓ | — | — | — | ✓ | 88,490 | — | 93,955 |
| C1554 | ✓ | ✓ | — | — | — | — | ✓ | — | — | ✓ | — | 88,502 | — | 94,004 |
| C1555 | ✓ | ✓ | — | — | — | — | ✓ | — | — | ✓ | ✓ | 88,502 | — | 94,004 |
| C1556 | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | — | — | 88,472 | — | 94,244 |
| C1557 | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | — | ✓ | 88,472 | — | 94,244 |
| C1558 | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | — | 88,485 | — | 94,221 |
| C1559 | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 88,485 | — | 94,221 |
| C1560 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | — | — | 95,516 | 95,578 | 95,578 |
| C1561 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | — | ✓ | 95,516 | — | 95,578 |
| C1562 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | — | 95,521 | — | 95,801 |
| C1563 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 95,521 | — | 95,801 |
| C1564 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | — | 95,575 | — | 95,705 |
| C1565 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 95,575 | — | 95,705 |
| C1566 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 95,580 | — | 95,880 |
| C1567 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 95,580 | — | 95,880 |
| C1568 | ✓ | ✓ | — | — | — | ✓ | — | — | — | — | — | 88,732 | 94,011 | 94,011 |
| C1569 | ✓ | ✓ | — | — | — | ✓ | — | — | — | — | ✓ | 88,732 | — | 94,011 |
| C1570 | ✓ | ✓ | — | — | — | ✓ | — | — | — | ✓ | — | 88,772 | — | 94,211 |
| C1571 | ✓ | ✓ | — | — | — | ✓ | — | — | — | ✓ | ✓ | 88,772 | — | 94,211 |
| C1572 | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | — | — | 88,722 | — | 94,306 |
| C1573 | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | — | ✓ | 88,722 | — | 94,306 |
| C1574 | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | — | 88,763 | — | 94,303 |
| C1575 | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 88,763 | — | 94,303 |
| C1576 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | — | — | 95,621 | 95,678 | 95,678 |
| C1577 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | — | ✓ | 95,621 | — | 95,678 |
| C1578 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | — | 95,651 | — | 95,792 |
| C1579 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 95,651 | — | 95,792 |
| C1580 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | — | 95,674 | — | 95,838 |
| C1581 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 95,674 | — | 95,838 |
| C1582 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 95,705 | — | 95,855 |
| C1583 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,705 | — | 95,855 |
| C1584 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | — | — | 88,575 | 93,948 | 93,948 |
| C1585 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | — | ✓ | 88,575 | — | 93,948 |
| C1586 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | — | 88,589 | — | 94,014 |
| C1587 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 88,589 | — | 94,014 |
| C1588 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | — | 88,554 | — | 94,275 |
| C1589 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 88,554 | — | 94,275 |
| C1590 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 88,568 | — | 94,169 |
| C1591 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 88,568 | — | 94,169 |
| C1592 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | — | 95,532 | 95,613 | 95,613 |
| C1593 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 95,532 | — | 95,613 |
| C1594 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 95,542 | — | 95,844 |
| C1595 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,542 | — | 95,844 |
| C1596 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 95,586 | — | 95,718 |
| C1597 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 95,586 | — | 95,718 |
| C1598 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,596 | — | 95,926 |
| C1599 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 95,596 | — | 95,926 |
| C1600 | ✓ | ✓ | — | — | ✓ | — | — | — | — | — | — | 88,438 | 93,969 | 93,969 |
| C1601 | ✓ | ✓ | — | — | ✓ | — | — | — | — | — | ✓ | 88,438 | — | 93,969 |
| C1602 | ✓ | ✓ | — | — | ✓ | — | — | — | — | ✓ | — | 88,438 | — | 93,994 |
| C1603 | ✓ | ✓ | — | — | ✓ | — | — | — | — | ✓ | ✓ | 88,438 | — | 93,994 |
| C1604 | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | — | — | 88,404 | — | 94,244 |
| C1605 | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | — | ✓ | 88,404 | — | 94,244 |
| C1606 | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | — | 88,404 | — | 94,212 |
| C1607 | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 88,404 | — | 94,212 |
| C1608 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | — | — | 95,478 | 95,586 | 95,586 |
| C1609 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | — | ✓ | 95,478 | — | 95,586 |
| C1610 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | — | 95,478 | — | 95,779 |
| C1611 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 95,478 | — | 95,779 |
| C1612 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | — | 95,514 | — | 95,782 |
| C1613 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 95,514 | — | 95,782 |
| C1614 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 95,514 | — | 95,867 |
| C1615 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 95,514 | — | 95,867 |
| C1616 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | — | — | 88,289 | 93,977 | 93,977 |
| C1617 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | — | ✓ | 88,289 | — | 93,977 |
| C1618 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | — | 88,290 | — | 93,972 |
| C1619 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 88,290 | — | 93,972 |
| C1620 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | — | 88,234 | — | 94,177 |
| C1621 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 88,234 | — | 94,177 |
| C1622 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 88,235 | — | 94,247 |
| C1623 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 88,235 | — | 94,247 |
| C1624 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | — | 95,409 | 95,522 | 95,522 |
| C1625 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 95,409 | — | 95,522 |
| C1626 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 95,409 | — | 95,744 |
| C1627 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 95,409 | — | 95,744 |
| C1628 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 95,418 | — | 95,619 |
| C1629 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 95,418 | — | 95,619 |
| C1630 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 95,418 | — | 95,803 |
| C1631 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 95,418 | — | 95,803 |
| C1632 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | — | — | 88,475 | 93,992 | 93,992 |
| C1633 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | — | ✓ | 88,475 | — | 93,992 |
| C1634 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | — | 88,475 | — | 93,986 |
| C1635 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 88,475 | — | 93,986 |
| C1636 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | — | 88,453 | — | 94,215 |
| C1637 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 88,453 | — | 94,215 |
| C1638 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 88,453 | — | 94,231 |
| C1639 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 88,453 | — | 94,231 |
| C1640 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | — | 95,472 | 95,588 | 95,588 |
| C1641 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 95,472 | — | 95,588 |
| C1642 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 95,472 | — | 95,798 |
| C1643 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 95,472 | — | 95,798 |
| C1644 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 95,516 | — | 95,768 |
| C1645 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 95,516 | — | 95,768 |
| C1646 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 95,516 | — | 95,849 |
| C1647 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,516 | — | 95,849 |
| C1648 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | — | 88,346 | 93,964 | 93,964 |
| C1649 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 88,346 | — | 93,964 |
| C1650 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 88,348 | — | 93,996 |
| C1651 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 88,348 | — | 93,996 |
| C1652 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 88,294 | — | 94,227 |
| C1653 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 88,294 | — | 94,227 |
| C1654 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 88,297 | — | 94,250 |
| C1655 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 88,297 | — | 94,250 |
| C1656 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 95,418 | 95,584 | 95,584 |
| C1657 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 95,418 | — | 95,584 |
| C1658 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 95,418 | — | 95,791 |
| C1659 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,418 | — | 95,791 |
| C1660 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 95,425 | — | 95,797 |
| C1661 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 95,425 | — | 95,797 |
| C1662 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,425 | — | 95,910 |
| C1663 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 95,425 | — | 95,910 |
| C1664 | ✓ | ✓ | — | ✓ | — | — | — | — | — | — | — | 88,155 | 94,025 | 94,025 |
| C1665 | ✓ | ✓ | — | ✓ | — | — | — | — | — | — | ✓ | 88,155 | — | 94,025 |
| C1666 | ✓ | ✓ | — | ✓ | — | — | — | — | — | ✓ | — | 88,205 | — | 94,053 |
| C1667 | ✓ | ✓ | — | ✓ | — | — | — | — | — | ✓ | ✓ | 88,205 | — | 94,053 |
| C1668 | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | — | — | 88,107 | — | 94,295 |
| C1669 | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | — | ✓ | 88,107 | — | 94,295 |
| C1670 | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | — | 88,158 | — | 94,159 |
| C1671 | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 88,158 | — | 94,159 |
| C1672 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | — | — | 95,317 | 95,671 | 95,671 |
| C1673 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | — | ✓ | 95,317 | — | 95,671 |
| C1674 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | — | 95,355 | — | 95,646 |
| C1675 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 95,355 | — | 95,646 |
| C1676 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | — | 95,315 | — | 95,824 |
| C1677 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 95,315 | — | 95,824 |
| C1678 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 95,353 | — | 95,825 |
| C1679 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 95,353 | — | 95,825 |
| C1680 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | — | — | 87,936 | 94,011 | 94,011 |
| C1681 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | — | ✓ | 87,936 | — | 94,011 |
| C1682 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | — | 87,949 | — | 94,004 |
| C1683 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 87,949 | — | 94,004 |
| C1684 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | — | 87,877 | — | 94,273 |
| C1685 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 87,877 | — | 94,273 |
| C1686 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 87,890 | — | 94,181 |
| C1687 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 87,890 | — | 94,181 |
| C1688 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | — | 95,086 | 95,609 | 95,609 |
| C1689 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 95,086 | — | 95,609 |
| C1690 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 95,092 | — | 95,802 |
| C1691 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 95,092 | — | 95,802 |
| C1692 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 95,076 | — | 95,701 |
| C1693 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 95,076 | — | 95,701 |
| C1694 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 95,082 | — | 95,762 |
| C1695 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 95,082 | — | 95,762 |
| C1696 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | — | — | 88,242 | 94,010 | 94,010 |
| C1697 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | — | ✓ | 88,242 | — | 94,010 |
| C1698 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | — | 88,293 | — | 94,140 |
| C1699 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 88,293 | — | 94,140 |
| C1700 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | — | 88,199 | — | 94,335 |
| C1701 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 88,199 | — | 94,335 |
| C1702 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 88,250 | — | 94,176 |
| C1703 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 88,250 | — | 94,176 |
| C1704 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | — | 95,356 | 95,724 | 95,724 |
| C1705 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 95,356 | — | 95,724 |
| C1706 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 95,394 | — | 95,687 |
| C1707 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 95,394 | — | 95,687 |
| C1708 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 95,352 | — | 95,876 |
| C1709 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 95,352 | — | 95,876 |
| C1710 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 95,390 | — | 95,721 |
| C1711 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,390 | — | 95,721 |
| C1712 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | — | 88,034 | 94,042 | 94,042 |
| C1713 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 88,034 | — | 94,042 |
| C1714 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 88,048 | — | 94,014 |
| C1715 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 88,048 | — | 94,014 |
| C1716 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 87,975 | — | 94,226 |
| C1717 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 87,975 | — | 94,226 |
| C1718 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 87,988 | — | 94,229 |
| C1719 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 87,988 | — | 94,229 |
| C1720 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 95,118 | 95,652 | 95,652 |
| C1721 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 95,118 | — | 95,652 |
| C1722 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 95,123 | — | 95,844 |
| C1723 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,123 | — | 95,844 |
| C1724 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 95,108 | — | 95,704 |
| C1725 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 95,108 | — | 95,704 |
| C1726 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,113 | — | 95,804 |
| C1727 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 95,113 | — | 95,804 |
| C1728 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | — | — | 87,854 | 93,996 | 93,996 |
| C1729 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | — | ✓ | 87,854 | — | 93,996 |
| C1730 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | — | 87,854 | — | 94,040 |
| C1731 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 87,854 | — | 94,040 |
| C1732 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | — | 87,791 | — | 94,261 |
| C1733 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 87,791 | — | 94,261 |
| C1734 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 87,791 | — | 94,209 |
| C1735 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 87,791 | — | 94,209 |
| C1736 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | — | 95,114 | 95,652 | 95,652 |
| C1737 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 95,114 | — | 95,652 |
| C1738 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 95,114 | — | 95,778 |
| C1739 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 95,114 | — | 95,778 |
| C1740 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 95,093 | — | 95,761 |
| C1741 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 95,093 | — | 95,761 |
| C1742 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 95,093 | — | 95,757 |
| C1743 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 95,093 | — | 95,757 |
| C1744 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | — | 87,706 | 93,965 | 93,965 |
| C1745 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 87,706 | — | 93,965 |
| C1746 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 87,706 | — | 93,854 |
| C1747 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 87,706 | — | 93,854 |
| C1748 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 87,667 | — | 94,252 |
| C1749 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 87,667 | — | 94,252 |
| C1750 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 87,667 | — | 94,244 |
| C1751 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 87,667 | — | 94,244 |
| C1752 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 94,952 | 95,527 | 95,527 |
| C1753 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 94,952 | — | 95,527 |
| C1754 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 94,952 | — | 95,759 |
| C1755 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 94,952 | — | 95,759 |
| C1756 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 94,928 | — | 95,650 |
| C1757 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 94,928 | — | 95,650 |
| C1758 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 94,928 | — | 95,698 |
| C1759 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,928 | — | 95,698 |
| C1760 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | — | 87,906 | 93,980 | 93,980 |
| C1761 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 87,906 | — | 93,980 |
| C1762 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 87,906 | — | 94,096 |
| C1763 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 87,906 | — | 94,096 |
| C1764 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 87,855 | — | 94,269 |
| C1765 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 87,855 | — | 94,269 |
| C1766 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 87,855 | — | 94,230 |
| C1767 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 87,855 | — | 94,230 |
| C1768 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 95,122 | 95,649 | 95,649 |
| C1769 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 95,122 | — | 95,649 |
| C1770 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 95,122 | — | 95,706 |
| C1771 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 95,122 | — | 95,706 |
| C1772 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 95,110 | — | 95,768 |
| C1773 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 95,110 | — | 95,768 |
| C1774 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 95,110 | — | 95,873 |
| C1775 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,110 | — | 95,873 |
| C1776 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 87,763 | 93,997 | 93,997 |
| C1777 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 87,763 | — | 93,997 |
| C1778 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 87,765 | — | 93,861 |
| C1779 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 87,765 | — | 93,861 |
| C1780 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 87,727 | — | 94,224 |
| C1781 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 87,727 | — | 94,224 |
| C1782 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 87,729 | — | 94,217 |
| C1783 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 87,729 | — | 94,217 |
| C1784 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 94,963 | 95,544 | 95,544 |
| C1785 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 94,963 | — | 95,544 |
| C1786 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 94,963 | — | 95,677 |
| C1787 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 94,963 | — | 95,677 |
| C1788 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 94,937 | — | 95,654 |
| C1789 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,937 | — | 95,654 |
| C1790 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 94,937 | — | 95,774 |
| C1791 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 94,937 | — | 95,774 |
| C1792 | ✓ | ✓ | ✓ | — | — | — | — | — | — | — | — | 88,680 | 94,136 | 94,136 |
| C1793 | ✓ | ✓ | ✓ | — | — | — | — | — | — | — | ✓ | 88,335 | — | 94,112 |
| C1794 | ✓ | ✓ | ✓ | — | — | — | — | — | — | ✓ | — | 88,702 | — | 94,188 |
| C1795 | ✓ | ✓ | ✓ | — | — | — | — | — | — | ✓ | ✓ | 88,393 | — | 94,147 |
| C1796 | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | — | — | 88,679 | — | 94,388 |
| C1797 | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | — | ✓ | 88,298 | — | 94,390 |
| C1798 | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | — | 88,700 | — | 94,388 |
| C1799 | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | ✓ | 88,366 | — | 94,345 |
| **C1800 · base** | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | — | — | 95,829 | 95,821 | 95,821 |
| C1801 | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | — | ✓ | 95,593 | — | 95,835 |
| C1802 | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | — | 95,841 | — | 95,897 |
| C1803 | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | ✓ | 95,632 | — | 95,923 |
| C1804 | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | — | 95,871 | — | 95,966 |
| C1805 | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | ✓ | 95,638 | — | 95,966 |
| C1806 | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | — | 95,883 | — | 96,003 |
| C1807 | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 95,681 | — | 96,022 |
| C1808 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | — | — | 88,554 | 94,184 | 94,184 |
| C1809 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | — | ✓ | 88,199 | — | 94,153 |
| C1810 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | — | 88,575 | — | 94,210 |
| C1811 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | ✓ | 88,212 | — | 94,171 |
| C1812 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | — | 88,541 | — | 94,407 |
| C1813 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | ✓ | 88,176 | — | 94,342 |
| C1814 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | — | 88,573 | — | 94,348 |
| C1815 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 88,203 | — | 94,342 |
| C1816 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | — | 95,771 | 95,868 | 95,868 |
| C1817 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | ✓ | 95,487 | — | 95,871 |
| C1818 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | — | 95,783 | — | 95,900 |
| C1819 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 95,493 | — | 96,036 |
| C1820 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | — | 95,817 | — | 95,993 |
| C1821 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 95,546 | — | 95,989 |
| C1822 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 95,833 | — | 95,956 |
| C1823 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 95,557 | — | 96,037 |
| C1824 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | — | — | 88,674 | 94,126 | 94,126 |
| C1825 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | — | ✓ | 88,342 | — | 94,102 |
| C1826 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | — | 88,738 | — | 94,219 |
| C1827 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | ✓ | 88,400 | — | 94,138 |
| C1828 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | — | 88,673 | — | 94,407 |
| C1829 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | ✓ | 88,304 | — | 94,407 |
| C1830 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | — | 88,737 | — | 94,381 |
| C1831 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 88,374 | — | 94,348 |
| C1832 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | — | 95,791 | 95,824 | 95,824 |
| C1833 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | ✓ | 95,542 | — | 95,707 |
| C1834 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | — | 95,824 | — | 95,926 |
| C1835 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 95,581 | — | 95,926 |
| C1836 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | — | 95,826 | — | 95,993 |
| C1837 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 95,577 | — | 96,012 |
| C1838 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 95,859 | — | 96,031 |
| C1839 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,620 | — | 96,037 |
| C1840 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | — | 88,604 | 94,191 | 94,191 |
| C1841 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | ✓ | 88,257 | — | 94,161 |
| C1842 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | — | 88,624 | — | 94,235 |
| C1843 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 88,270 | — | 94,185 |
| C1844 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | — | 88,590 | — | 94,423 |
| C1845 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 88,230 | — | 94,373 |
| C1846 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 88,621 | — | 94,354 |
| C1847 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 88,256 | — | 94,336 |
| C1848 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | — | 95,798 | 95,834 | 95,834 |
| C1849 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 95,479 | — | 95,816 |
| C1850 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 95,803 | — | 96,074 |
| C1851 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,484 | — | 96,065 |
| C1852 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 95,830 | — | 96,001 |
| C1853 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 95,529 | — | 96,064 |
| **C1854 · millor cerca** | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,840 | — | **96,186** |
| C1855 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 95,540 | — | 96,182 |
| C1856 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | — | — | 88,504 | 94,095 | 94,095 |
| C1857 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | — | ✓ | 88,061 | — | 94,084 |
| C1858 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | — | 88,525 | — | 94,136 |
| C1859 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | ✓ | 88,105 | — | 94,120 |
| C1860 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | — | 88,463 | — | 94,337 |
| C1861 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | ✓ | 87,993 | — | 94,362 |
| C1862 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | — | 88,484 | — | 94,326 |
| C1863 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 88,050 | — | 94,282 |
| C1864 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | — | 95,669 | 95,759 | 95,759 |
| C1865 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | ✓ | 95,414 | — | 95,729 |
| C1866 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | — | 95,681 | — | 95,846 |
| C1867 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 95,444 | — | 95,842 |
| C1868 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | — | 95,709 | — | 95,939 |
| C1869 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 95,439 | — | 95,966 |
| C1870 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 95,720 | — | 95,925 |
| C1871 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 95,475 | — | 96,016 |
| C1872 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | — | 88,385 | 94,108 | 94,108 |
| C1873 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | ✓ | 88,009 | — | 94,014 |
| C1874 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | — | 88,406 | — | 94,176 |
| C1875 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 88,010 | — | 94,138 |
| C1876 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | — | 88,355 | — | 94,373 |
| C1877 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 87,940 | — | 94,358 |
| C1878 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 88,389 | — | 94,375 |
| C1879 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 87,955 | — | 94,349 |
| C1880 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | — | 95,687 | 95,802 | 95,802 |
| C1881 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 95,327 | — | 95,619 |
| C1882 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 95,699 | — | 96,031 |
| C1883 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 95,327 | — | 96,031 |
| C1884 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 95,724 | — | 95,858 |
| C1885 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 95,305 | — | 96,012 |
| C1886 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 95,742 | — | 96,081 |
| C1887 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 95,311 | — | 95,996 |
| C1888 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | — | 88,571 | 94,112 | 94,112 |
| C1889 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | ✓ | 88,142 | — | 94,053 |
| C1890 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | — | 88,585 | — | 94,165 |
| C1891 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 88,187 | — | 94,148 |
| C1892 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | — | 88,537 | — | 94,354 |
| C1893 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 88,083 | — | 94,340 |
| C1894 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 88,551 | — | 94,319 |
| C1895 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 88,142 | — | 94,316 |
| C1896 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | — | 95,679 | 95,751 | 95,751 |
| C1897 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 95,389 | — | 95,712 |
| C1898 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 95,690 | — | 95,883 |
| C1899 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 95,420 | — | 95,913 |
| C1900 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 95,720 | — | 95,978 |
| C1901 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 95,419 | — | 96,013 |
| C1902 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 95,730 | — | 95,999 |
| C1903 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,455 | — | 96,038 |
| C1904 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | — | 88,479 | 94,158 | 94,158 |
| C1905 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 88,032 | — | 94,019 |
| C1906 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 88,498 | — | 94,171 |
| C1907 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 88,032 | — | 94,120 |
| C1908 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 88,452 | — | 94,369 |
| C1909 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 87,972 | — | 94,390 |
| C1910 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 88,485 | — | 94,342 |
| C1911 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 87,987 | — | 94,267 |
| C1912 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 95,721 | 95,845 | 95,845 |
| C1913 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 95,291 | — | 95,846 |
| C1914 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 95,726 | — | 96,046 |
| C1915 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,291 | — | 96,021 |
| C1916 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 95,758 | — | 96,013 |
| C1917 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 95,274 | — | 96,016 |
| C1918 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,768 | — | 95,965 |
| C1919 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 95,280 | — | 96,058 |
| C1920 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | — | — | 88,057 | 94,170 | 94,170 |
| C1921 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | — | ✓ | 87,650 | — | 94,109 |
| C1922 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | — | 88,080 | — | 94,208 |
| C1923 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | ✓ | 87,694 | — | 94,212 |
| C1924 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | — | 88,009 | — | 94,378 |
| C1925 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | ✓ | 87,567 | — | 94,381 |
| C1926 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | — | 88,032 | — | 94,355 |
| C1927 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 87,628 | — | 94,348 |
| C1928 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | — | 95,512 | 95,839 | 95,839 |
| C1929 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | ✓ | 95,073 | — | 95,859 |
| C1930 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | — | 95,520 | — | 95,879 |
| C1931 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 95,105 | — | 95,856 |
| C1932 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | — | 95,510 | — | 95,911 |
| C1933 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 95,050 | — | 95,946 |
| C1934 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 95,519 | — | 95,899 |
| C1935 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 95,091 | — | 95,977 |
| C1936 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | — | 87,916 | 94,177 | 94,177 |
| C1937 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | ✓ | 87,697 | — | 94,124 |
| C1938 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | — | 87,939 | — | 94,231 |
| C1939 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 87,711 | — | 94,177 |
| C1940 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | — | 87,833 | — | 94,372 |
| C1941 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 87,607 | — | 94,383 |
| C1942 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 87,870 | — | 94,401 |
| C1943 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 87,638 | — | 94,369 |
| C1944 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | — | 95,314 | 95,860 | 95,860 |
| C1945 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 95,037 | — | 95,897 |
| C1946 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 95,325 | — | 95,931 |
| C1947 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 95,043 | — | 95,952 |
| C1948 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 95,275 | — | 96,014 |
| C1949 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 94,990 | — | 95,975 |
| C1950 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 95,292 | — | 95,986 |
| C1951 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 95,004 | — | 96,015 |
| C1952 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | — | 87,989 | 94,192 | 94,192 |
| C1953 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | ✓ | 87,676 | — | 94,163 |
| C1954 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | — | 88,009 | — | 94,204 |
| C1955 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 87,721 | — | 94,195 |
| C1956 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | — | 87,941 | — | 94,353 |
| C1957 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 87,596 | — | 94,358 |
| C1958 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 87,962 | — | 94,391 |
| C1959 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 87,658 | — | 94,374 |
| C1960 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | — | 95,430 | 95,891 | 95,891 |
| C1961 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 95,040 | — | 95,832 |
| C1962 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 95,435 | — | 95,910 |
| C1963 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 95,073 | — | 95,907 |
| C1964 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 95,421 | — | 95,897 |
| C1965 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 95,011 | — | 96,076 |
| C1966 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 95,427 | — | 96,004 |
| C1967 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,052 | — | 95,972 |
| C1968 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | — | 88,008 | 94,190 | 94,190 |
| C1969 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 87,765 | — | 94,076 |
| C1970 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 88,029 | — | 94,226 |
| C1971 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 87,778 | — | 94,191 |
| C1972 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 87,923 | — | 94,354 |
| C1973 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 87,673 | — | 94,379 |
| C1974 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 87,958 | — | 94,394 |
| C1975 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 87,704 | — | 94,330 |
| C1976 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 95,364 | 95,846 | 95,846 |
| C1977 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 95,028 | — | 95,834 |
| C1978 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 95,368 | — | 96,062 |
| C1979 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,033 | — | 96,050 |
| C1980 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 95,321 | — | 95,978 |
| C1981 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,977 | — | 96,017 |
| C1982 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,331 | — | 96,112 |
| C1983 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 94,991 | — | 96,179 |
| C1984 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | — | 87,847 | 94,138 | 94,138 |
| C1985 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | ✓ | 87,296 | — | 94,071 |
| C1986 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | — | 87,879 | — | 94,154 |
| C1987 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 87,350 | — | 94,134 |
| C1988 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | — | 87,765 | — | 94,328 |
| C1989 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 87,191 | — | 94,320 |
| C1990 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 87,798 | — | 94,316 |
| C1991 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 87,263 | — | 94,305 |
| C1992 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | — | 95,256 | 95,789 | 95,789 |
| C1993 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 94,793 | — | 95,799 |
| C1994 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 95,290 | — | 95,798 |
| C1995 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 94,833 | — | 95,799 |
| C1996 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 95,233 | — | 95,954 |
| C1997 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 94,742 | — | 95,961 |
| C1998 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 95,267 | — | 95,898 |
| C1999 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 94,791 | — | 95,975 |
| C2000 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | — | 87,851 | 94,157 | 94,157 |
| C2001 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 87,451 | — | 94,090 |
| C2002 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 87,875 | — | 94,184 |
| C2003 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 87,451 | — | 94,133 |
| C2004 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 87,764 | — | 94,360 |
| C2005 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 87,366 | — | 94,297 |
| C2006 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 87,805 | — | 94,367 |
| C2007 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 87,384 | — | 94,344 |
| C2008 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 95,182 | 95,754 | 95,754 |
| C2009 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 94,813 | — | 95,738 |
| C2010 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 95,196 | — | 95,819 |
| C2011 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 94,813 | — | 95,889 |
| C2012 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 95,137 | — | 95,924 |
| C2013 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 94,748 | — | 95,992 |
| C2014 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 95,159 | — | 95,960 |
| C2015 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,757 | — | 95,997 |
| C2016 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | 87,906 | 94,143 | 94,143 |
| C2017 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 87,376 | — | 94,094 |
| C2018 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 87,939 | — | 94,134 |
| C2019 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 87,431 | — | 94,094 |
| C2020 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 87,834 | — | 94,336 |
| C2021 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 87,282 | — | 94,289 |
| C2022 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 87,867 | — | 94,355 |
| C2023 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 87,354 | — | 94,283 |
| C2024 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 95,269 | 95,819 | 95,819 |
| C2025 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 94,767 | — | 95,868 |
| C2026 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 95,298 | — | 95,819 |
| C2027 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 94,807 | — | 95,864 |
| C2028 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 95,251 | — | 95,983 |
| C2029 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 94,722 | — | 95,962 |
| C2030 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 95,280 | — | 95,989 |
| C2031 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 94,770 | — | 96,029 |
| C2032 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 87,956 | 94,157 | 94,157 |
| C2033 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 87,473 | — | 94,099 |
| C2034 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 87,979 | — | 94,181 |
| C2035 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 87,473 | — | 94,118 |
| C2036 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 87,877 | — | 94,325 |
| C2037 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 87,397 | — | 94,384 |
| C2038 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 87,917 | — | 94,363 |
| C2039 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 87,415 | — | 94,343 |
| C2040 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 95,223 | 95,843 | 95,843 |
| C2041 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 94,769 | — | 95,781 |
| C2042 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 95,231 | — | 96,064 |
| C2043 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 94,769 | — | 96,063 |
| C2044 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 95,183 | — | 95,971 |
| C2045 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,709 | — | 96,012 |
| C2046 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 95,199 | — | 96,005 |
| C2047 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 94,718 | — | 96,039 |

Els valors exactes de cada fila són al [CSV de combinacions ajustades](https://github.com/victor836768/P2/blob/jordi-albareda-combinacions/resultats/combinacions/combinacions_ajustades.csv). Hi ha files repetides perquè algunes idees no fan res quan una altra està apagada.
<!-- final-matriu-combinacions -->

## Com ho he comprovat

Per no haver de llegir els àudios a cada prova, primer calculo les potències amb el codi C. Després faig servir el mateix detector amb aquestes potències. Les marques de referència només es fan servir per puntuar el resultat.

Després he comprovat **33 configuracions** amb el programa normal, llegint els WAVE originals, i amb el `vad_evaluation.pl` original. Hi ha la base, cada idea sola, cada idea canviada respecte de la base i les deu millors combinacions ajustades. Els resultats coincideixen, comptant que el Perl només mostra tres decimals al TOTAL.

També he comprovat àudios petits a 8, 16 i 48 kHz: silenci, cops, baixades, desplaçament respecte de zero, els dos llindars, les esperes i els límits dels segments. He provat totes les idees juntes i opcions mal escrites. Les proves noves comproven també que el ZCR no accepti blocs sense prou energia, que la confirmació caduqui i que el soroll no incorpori blocs massa alts.

Tot això és amb `db.v4`, que ja havia fet servir abans. Caldria provar àudios nous per saber si també va bé fora d’aquesta base.

## On són les proves

A la branca [jordi-albareda-combinacions](https://github.com/victor836768/P2/tree/jordi-albareda-combinacions):

- `scripts/prova_combinacions.py`: combinacions i ajust de valors.
- `scripts/comprova_metodes.py`: àudios petits amb casos coneguts.
- `resultats/combinacions/combinacions_amb_valors_fixos.csv`: les 8.192 files fixes.
- `resultats/combinacions/combinacions_vuit_metodes.csv`: l’estudi anterior amb vuit idees.
- `scripts/comprova_metodes_nous.py`: casos petits per a les tres idees inspirades en altres grups.
- `resultats/combinacions/canvis_per_parelles.csv`: què passa quan només activo una idea.
- `resultats/combinacions/combinacions_afinament_anterior.csv`: els guanyadors de la cerca anterior, només per comparar.
- `resultats/combinacions/combinacions_ajustades.csv`: el millor trobat per la cerca adaptativa per a cadascun dels 2.048 grups.
- `resultats/combinacions/recorregut_cerca.csv`: com es mou el centre, canvia el pas i arriba a cada resultat.
- `resultats/combinacions/combinacions_abans_afinament.csv` i `afinament_detall_anterior.csv`: els estudis anteriors, que conservo com a historial.
- `resultats/combinacions/verificacio.csv`: comparació amb el programa normal i el Perl.
- `resultats/combinacions/avaluacio_millor.txt`: resultat complet de la millor configuració trobada.

Les tres proves inicials per separat també es conserven a `jordi-albareda-prova-soroll`, `jordi-albareda-prova-baixada` i `jordi-albareda-prova-dc`.

## Altres coses del treball

A la base d’entrega el ZCR només es dibuixa. A la branca de combinacions ara també pot ajudar a decidir si hi ha veu. L’amplitud mitjana continua sense intervenir en la decisió.

Les opcions de `docopt_c`, `cardem-li`, els rànquings i les gràfiques ajuden a fer i explicar les proves. No són canvis en la manera de detectar veu. Tampoc he implementat la cancel·lació del silenci.

La lectura correcta del fitxer, la durada final, les etiquetes S/V i el tractament dels errors es mantenen a totes les proves. No els desactivo per intentar pujar la puntuació.
