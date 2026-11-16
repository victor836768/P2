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

### Com comença la cerca

La cerca nova no llegeix els guanyadors anteriors per decidir on comença. Parteixo d’uns valors normals: 100 ms inicials, 50 ms de veu, 150 ms de silenci, marge de 6 dB, alfa de 0,01 i diferència d’1 dB entre llindars.

Per no dependre d’un sol començament, faig tres inicis. El primer surt una mica per sota d’aquests valors, el segon al centre i el tercer una mica per sobre. Els dos extrems es calculen sumant o restant el pas inicial; no són llistes de valors bons triats d’una prova anterior.

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

Poso límits amplis per no anar cap a valors absurds: 20–400 ms inicials, 20–200 ms de veu, 20–500 ms de silenci, marge de 2–14 dB, alfa entre 0,0001 i 0,1 i diferència entre llindars de 0,01–4 dB. La diferència ha de ser menor que el marge. Aquests són límits de cerca, no els resultats que vull obtenir.

Hi ha un màxim de 60 voltes per inici com a límit de temps. En aquesta execució **cap dels 768 inicis ha arribat al límit**: tots han acabat perquè el pas ja era petit i no milloraven.

### Què conservo de les proves anteriors

Els quatre grups històrics continuen servint per comparar les idees amb valors fixos. No serveixen per iniciar o orientar la cerca adaptativa.

| Grup històric | Blocs inicials | Blocs de veu | Blocs de silenci | Marge | Alfa |
|---|---:|---:|---:|---:|---:|
| Primer ajust | 20 | 5 | 15 | 8 dB | 0,02 |
| Base de 6 dB | 10 | 8 | 15 | 6 dB | 0,02 |
| Ajust de 6,63 dB | 10 | 8 | 15 | 6,63 dB | 0,02 |
| Base actual | 9 | 8 | 17 | 5,94 dB | 0,00615 |

Si hi ha histèresi, en aquestes comparacions fixes separo els llindars 1 dB. Són les mateixes 1.024 files de comparació que abans.

La cerca adaptativa ha calculat **46.888 configuracions diferents**. El recorregut queda guardat a `recorregut_cerca.csv`: es veu quan mou el centre, quan redueix el pas i quan para.

Respecte de la cerca anterior, **183 combinacions milloren, 66 baixen i set queden igual**. No recupero el guanyador anterior per fer veure que la cerca nova sempre millora. Conservo tots dos resultats a la matriu. Dins de cada recorregut sí que mantinc sempre el millor punt trobat fins llavors.

Això s’acosta a un bon resultat, però no garanteix el perfecte. Hi pot haver altres zones bones que aquests tres inicis no trobin. A més, tot s’ha ajustat amb `db.v4`, no amb àudios nous.

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
| Millor resultat de la cerca anterior | 95,871 % |
| Millor resultat de la cerca adaptativa | **95,891 %** |

La millor combinació manté les esperes de veu i silenci, el seguiment del soroll i el retorn al primer bloc pendent. També fa servir **histèresi i una baixada curta permesa**. No treu el pic inicial ni la mitjana.

Ha arribat a nou blocs inicials, **set blocs de veu**, 17 de silenci, marge de **7,885 dB**, alfa d’aproximadament **0,00402138** i una diferència de **2,09375 dB** entre llindars. Aquests valors són el resultat del recorregut, no valors posats al començament.

El guany és d’uns **0,020 punts respecte de la cerca anterior** i **0,062 punts respecte de la base d’entrega**. La configuració nova queda a la branca de combinacions. El detector per defecte de l’entrega no ha canviat.

<!-- inici-matriu-combinacions -->
## Matriu de totes les combinacions

Cada fila és una combinació. **✓** vol dir activat i **—** vol dir desactivat.

**Veu** i **Sil.** són les esperes de veu i silenci; **Sor.** és el seguiment del soroll; **Hist.** són els dos llindars; **Pic** deixa fora el pic inicial; **Baix.** permet una baixada; **DC** treu la mitjana; **Ret.** torna al primer bloc pendent.

**Fix** és el TOTAL amb els valors de la base actual. Si activo la histèresi, separo els llindars 1 dB. **Anterior** és el millor resultat de la cerca anterior. **Adaptativa** és el resultat de la cerca nova, que mou el centre i redueix el pas segons les puntuacions. Per tant, les columnes ajustades poden fer servir paràmetres diferents a cada fila. Els tres resultats són sobre les 115 gravacions de `db.v4`.

La **C225** és la combinació de la base actual. La millor cerca adaptativa és a **C245**. El número identifica els vuit interruptors en l’ordre de les columnes; les files van de C000 a C255.

| Combinació | Veu | Sil. | Sor. | Hist. | Pic | Baix. | DC | Ret. | Fix (%) | Anterior (%) | Adaptativa (%) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---:|---:|---:|
| C000 | — | — | — | — | — | — | — | — | 90,943 | 91,678 | 91,690 |
| C001 | — | — | — | — | — | — | — | ✓ | 90,943 | 91,678 | 91,690 |
| C002 | — | — | — | — | — | — | ✓ | — | 91,063 | 91,612 | 91,612 |
| C003 | — | — | — | — | — | — | ✓ | ✓ | 91,063 | 91,612 | 91,612 |
| C004 | — | — | — | — | — | ✓ | — | — | 90,943 | 91,678 | 91,690 |
| C005 | — | — | — | — | — | ✓ | — | ✓ | 90,943 | 91,678 | 91,690 |
| C006 | — | — | — | — | — | ✓ | ✓ | — | 91,063 | 91,612 | 91,612 |
| C007 | — | — | — | — | — | ✓ | ✓ | ✓ | 91,063 | 91,612 | 91,612 |
| C008 | — | — | — | — | ✓ | — | — | — | 91,180 | 91,674 | 91,674 |
| C009 | — | — | — | — | ✓ | — | — | ✓ | 91,180 | 91,674 | 91,674 |
| C010 | — | — | — | — | ✓ | — | ✓ | — | 91,214 | 91,611 | 91,610 |
| C011 | — | — | — | — | ✓ | — | ✓ | ✓ | 91,214 | 91,611 | 91,610 |
| C012 | — | — | — | — | ✓ | ✓ | — | — | 91,180 | 91,674 | 91,674 |
| C013 | — | — | — | — | ✓ | ✓ | — | ✓ | 91,180 | 91,674 | 91,674 |
| C014 | — | — | — | — | ✓ | ✓ | ✓ | — | 91,214 | 91,611 | 91,610 |
| C015 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,214 | 91,611 | 91,610 |
| C016 | — | — | — | ✓ | — | — | — | — | 91,408 | 92,219 | 92,551 |
| C017 | — | — | — | ✓ | — | — | — | ✓ | 91,408 | 92,219 | 92,551 |
| C018 | — | — | — | ✓ | — | — | ✓ | — | 91,440 | 92,100 | 92,511 |
| C019 | — | — | — | ✓ | — | — | ✓ | ✓ | 91,440 | 92,100 | 92,511 |
| C020 | — | — | — | ✓ | — | ✓ | — | — | 91,408 | 92,219 | 92,551 |
| C021 | — | — | — | ✓ | — | ✓ | — | ✓ | 91,408 | 92,219 | 92,551 |
| C022 | — | — | — | ✓ | — | ✓ | ✓ | — | 91,440 | 92,100 | 92,511 |
| C023 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 91,440 | 92,100 | 92,511 |
| C024 | — | — | — | ✓ | ✓ | — | — | — | 91,567 | 92,223 | 92,560 |
| C025 | — | — | — | ✓ | ✓ | — | — | ✓ | 91,567 | 92,223 | 92,560 |
| C026 | — | — | — | ✓ | ✓ | — | ✓ | — | 91,524 | 92,108 | 92,476 |
| C027 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,524 | 92,108 | 92,476 |
| C028 | — | — | — | ✓ | ✓ | ✓ | — | — | 91,567 | 92,223 | 92,560 |
| C029 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,567 | 92,223 | 92,560 |
| C030 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 91,524 | 92,108 | 92,476 |
| C031 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,524 | 92,108 | 92,476 |
| C032 | — | — | ✓ | — | — | — | — | — | 91,244 | 91,830 | 91,827 |
| C033 | — | — | ✓ | — | — | — | — | ✓ | 91,244 | 91,830 | 91,827 |
| C034 | — | — | ✓ | — | — | — | ✓ | — | 91,257 | 91,769 | 91,769 |
| C035 | — | — | ✓ | — | — | — | ✓ | ✓ | 91,257 | 91,769 | 91,769 |
| C036 | — | — | ✓ | — | — | ✓ | — | — | 91,244 | 91,830 | 91,827 |
| C037 | — | — | ✓ | — | — | ✓ | — | ✓ | 91,244 | 91,830 | 91,827 |
| C038 | — | — | ✓ | — | — | ✓ | ✓ | — | 91,257 | 91,769 | 91,769 |
| C039 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 91,257 | 91,769 | 91,769 |
| C040 | — | — | ✓ | — | ✓ | — | — | — | 91,371 | 91,867 | 91,853 |
| C041 | — | — | ✓ | — | ✓ | — | — | ✓ | 91,371 | 91,867 | 91,853 |
| C042 | — | — | ✓ | — | ✓ | — | ✓ | — | 91,396 | 91,793 | 91,830 |
| C043 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,396 | 91,793 | 91,830 |
| C044 | — | — | ✓ | — | ✓ | ✓ | — | — | 91,371 | 91,867 | 91,853 |
| C045 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,371 | 91,867 | 91,853 |
| C046 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 91,396 | 91,793 | 91,830 |
| C047 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,396 | 91,793 | 91,830 |
| C048 | — | — | ✓ | ✓ | — | — | — | — | 91,722 | 92,413 | 92,739 |
| C049 | — | — | ✓ | ✓ | — | — | — | ✓ | 91,722 | 92,413 | 92,739 |
| C050 | — | — | ✓ | ✓ | — | — | ✓ | — | 91,691 | 92,369 | 92,767 |
| C051 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,691 | 92,369 | 92,767 |
| C052 | — | — | ✓ | ✓ | — | ✓ | — | — | 91,722 | 92,413 | 92,739 |
| C053 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 91,722 | 92,413 | 92,739 |
| C054 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 91,691 | 92,369 | 92,767 |
| C055 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,691 | 92,369 | 92,767 |
| C056 | — | — | ✓ | ✓ | ✓ | — | — | — | 91,762 | 92,454 | 92,778 |
| C057 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,762 | 92,454 | 92,778 |
| C058 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 91,752 | 92,342 | 92,738 |
| C059 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,752 | 92,342 | 92,738 |
| C060 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,762 | 92,454 | 92,778 |
| C061 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,762 | 92,454 | 92,778 |
| C062 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,752 | 92,342 | 92,738 |
| C063 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,752 | 92,342 | 92,738 |
| C064 | — | ✓ | — | — | — | — | — | — | 91,736 | 94,495 | 94,494 |
| C065 | — | ✓ | — | — | — | — | — | ✓ | 94,958 | 95,220 | 95,223 |
| C066 | — | ✓ | — | — | — | — | ✓ | — | 91,539 | 94,449 | 94,474 |
| C067 | — | ✓ | — | — | — | — | ✓ | ✓ | 94,864 | 95,224 | 95,229 |
| C068 | — | ✓ | — | — | — | ✓ | — | — | 91,736 | 94,495 | 94,494 |
| C069 | — | ✓ | — | — | — | ✓ | — | ✓ | 94,958 | 95,220 | 95,223 |
| C070 | — | ✓ | — | — | — | ✓ | ✓ | — | 91,539 | 94,449 | 94,474 |
| C071 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 94,864 | 95,224 | 95,229 |
| C072 | — | ✓ | — | — | ✓ | — | — | — | 91,093 | 94,450 | 94,467 |
| C073 | — | ✓ | — | — | ✓ | — | — | ✓ | 94,708 | 95,137 | 95,234 |
| C074 | — | ✓ | — | — | ✓ | — | ✓ | — | 90,757 | 94,384 | 94,455 |
| C075 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 94,614 | 95,211 | 95,202 |
| C076 | — | ✓ | — | — | ✓ | ✓ | — | — | 91,093 | 94,450 | 94,467 |
| C077 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 94,708 | 95,137 | 95,234 |
| C078 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 90,757 | 94,384 | 94,455 |
| C079 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 94,614 | 95,211 | 95,202 |
| C080 | — | ✓ | — | ✓ | — | — | — | — | 91,157 | 94,512 | 94,591 |
| C081 | — | ✓ | — | ✓ | — | — | — | ✓ | 94,519 | 95,299 | 95,260 |
| C082 | — | ✓ | — | ✓ | — | — | ✓ | — | 90,941 | 94,464 | 94,494 |
| C083 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 94,378 | 95,259 | 95,269 |
| C084 | — | ✓ | — | ✓ | — | ✓ | — | — | 91,157 | 94,512 | 94,591 |
| C085 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 94,519 | 95,299 | 95,260 |
| C086 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 90,941 | 94,464 | 94,494 |
| C087 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 94,378 | 95,259 | 95,269 |
| C088 | — | ✓ | — | ✓ | ✓ | — | — | — | 90,403 | 94,464 | 94,549 |
| C089 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 94,184 | 95,131 | 95,130 |
| C090 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 90,095 | 94,399 | 94,474 |
| C091 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 94,006 | 95,169 | 95,236 |
| C092 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 90,403 | 94,464 | 94,549 |
| C093 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 94,184 | 95,131 | 95,130 |
| C094 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 90,095 | 94,399 | 94,474 |
| C095 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,006 | 95,169 | 95,236 |
| C096 | — | ✓ | ✓ | — | — | — | — | — | 91,097 | 94,627 | 94,627 |
| C097 | — | ✓ | ✓ | — | — | — | — | ✓ | 94,871 | 95,450 | 95,423 |
| C098 | — | ✓ | ✓ | — | — | — | ✓ | — | 90,939 | 94,619 | 94,665 |
| C099 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 94,792 | 95,416 | 95,450 |
| C100 | — | ✓ | ✓ | — | — | ✓ | — | — | 91,097 | 94,627 | 94,627 |
| C101 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 94,871 | 95,450 | 95,423 |
| C102 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 90,939 | 94,619 | 94,665 |
| C103 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 94,792 | 95,416 | 95,450 |
| C104 | — | ✓ | ✓ | — | ✓ | — | — | — | 90,727 | 94,579 | 94,621 |
| C105 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 94,696 | 95,383 | 95,362 |
| C106 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 90,528 | 94,521 | 94,646 |
| C107 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 94,614 | 95,433 | 95,348 |
| C108 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 90,727 | 94,579 | 94,621 |
| C109 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 94,696 | 95,383 | 95,362 |
| C110 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 90,528 | 94,521 | 94,646 |
| C111 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 94,614 | 95,433 | 95,348 |
| C112 | — | ✓ | ✓ | ✓ | — | — | — | — | 90,366 | 94,660 | 94,705 |
| C113 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 94,324 | 95,409 | 95,502 |
| C114 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 90,297 | 94,636 | 94,708 |
| C115 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 94,288 | 95,572 | 95,505 |
| C116 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 90,366 | 94,660 | 94,705 |
| C117 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 94,324 | 95,409 | 95,502 |
| C118 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 90,297 | 94,636 | 94,708 |
| C119 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 94,288 | 95,572 | 95,505 |
| C120 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 89,891 | 94,607 | 94,657 |
| C121 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 94,044 | 95,480 | 95,408 |
| C122 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 89,799 | 94,622 | 94,658 |
| C123 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 93,989 | 95,525 | 95,413 |
| C124 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 89,891 | 94,607 | 94,657 |
| C125 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,044 | 95,480 | 95,408 |
| C126 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 89,799 | 94,622 | 94,658 |
| C127 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 93,989 | 95,525 | 95,413 |
| C128 | ✓ | — | — | — | — | — | — | — | 80,661 | 90,844 | 91,041 |
| C129 | ✓ | — | — | — | — | — | — | ✓ | 90,494 | 92,044 | 92,518 |
| C130 | ✓ | — | — | — | — | — | ✓ | — | 81,005 | 90,851 | 90,954 |
| C131 | ✓ | — | — | — | — | — | ✓ | ✓ | 90,686 | 92,086 | 92,430 |
| C132 | ✓ | — | — | — | — | ✓ | — | — | 80,866 | 90,843 | 90,976 |
| C133 | ✓ | — | — | — | — | ✓ | — | ✓ | 90,779 | 92,165 | 92,471 |
| C134 | ✓ | — | — | — | — | ✓ | ✓ | — | 81,192 | 90,831 | 90,903 |
| C135 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 90,919 | 92,164 | 92,379 |
| C136 | ✓ | — | — | — | ✓ | — | — | — | 81,358 | 90,954 | 91,059 |
| C137 | ✓ | — | — | — | ✓ | — | — | ✓ | 90,822 | 92,218 | 92,535 |
| C138 | ✓ | — | — | — | ✓ | — | ✓ | — | 81,585 | 90,858 | 90,981 |
| C139 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 90,957 | 92,108 | 92,432 |
| C140 | ✓ | — | — | — | ✓ | ✓ | — | — | 81,510 | 90,949 | 91,004 |
| C141 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 91,071 | 92,244 | 92,486 |
| C142 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 81,722 | 90,871 | 90,908 |
| C143 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,157 | 92,152 | 92,391 |
| C144 | ✓ | — | — | ✓ | — | — | — | — | 81,639 | 91,634 | 91,781 |
| C145 | ✓ | — | — | ✓ | — | — | — | ✓ | 90,971 | 92,875 | 93,189 |
| C146 | ✓ | — | — | ✓ | — | — | ✓ | — | 81,810 | 91,523 | 91,756 |
| C147 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 91,066 | 92,820 | 93,029 |
| C148 | ✓ | — | — | ✓ | — | ✓ | — | — | 81,824 | 91,573 | 91,762 |
| C149 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 91,241 | 92,894 | 93,189 |
| C150 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 81,995 | 91,521 | 91,897 |
| C151 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 91,305 | 92,958 | 93,027 |
| C152 | ✓ | — | — | ✓ | ✓ | — | — | — | 82,163 | 91,611 | 91,972 |
| C153 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 91,276 | 92,953 | 93,289 |
| C154 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 82,327 | 91,487 | 91,828 |
| C155 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,368 | 92,800 | 93,023 |
| C156 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 82,307 | 91,552 | 91,958 |
| C157 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,513 | 93,008 | 93,252 |
| C158 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 82,455 | 91,477 | 91,832 |
| C159 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,555 | 92,837 | 92,960 |
| C160 | ✓ | — | ✓ | — | — | — | — | — | 80,970 | 91,104 | 91,129 |
| C161 | ✓ | — | ✓ | — | — | — | — | ✓ | 90,779 | 92,486 | 92,587 |
| C162 | ✓ | — | ✓ | — | — | — | ✓ | — | 81,134 | 91,111 | 91,120 |
| C163 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 90,871 | 92,433 | 92,522 |
| C164 | ✓ | — | ✓ | — | — | ✓ | — | — | 81,199 | 91,059 | 91,092 |
| C165 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 91,072 | 92,491 | 92,559 |
| C166 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 81,390 | 91,041 | 91,140 |
| C167 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 91,179 | 92,454 | 92,482 |
| C168 | ✓ | — | ✓ | — | ✓ | — | — | — | 81,348 | 91,145 | 91,144 |
| C169 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 90,998 | 92,517 | 92,613 |
| C170 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 81,520 | 91,031 | 91,137 |
| C171 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,127 | 92,434 | 92,518 |
| C172 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 81,600 | 91,136 | 91,123 |
| C173 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,338 | 92,540 | 92,572 |
| C174 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 81,776 | 90,958 | 91,105 |
| C175 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,446 | 92,504 | 92,561 |
| C176 | ✓ | — | ✓ | ✓ | — | — | — | — | 82,020 | 91,662 | 92,026 |
| C177 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 91,354 | 93,126 | 93,410 |
| C178 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 82,065 | 91,621 | 92,091 |
| C179 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,362 | 93,010 | 93,310 |
| C180 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 82,236 | 91,728 | 92,096 |
| C181 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 91,618 | 93,145 | 93,393 |
| C182 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 82,313 | 91,655 | 91,782 |
| C183 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,666 | 93,095 | 93,127 |
| C184 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 82,292 | 91,737 | 91,784 |
| C185 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,499 | 93,218 | 93,424 |
| C186 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 82,370 | 91,591 | 92,030 |
| C187 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,584 | 93,107 | 93,304 |
| C188 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 82,505 | 91,680 | 92,159 |
| C189 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,792 | 93,121 | 93,389 |
| C190 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 82,550 | 91,655 | 91,821 |
| C191 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,834 | 93,101 | 93,172 |
| C192 | ✓ | ✓ | — | — | — | — | — | — | 88,655 | 94,017 | 94,030 |
| C193 | ✓ | ✓ | — | — | — | — | — | ✓ | 95,592 | 95,640 | 95,639 |
| C194 | ✓ | ✓ | — | — | — | — | ✓ | — | 88,490 | 93,946 | 93,955 |
| C195 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 95,516 | 95,566 | 95,578 |
| C196 | ✓ | ✓ | — | — | — | ✓ | — | — | 88,732 | 94,013 | 94,011 |
| C197 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 95,621 | 95,679 | 95,678 |
| C198 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 88,575 | 93,949 | 93,948 |
| C199 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 95,532 | 95,604 | 95,613 |
| C200 | ✓ | ✓ | — | — | ✓ | — | — | — | 88,438 | 94,002 | 93,969 |
| C201 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 95,478 | 95,608 | 95,586 |
| C202 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 88,289 | 93,615 | 93,977 |
| C203 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 95,409 | 95,556 | 95,522 |
| C204 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 88,475 | 93,991 | 93,992 |
| C205 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 95,472 | 95,588 | 95,588 |
| C206 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 88,346 | 93,571 | 93,964 |
| C207 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 95,418 | 95,581 | 95,584 |
| C208 | ✓ | ✓ | — | ✓ | — | — | — | — | 88,155 | 94,036 | 94,025 |
| C209 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 95,317 | 95,680 | 95,671 |
| C210 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 87,936 | 93,715 | 94,011 |
| C211 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 95,086 | 95,615 | 95,609 |
| C212 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 88,242 | 93,784 | 94,010 |
| C213 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 95,356 | 95,688 | 95,724 |
| C214 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 88,034 | 93,749 | 94,042 |
| C215 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 95,118 | 95,681 | 95,652 |
| C216 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 87,854 | 93,788 | 93,996 |
| C217 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 95,114 | 95,595 | 95,652 |
| C218 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 87,706 | 93,627 | 93,965 |
| C219 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 94,952 | 95,542 | 95,527 |
| C220 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 87,906 | 93,735 | 93,980 |
| C221 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 95,122 | 95,650 | 95,649 |
| C222 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 87,763 | 93,566 | 93,997 |
| C223 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,963 | 95,604 | 95,544 |
| C224 | ✓ | ✓ | ✓ | — | — | — | — | — | 88,680 | 94,126 | 94,136 |
| **C225 · base** | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 95,829 | 95,829 | 95,821 |
| C226 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 88,554 | 94,177 | 94,184 |
| C227 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 95,771 | 95,832 | 95,868 |
| C228 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 88,674 | 94,124 | 94,126 |
| C229 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 95,791 | 95,833 | 95,824 |
| C230 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 88,604 | 94,192 | 94,191 |
| C231 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 95,798 | 95,825 | 95,834 |
| C232 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 88,504 | 94,102 | 94,095 |
| C233 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 95,669 | 95,760 | 95,759 |
| C234 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 88,385 | 94,131 | 94,108 |
| C235 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 95,687 | 95,731 | 95,802 |
| C236 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 88,571 | 94,108 | 94,112 |
| C237 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 95,679 | 95,767 | 95,751 |
| C238 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 88,479 | 94,133 | 94,158 |
| C239 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,721 | 95,773 | 95,845 |
| C240 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 88,057 | 94,020 | 94,170 |
| C241 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 95,512 | 95,825 | 95,839 |
| C242 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 87,916 | 93,926 | 94,177 |
| C243 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 95,314 | 95,856 | 95,860 |
| C244 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 87,989 | 93,930 | 94,192 |
| **C245 · millor cerca** | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 95,430 | 95,871 | **95,891** |
| C246 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 88,008 | 93,961 | 94,190 |
| C247 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 95,364 | 95,867 | 95,846 |
| C248 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 87,847 | 93,939 | 94,138 |
| C249 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 95,256 | 95,760 | 95,789 |
| C250 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 87,851 | 93,873 | 94,157 |
| C251 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,182 | 95,801 | 95,754 |
| C252 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 87,906 | 93,922 | 94,143 |
| C253 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 95,269 | 95,780 | 95,819 |
| C254 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 87,956 | 94,117 | 94,157 |
| C255 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 95,223 | 95,857 | 95,843 |

Els paràmetres concrets de cada ajust són al [CSV de combinacions ajustades](https://github.com/victor836768/P2/blob/jordi-albareda-combinacions/resultats/combinacions/combinacions_ajustades.csv). Algunes files donen el mateix perquè hi ha idees que no fan res si una altra està desactivada.
<!-- final-matriu-combinacions -->

## Com ho he comprovat

La prova ràpida calcula les potències amb el codi C i fa servir el mateix autòmat del detector. Les referències només serveixen per calcular la puntuació.

Després he comprovat **27 configuracions** amb el programa normal, llegint els WAVE originals, i amb el `vad_evaluation.pl` original. Hi ha la base, cada idea sola, cada idea canviada respecte de la base i les deu millors combinacions ajustades. Les puntuacions coincideixen amb les de la prova ràpida dins de l’arrodoniment del Perl.

També he comprovat àudios petits a 8, 16 i 48 kHz: silenci, cops, baixades, desplaçament respecte de zero, els dos llindars, les esperes i els límits dels segments. He provat totes les idees juntes i opcions mal escrites.

Tot això és sobre `db.v4`, que ja havia fet servir per ajustar la base. No és una prova amb dades noves ni una garantia del millor resultat possible.

## On són les proves

A la branca [jordi-albareda-combinacions](https://github.com/victor836768/P2/tree/jordi-albareda-combinacions):

- `scripts/prova_combinacions.py`: combinacions i ajust de valors.
- `scripts/comprova_metodes.py`: àudios petits amb casos coneguts.
- `resultats/combinacions/combinacions_amb_valors_fixos.csv`: les 1.024 files inicials.
- `resultats/combinacions/canvis_per_parelles.csv`: què passa quan només activo una idea.
- `resultats/combinacions/combinacions_afinament_anterior.csv`: els guanyadors de la cerca anterior, només per comparar.
- `resultats/combinacions/combinacions_ajustades.csv`: el millor trobat per la cerca adaptativa per a cadascun dels 256 grups.
- `resultats/combinacions/recorregut_cerca.csv`: com es mou el centre, canvia el pas i arriba a cada resultat.
- `resultats/combinacions/combinacions_abans_afinament.csv` i `afinament_detall_anterior.csv`: els estudis anteriors, que conservo com a historial.
- `resultats/combinacions/verificacio.csv`: comparació amb el programa normal i el Perl.
- `resultats/combinacions/avaluacio_millor.txt`: resultat complet de la millor configuració trobada.

Les tres proves inicials per separat també es conserven a `jordi-albareda-prova-soroll`, `jordi-albareda-prova-baixada` i `jordi-albareda-prova-dc`.

## Altres coses del treball

He dibuixat el ZCR i he calculat l’amplitud mitjana, però no hi ha cap regla del detector que els faci servir. Per això no els poso com si fossin mètodes ja provats. Afegir-los com a decisió seria una prova nova.

Les opcions de `docopt_c`, `cardem-li`, els rànquings i les gràfiques ajuden a fer i explicar les proves. No són canvis en la manera de detectar veu. Tampoc he implementat la cancel·lació del silenci.

La lectura correcta del fitxer, la durada final, les etiquetes S/V i el tractament dels errors es mantenen a totes les proves. No els desactivo per intentar pujar la puntuació.
