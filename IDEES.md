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

La primera cerca tenia **11.201 configuracions diferents**. Després he afegit una cerca més fina al voltant del millor valor de cada combinació.

### Afinar al voltant del millor valor

Si el millor marge és 5,94 dB, no em quedo només amb aquest nombre. Primer provo de 5,74 a 6,14 dB, amb pas de 0,02 dB. Això inclou 5,90, 5,92, 5,96 i 6,00 dB. Després torno a mirar els voltants del millor, amb pas de 0,01 dB.

Faig una cosa semblant amb els altres valors:

- Temps inicial i duracions: dos blocs menys i dos més, amb pas d’un bloc de 10 ms.
- Alfa: primer un 20 % per sota i per sobre, amb 21 valors. Després un 5 %, també amb 21 valors.
- Diferència entre llindars: primer passos de 0,05 dB, després de 0,01 dB.
- També provo marge i alfa junts, en una petita graella de cinc valors de cada un.

Sempre torno a centrar la cerca al millor valor que he trobat. Faig com a mínim dues passades fines i com a màxim tres. Si després de la segona ja no millora, paro. Les idees desactivades continuen desactivades.

Conservo els resultats del primer ajust i no accepto un resultat pitjor. Amb aquesta passada, **249 combinacions milloren i set queden igual**. Cap empitjora.

En total, la cerca amb l’afinament calcula **45.163 configuracions diferents**. Els punts de les passades fines queden a `afinament_detall.csv`. També he comprovat que, per a la combinació de la base, s’han provat explícitament 5,90 i 6,00 dB.

Continua sent una cerca limitada. No he provat tots els nombres possibles ni totes les barreges possibles dels paràmetres.

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
| Millor combinació amb l’ajust curt anterior | 95,831 % |
| Millor combinació després d’afinar | **95,871 %** |

La millor combinació ara manté l’espera de veu, l’espera de silenci, el seguiment del soroll i el retorn al primer bloc pendent. També fa servir **histèresi i una baixada curta permesa**. No treu el pic inicial ni la mitjana.

Fa servir nou blocs inicials, vuit blocs de veu, **16 de silenci**, marge de **6,75 dB**, alfa de **0,005842** i una diferència de **0,99 dB** entre llindars.

Abans d’afinar, la millor combinació treia la mitjana i donava 95,831 %. La nova cerca mostra que hi havia una altra combinació que podia anar millor canviant una mica els valors. Aquesta mateixa combinació amb histèresi i baixada només donava 95,767 % en l’ajust curt.

El guany és d’uns **0,040 punts respecte del millor ajust anterior** i **0,042 punts respecte de la base d’entrega**. Són resultats de desenvolupament. La configuració nova queda a la branca de combinacions; no he canviat el detector per defecte de l’entrega.

<!-- inici-matriu-combinacions -->
## Matriu de totes les combinacions

Cada fila és una combinació. **✓** vol dir activat i **—** vol dir desactivat.

**Veu** i **Sil.** són les esperes de veu i silenci; **Sor.** és el seguiment del soroll; **Hist.** són els dos llindars; **Pic** deixa fora el pic inicial; **Baix.** permet una baixada; **DC** treu la mitjana; **Ret.** torna al primer bloc pendent.

**Fix** és el TOTAL amb els valors de la base actual. Si activo la histèresi, separo els llindars 1 dB. **Ajust curt** és el resultat de la primera cerca. **Ajust fi** és el millor TOTAL trobat després de provar valors més propers. Per tant, les columnes ajustades poden fer servir paràmetres diferents a cada fila. Els tres resultats són sobre les 115 gravacions de `db.v4`.

La **C225** és la combinació de la base actual. El millor ajust és a **C245**. El número identifica els vuit interruptors en l’ordre de les columnes; les files van de C000 a C255.

| Combinació | Veu | Sil. | Sor. | Hist. | Pic | Baix. | DC | Ret. | Fix (%) | Ajust curt (%) | Ajust fi (%) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---:|---:|---:|
| C000 | — | — | — | — | — | — | — | — | 90,943 | 91,659 | 91,678 |
| C001 | — | — | — | — | — | — | — | ✓ | 90,943 | 91,659 | 91,678 |
| C002 | — | — | — | — | — | — | ✓ | — | 91,063 | 91,612 | 91,612 |
| C003 | — | — | — | — | — | — | ✓ | ✓ | 91,063 | 91,612 | 91,612 |
| C004 | — | — | — | — | — | ✓ | — | — | 90,943 | 91,659 | 91,678 |
| C005 | — | — | — | — | — | ✓ | — | ✓ | 90,943 | 91,659 | 91,678 |
| C006 | — | — | — | — | — | ✓ | ✓ | — | 91,063 | 91,612 | 91,612 |
| C007 | — | — | — | — | — | ✓ | ✓ | ✓ | 91,063 | 91,612 | 91,612 |
| C008 | — | — | — | — | ✓ | — | — | — | 91,180 | 91,638 | 91,674 |
| C009 | — | — | — | — | ✓ | — | — | ✓ | 91,180 | 91,638 | 91,674 |
| C010 | — | — | — | — | ✓ | — | ✓ | — | 91,214 | 91,561 | 91,611 |
| C011 | — | — | — | — | ✓ | — | ✓ | ✓ | 91,214 | 91,561 | 91,611 |
| C012 | — | — | — | — | ✓ | ✓ | — | — | 91,180 | 91,638 | 91,674 |
| C013 | — | — | — | — | ✓ | ✓ | — | ✓ | 91,180 | 91,638 | 91,674 |
| C014 | — | — | — | — | ✓ | ✓ | ✓ | — | 91,214 | 91,561 | 91,611 |
| C015 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,214 | 91,561 | 91,611 |
| C016 | — | — | — | ✓ | — | — | — | — | 91,408 | 92,102 | 92,219 |
| C017 | — | — | — | ✓ | — | — | — | ✓ | 91,408 | 92,102 | 92,219 |
| C018 | — | — | — | ✓ | — | — | ✓ | — | 91,440 | 92,049 | 92,100 |
| C019 | — | — | — | ✓ | — | — | ✓ | ✓ | 91,440 | 92,049 | 92,100 |
| C020 | — | — | — | ✓ | — | ✓ | — | — | 91,408 | 92,102 | 92,219 |
| C021 | — | — | — | ✓ | — | ✓ | — | ✓ | 91,408 | 92,102 | 92,219 |
| C022 | — | — | — | ✓ | — | ✓ | ✓ | — | 91,440 | 92,049 | 92,100 |
| C023 | — | — | — | ✓ | — | ✓ | ✓ | ✓ | 91,440 | 92,049 | 92,100 |
| C024 | — | — | — | ✓ | ✓ | — | — | — | 91,567 | 92,141 | 92,223 |
| C025 | — | — | — | ✓ | ✓ | — | — | ✓ | 91,567 | 92,141 | 92,223 |
| C026 | — | — | — | ✓ | ✓ | — | ✓ | — | 91,524 | 92,019 | 92,108 |
| C027 | — | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,524 | 92,019 | 92,108 |
| C028 | — | — | — | ✓ | ✓ | ✓ | — | — | 91,567 | 92,141 | 92,223 |
| C029 | — | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,567 | 92,141 | 92,223 |
| C030 | — | — | — | ✓ | ✓ | ✓ | ✓ | — | 91,524 | 92,019 | 92,108 |
| C031 | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,524 | 92,019 | 92,108 |
| C032 | — | — | ✓ | — | — | — | — | — | 91,244 | 91,820 | 91,830 |
| C033 | — | — | ✓ | — | — | — | — | ✓ | 91,244 | 91,820 | 91,830 |
| C034 | — | — | ✓ | — | — | — | ✓ | — | 91,257 | 91,759 | 91,769 |
| C035 | — | — | ✓ | — | — | — | ✓ | ✓ | 91,257 | 91,759 | 91,769 |
| C036 | — | — | ✓ | — | — | ✓ | — | — | 91,244 | 91,820 | 91,830 |
| C037 | — | — | ✓ | — | — | ✓ | — | ✓ | 91,244 | 91,820 | 91,830 |
| C038 | — | — | ✓ | — | — | ✓ | ✓ | — | 91,257 | 91,759 | 91,769 |
| C039 | — | — | ✓ | — | — | ✓ | ✓ | ✓ | 91,257 | 91,759 | 91,769 |
| C040 | — | — | ✓ | — | ✓ | — | — | — | 91,371 | 91,843 | 91,867 |
| C041 | — | — | ✓ | — | ✓ | — | — | ✓ | 91,371 | 91,843 | 91,867 |
| C042 | — | — | ✓ | — | ✓ | — | ✓ | — | 91,396 | 91,757 | 91,793 |
| C043 | — | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,396 | 91,757 | 91,793 |
| C044 | — | — | ✓ | — | ✓ | ✓ | — | — | 91,371 | 91,843 | 91,867 |
| C045 | — | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,371 | 91,843 | 91,867 |
| C046 | — | — | ✓ | — | ✓ | ✓ | ✓ | — | 91,396 | 91,757 | 91,793 |
| C047 | — | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,396 | 91,757 | 91,793 |
| C048 | — | — | ✓ | ✓ | — | — | — | — | 91,722 | 92,308 | 92,413 |
| C049 | — | — | ✓ | ✓ | — | — | — | ✓ | 91,722 | 92,308 | 92,413 |
| C050 | — | — | ✓ | ✓ | — | — | ✓ | — | 91,691 | 92,243 | 92,369 |
| C051 | — | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,691 | 92,243 | 92,369 |
| C052 | — | — | ✓ | ✓ | — | ✓ | — | — | 91,722 | 92,308 | 92,413 |
| C053 | — | — | ✓ | ✓ | — | ✓ | — | ✓ | 91,722 | 92,308 | 92,413 |
| C054 | — | — | ✓ | ✓ | — | ✓ | ✓ | — | 91,691 | 92,243 | 92,369 |
| C055 | — | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,691 | 92,243 | 92,369 |
| C056 | — | — | ✓ | ✓ | ✓ | — | — | — | 91,762 | 92,323 | 92,454 |
| C057 | — | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,762 | 92,323 | 92,454 |
| C058 | — | — | ✓ | ✓ | ✓ | — | ✓ | — | 91,752 | 92,269 | 92,342 |
| C059 | — | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,752 | 92,269 | 92,342 |
| C060 | — | — | ✓ | ✓ | ✓ | ✓ | — | — | 91,762 | 92,323 | 92,454 |
| C061 | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,762 | 92,323 | 92,454 |
| C062 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 91,752 | 92,269 | 92,342 |
| C063 | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,752 | 92,269 | 92,342 |
| C064 | — | ✓ | — | — | — | — | — | — | 91,736 | 94,453 | 94,495 |
| C065 | — | ✓ | — | — | — | — | — | ✓ | 94,958 | 95,183 | 95,220 |
| C066 | — | ✓ | — | — | — | — | ✓ | — | 91,539 | 94,430 | 94,449 |
| C067 | — | ✓ | — | — | — | — | ✓ | ✓ | 94,864 | 95,220 | 95,224 |
| C068 | — | ✓ | — | — | — | ✓ | — | — | 91,736 | 94,453 | 94,495 |
| C069 | — | ✓ | — | — | — | ✓ | — | ✓ | 94,958 | 95,183 | 95,220 |
| C070 | — | ✓ | — | — | — | ✓ | ✓ | — | 91,539 | 94,430 | 94,449 |
| C071 | — | ✓ | — | — | — | ✓ | ✓ | ✓ | 94,864 | 95,220 | 95,224 |
| C072 | — | ✓ | — | — | ✓ | — | — | — | 91,093 | 94,373 | 94,450 |
| C073 | — | ✓ | — | — | ✓ | — | — | ✓ | 94,708 | 95,048 | 95,137 |
| C074 | — | ✓ | — | — | ✓ | — | ✓ | — | 90,757 | 94,290 | 94,384 |
| C075 | — | ✓ | — | — | ✓ | — | ✓ | ✓ | 94,614 | 95,207 | 95,211 |
| C076 | — | ✓ | — | — | ✓ | ✓ | — | — | 91,093 | 94,373 | 94,450 |
| C077 | — | ✓ | — | — | ✓ | ✓ | — | ✓ | 94,708 | 95,048 | 95,137 |
| C078 | — | ✓ | — | — | ✓ | ✓ | ✓ | — | 90,757 | 94,290 | 94,384 |
| C079 | — | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 94,614 | 95,207 | 95,211 |
| C080 | — | ✓ | — | ✓ | — | — | — | — | 91,157 | 94,460 | 94,512 |
| C081 | — | ✓ | — | ✓ | — | — | — | ✓ | 94,519 | 95,295 | 95,299 |
| C082 | — | ✓ | — | ✓ | — | — | ✓ | — | 90,941 | 94,404 | 94,464 |
| C083 | — | ✓ | — | ✓ | — | — | ✓ | ✓ | 94,378 | 95,247 | 95,259 |
| C084 | — | ✓ | — | ✓ | — | ✓ | — | — | 91,157 | 94,460 | 94,512 |
| C085 | — | ✓ | — | ✓ | — | ✓ | — | ✓ | 94,519 | 95,295 | 95,299 |
| C086 | — | ✓ | — | ✓ | — | ✓ | ✓ | — | 90,941 | 94,404 | 94,464 |
| C087 | — | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 94,378 | 95,247 | 95,259 |
| C088 | — | ✓ | — | ✓ | ✓ | — | — | — | 90,403 | 94,353 | 94,464 |
| C089 | — | ✓ | — | ✓ | ✓ | — | — | ✓ | 94,184 | 95,129 | 95,131 |
| C090 | — | ✓ | — | ✓ | ✓ | — | ✓ | — | 90,095 | 94,275 | 94,399 |
| C091 | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 94,006 | 95,167 | 95,169 |
| C092 | — | ✓ | — | ✓ | ✓ | ✓ | — | — | 90,403 | 94,353 | 94,464 |
| C093 | — | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 94,184 | 95,129 | 95,131 |
| C094 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 90,095 | 94,275 | 94,399 |
| C095 | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,006 | 95,167 | 95,169 |
| C096 | — | ✓ | ✓ | — | — | — | — | — | 91,097 | 94,592 | 94,627 |
| C097 | — | ✓ | ✓ | — | — | — | — | ✓ | 94,871 | 95,401 | 95,450 |
| C098 | — | ✓ | ✓ | — | — | — | ✓ | — | 90,939 | 94,598 | 94,619 |
| C099 | — | ✓ | ✓ | — | — | — | ✓ | ✓ | 94,792 | 95,381 | 95,416 |
| C100 | — | ✓ | ✓ | — | — | ✓ | — | — | 91,097 | 94,592 | 94,627 |
| C101 | — | ✓ | ✓ | — | — | ✓ | — | ✓ | 94,871 | 95,401 | 95,450 |
| C102 | — | ✓ | ✓ | — | — | ✓ | ✓ | — | 90,939 | 94,598 | 94,619 |
| C103 | — | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 94,792 | 95,381 | 95,416 |
| C104 | — | ✓ | ✓ | — | ✓ | — | — | — | 90,727 | 94,535 | 94,579 |
| C105 | — | ✓ | ✓ | — | ✓ | — | — | ✓ | 94,696 | 95,332 | 95,383 |
| C106 | — | ✓ | ✓ | — | ✓ | — | ✓ | — | 90,528 | 94,456 | 94,521 |
| C107 | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 94,614 | 95,345 | 95,433 |
| C108 | — | ✓ | ✓ | — | ✓ | ✓ | — | — | 90,727 | 94,535 | 94,579 |
| C109 | — | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 94,696 | 95,332 | 95,383 |
| C110 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 90,528 | 94,456 | 94,521 |
| C111 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 94,614 | 95,345 | 95,433 |
| C112 | — | ✓ | ✓ | ✓ | — | — | — | — | 90,366 | 94,649 | 94,660 |
| C113 | — | ✓ | ✓ | ✓ | — | — | — | ✓ | 94,324 | 95,257 | 95,409 |
| C114 | — | ✓ | ✓ | ✓ | — | — | ✓ | — | 90,297 | 94,626 | 94,636 |
| C115 | — | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 94,288 | 95,539 | 95,572 |
| C116 | — | ✓ | ✓ | ✓ | — | ✓ | — | — | 90,366 | 94,649 | 94,660 |
| C117 | — | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 94,324 | 95,257 | 95,409 |
| C118 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 90,297 | 94,626 | 94,636 |
| C119 | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 94,288 | 95,539 | 95,572 |
| C120 | — | ✓ | ✓ | ✓ | ✓ | — | — | — | 89,891 | 94,549 | 94,607 |
| C121 | — | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 94,044 | 95,394 | 95,480 |
| C122 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 89,799 | 94,550 | 94,622 |
| C123 | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 93,989 | 95,480 | 95,525 |
| C124 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 89,891 | 94,549 | 94,607 |
| C125 | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 94,044 | 95,394 | 95,480 |
| C126 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 89,799 | 94,550 | 94,622 |
| C127 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 93,989 | 95,480 | 95,525 |
| C128 | ✓ | — | — | — | — | — | — | — | 80,661 | 88,230 | 90,844 |
| C129 | ✓ | — | — | — | — | — | — | ✓ | 90,494 | 92,030 | 92,044 |
| C130 | ✓ | — | — | — | — | — | ✓ | — | 81,005 | 88,263 | 90,851 |
| C131 | ✓ | — | — | — | — | — | ✓ | ✓ | 90,686 | 91,974 | 92,086 |
| C132 | ✓ | — | — | — | — | ✓ | — | — | 80,866 | 88,288 | 90,843 |
| C133 | ✓ | — | — | — | — | ✓ | — | ✓ | 90,779 | 92,107 | 92,165 |
| C134 | ✓ | — | — | — | — | ✓ | ✓ | — | 81,192 | 88,345 | 90,831 |
| C135 | ✓ | — | — | — | — | ✓ | ✓ | ✓ | 90,919 | 91,975 | 92,164 |
| C136 | ✓ | — | — | — | ✓ | — | — | — | 81,358 | 88,478 | 90,954 |
| C137 | ✓ | — | — | — | ✓ | — | — | ✓ | 90,822 | 92,138 | 92,218 |
| C138 | ✓ | — | — | — | ✓ | — | ✓ | — | 81,585 | 88,547 | 90,858 |
| C139 | ✓ | — | — | — | ✓ | — | ✓ | ✓ | 90,957 | 92,087 | 92,108 |
| C140 | ✓ | — | — | — | ✓ | ✓ | — | — | 81,510 | 88,522 | 90,949 |
| C141 | ✓ | — | — | — | ✓ | ✓ | — | ✓ | 91,071 | 92,236 | 92,244 |
| C142 | ✓ | — | — | — | ✓ | ✓ | ✓ | — | 81,722 | 88,611 | 90,871 |
| C143 | ✓ | — | — | — | ✓ | ✓ | ✓ | ✓ | 91,157 | 92,145 | 92,152 |
| C144 | ✓ | — | — | ✓ | — | — | — | — | 81,639 | 89,508 | 91,634 |
| C145 | ✓ | — | — | ✓ | — | — | — | ✓ | 90,971 | 92,821 | 92,875 |
| C146 | ✓ | — | — | ✓ | — | — | ✓ | — | 81,810 | 89,463 | 91,523 |
| C147 | ✓ | — | — | ✓ | — | — | ✓ | ✓ | 91,066 | 92,658 | 92,820 |
| C148 | ✓ | — | — | ✓ | — | ✓ | — | — | 81,824 | 89,515 | 91,573 |
| C149 | ✓ | — | — | ✓ | — | ✓ | — | ✓ | 91,241 | 92,835 | 92,894 |
| C150 | ✓ | — | — | ✓ | — | ✓ | ✓ | — | 81,995 | 89,471 | 91,521 |
| C151 | ✓ | — | — | ✓ | — | ✓ | ✓ | ✓ | 91,305 | 92,721 | 92,958 |
| C152 | ✓ | — | — | ✓ | ✓ | — | — | — | 82,163 | 89,649 | 91,611 |
| C153 | ✓ | — | — | ✓ | ✓ | — | — | ✓ | 91,276 | 92,883 | 92,953 |
| C154 | ✓ | — | — | ✓ | ✓ | — | ✓ | — | 82,327 | 89,525 | 91,487 |
| C155 | ✓ | — | — | ✓ | ✓ | — | ✓ | ✓ | 91,368 | 92,697 | 92,800 |
| C156 | ✓ | — | — | ✓ | ✓ | ✓ | — | — | 82,307 | 89,642 | 91,552 |
| C157 | ✓ | — | — | ✓ | ✓ | ✓ | — | ✓ | 91,513 | 92,921 | 93,008 |
| C158 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | — | 82,455 | 89,472 | 91,477 |
| C159 | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | 91,555 | 92,774 | 92,837 |
| C160 | ✓ | — | ✓ | — | — | — | — | — | 80,970 | 88,794 | 91,104 |
| C161 | ✓ | — | ✓ | — | — | — | — | ✓ | 90,779 | 92,366 | 92,486 |
| C162 | ✓ | — | ✓ | — | — | — | ✓ | — | 81,134 | 88,870 | 91,111 |
| C163 | ✓ | — | ✓ | — | — | — | ✓ | ✓ | 90,871 | 92,389 | 92,433 |
| C164 | ✓ | — | ✓ | — | — | ✓ | — | — | 81,199 | 88,835 | 91,059 |
| C165 | ✓ | — | ✓ | — | — | ✓ | — | ✓ | 91,072 | 92,471 | 92,491 |
| C166 | ✓ | — | ✓ | — | — | ✓ | ✓ | — | 81,390 | 88,860 | 91,041 |
| C167 | ✓ | — | ✓ | — | — | ✓ | ✓ | ✓ | 91,179 | 92,398 | 92,454 |
| C168 | ✓ | — | ✓ | — | ✓ | — | — | — | 81,348 | 88,913 | 91,145 |
| C169 | ✓ | — | ✓ | — | ✓ | — | — | ✓ | 90,998 | 92,434 | 92,517 |
| C170 | ✓ | — | ✓ | — | ✓ | — | ✓ | — | 81,520 | 88,904 | 91,031 |
| C171 | ✓ | — | ✓ | — | ✓ | — | ✓ | ✓ | 91,127 | 92,375 | 92,434 |
| C172 | ✓ | — | ✓ | — | ✓ | ✓ | — | — | 81,600 | 88,958 | 91,136 |
| C173 | ✓ | — | ✓ | — | ✓ | ✓ | — | ✓ | 91,338 | 92,522 | 92,540 |
| C174 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | — | 81,776 | 88,926 | 90,958 |
| C175 | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | 91,446 | 92,389 | 92,504 |
| C176 | ✓ | — | ✓ | ✓ | — | — | — | — | 82,020 | 89,818 | 91,662 |
| C177 | ✓ | — | ✓ | ✓ | — | — | — | ✓ | 91,354 | 93,014 | 93,126 |
| C178 | ✓ | — | ✓ | ✓ | — | — | ✓ | — | 82,065 | 89,775 | 91,621 |
| C179 | ✓ | — | ✓ | ✓ | — | — | ✓ | ✓ | 91,362 | 92,961 | 93,010 |
| C180 | ✓ | — | ✓ | ✓ | — | ✓ | — | — | 82,236 | 89,658 | 91,728 |
| C181 | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | 91,618 | 93,064 | 93,145 |
| C182 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | — | 82,313 | 89,828 | 91,655 |
| C183 | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | 91,666 | 92,978 | 93,095 |
| C184 | ✓ | — | ✓ | ✓ | ✓ | — | — | — | 82,292 | 89,784 | 91,737 |
| C185 | ✓ | — | ✓ | ✓ | ✓ | — | — | ✓ | 91,499 | 93,047 | 93,218 |
| C186 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | — | 82,370 | 89,863 | 91,591 |
| C187 | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | ✓ | 91,584 | 92,985 | 93,107 |
| C188 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | — | 82,505 | 89,878 | 91,680 |
| C189 | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | 91,792 | 93,090 | 93,121 |
| C190 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | — | 82,550 | 89,815 | 91,655 |
| C191 | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 91,834 | 92,999 | 93,101 |
| C192 | ✓ | ✓ | — | — | — | — | — | — | 88,655 | 92,310 | 94,017 |
| C193 | ✓ | ✓ | — | — | — | — | — | ✓ | 95,592 | 95,628 | 95,640 |
| C194 | ✓ | ✓ | — | — | — | — | ✓ | — | 88,490 | 92,258 | 93,946 |
| C195 | ✓ | ✓ | — | — | — | — | ✓ | ✓ | 95,516 | 95,542 | 95,566 |
| C196 | ✓ | ✓ | — | — | — | ✓ | — | — | 88,732 | 92,338 | 94,013 |
| C197 | ✓ | ✓ | — | — | — | ✓ | — | ✓ | 95,621 | 95,667 | 95,679 |
| C198 | ✓ | ✓ | — | — | — | ✓ | ✓ | — | 88,575 | 92,267 | 93,949 |
| C199 | ✓ | ✓ | — | — | — | ✓ | ✓ | ✓ | 95,532 | 95,579 | 95,604 |
| C200 | ✓ | ✓ | — | — | ✓ | — | — | — | 88,438 | 92,306 | 94,002 |
| C201 | ✓ | ✓ | — | — | ✓ | — | — | ✓ | 95,478 | 95,608 | 95,608 |
| C202 | ✓ | ✓ | — | — | ✓ | — | ✓ | — | 88,289 | 92,244 | 93,615 |
| C203 | ✓ | ✓ | — | — | ✓ | — | ✓ | ✓ | 95,409 | 95,552 | 95,556 |
| C204 | ✓ | ✓ | — | — | ✓ | ✓ | — | — | 88,475 | 92,309 | 93,991 |
| C205 | ✓ | ✓ | — | — | ✓ | ✓ | — | ✓ | 95,472 | 95,567 | 95,588 |
| C206 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | — | 88,346 | 92,244 | 93,571 |
| C207 | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ | 95,418 | 95,567 | 95,581 |
| C208 | ✓ | ✓ | — | ✓ | — | — | — | — | 88,155 | 92,286 | 94,036 |
| C209 | ✓ | ✓ | — | ✓ | — | — | — | ✓ | 95,317 | 95,677 | 95,680 |
| C210 | ✓ | ✓ | — | ✓ | — | — | ✓ | — | 87,936 | 92,264 | 93,715 |
| C211 | ✓ | ✓ | — | ✓ | — | — | ✓ | ✓ | 95,086 | 95,584 | 95,615 |
| C212 | ✓ | ✓ | — | ✓ | — | ✓ | — | — | 88,242 | 92,319 | 93,784 |
| C213 | ✓ | ✓ | — | ✓ | — | ✓ | — | ✓ | 95,356 | 95,685 | 95,688 |
| C214 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | — | 88,034 | 92,275 | 93,749 |
| C215 | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | ✓ | 95,118 | 95,618 | 95,681 |
| C216 | ✓ | ✓ | — | ✓ | ✓ | — | — | — | 87,854 | 92,355 | 93,788 |
| C217 | ✓ | ✓ | — | ✓ | ✓ | — | — | ✓ | 95,114 | 95,593 | 95,595 |
| C218 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | — | 87,706 | 92,251 | 93,627 |
| C219 | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | ✓ | 94,952 | 95,542 | 95,542 |
| C220 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | — | 87,906 | 92,322 | 93,735 |
| C221 | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | ✓ | 95,122 | 95,613 | 95,650 |
| C222 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | 87,763 | 92,229 | 93,566 |
| C223 | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | 94,963 | 95,595 | 95,604 |
| C224 | ✓ | ✓ | ✓ | — | — | — | — | — | 88,680 | 92,488 | 94,126 |
| **C225 · base** | ✓ | ✓ | ✓ | — | — | — | — | ✓ | 95,829 | 95,829 | 95,829 |
| C226 | ✓ | ✓ | ✓ | — | — | — | ✓ | — | 88,554 | 92,477 | 94,177 |
| C227 | ✓ | ✓ | ✓ | — | — | — | ✓ | ✓ | 95,771 | 95,831 | 95,832 |
| C228 | ✓ | ✓ | ✓ | — | — | ✓ | — | — | 88,674 | 92,500 | 94,124 |
| C229 | ✓ | ✓ | ✓ | — | — | ✓ | — | ✓ | 95,791 | 95,813 | 95,833 |
| C230 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | — | 88,604 | 92,495 | 94,192 |
| C231 | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | 95,798 | 95,819 | 95,825 |
| C232 | ✓ | ✓ | ✓ | — | ✓ | — | — | — | 88,504 | 92,447 | 94,102 |
| C233 | ✓ | ✓ | ✓ | — | ✓ | — | — | ✓ | 95,669 | 95,747 | 95,760 |
| C234 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | — | 88,385 | 92,402 | 94,131 |
| C235 | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | ✓ | 95,687 | 95,714 | 95,731 |
| C236 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | — | 88,571 | 92,415 | 94,108 |
| C237 | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | ✓ | 95,679 | 95,739 | 95,767 |
| C238 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | — | 88,479 | 92,403 | 94,133 |
| C239 | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | 95,721 | 95,755 | 95,773 |
| C240 | ✓ | ✓ | ✓ | ✓ | — | — | — | — | 88,057 | 92,576 | 94,020 |
| C241 | ✓ | ✓ | ✓ | ✓ | — | — | — | ✓ | 95,512 | 95,814 | 95,825 |
| C242 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | — | 87,916 | 92,546 | 93,926 |
| C243 | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | 95,314 | 95,749 | 95,856 |
| C244 | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | — | 87,989 | 92,533 | 93,930 |
| **C245 · millor ajust** | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | ✓ | 95,430 | 95,767 | **95,871** |
| C246 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | — | 88,008 | 92,572 | 93,961 |
| C247 | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | 95,364 | 95,828 | 95,867 |
| C248 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | 87,847 | 92,524 | 93,939 |
| C249 | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | ✓ | 95,256 | 95,758 | 95,760 |
| C250 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | — | 87,851 | 92,555 | 93,873 |
| C251 | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | 95,182 | 95,760 | 95,801 |
| C252 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | 87,906 | 92,523 | 93,922 |
| C253 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | 95,269 | 95,767 | 95,780 |
| C254 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | 87,956 | 92,471 | 94,117 |
| C255 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 95,223 | 95,812 | 95,857 |

Els paràmetres concrets de cada ajust són al [CSV de combinacions ajustades](https://github.com/victor836768/P2/blob/jordi-albareda-combinacions/resultats/combinacions/combinacions_ajustades.csv). Algunes files donen el mateix perquè hi ha idees que no fan res si una altra està desactivada.
<!-- final-matriu-combinacions -->

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
- `resultats/combinacions/combinacions_abans_afinament.csv`: el primer ajust, per poder comparar.
- `resultats/combinacions/combinacions_ajustades.csv`: el millor trobat després d’afinar per a cadascun dels 256 grups.
- `resultats/combinacions/afinament_detall.csv`: els valors propers que he provat i la seva puntuació.
- `resultats/combinacions/verificacio.csv`: comparació amb el programa normal i el Perl.
- `resultats/combinacions/avaluacio_millor.txt`: resultat complet de la millor configuració trobada.

Les tres proves inicials per separat també es conserven a `jordi-albareda-prova-soroll`, `jordi-albareda-prova-baixada` i `jordi-albareda-prova-dc`.

## Altres coses del treball

He dibuixat el ZCR i he calculat l’amplitud mitjana, però no hi ha cap regla del detector que els faci servir. Per això no els poso com si fossin mètodes ja provats. Afegir-los com a decisió seria una prova nova.

Les opcions de `docopt_c`, `cardem-li`, els rànquings i les gràfiques ajuden a fer i explicar les proves. No són canvis en la manera de detectar veu. Tampoc he implementat la cancel·lació del silenci.

La lectura correcta del fitxer, la durada final, les etiquetes S/V i el tractament dels errors es mantenen a totes les proves. No els desactivo per intentar pujar la puntuació.
