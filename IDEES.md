# Idees que he fet servir a P2

## Com funciona la versió que tinc ara

- Llegeixo l’àudio en blocs de 10 ms.
- Calculo la potència de cada bloc. És una manera de mirar si el so és fort o fluix.
- Faig servir els primers 90 ms per calcular el soroll del començament.
- Si la potència passa de soroll + 5,94 dB, pot ser veu.
- Espero 80 ms de veu abans de confirmar-la. Així evito donar per bona una punta molt curta.
- Espero 170 ms de silenci abans de tallar la veu. Així no tallo una paraula per una pausa curta.
- Quan hi ha silenci, vaig canviant el valor del soroll a poc a poc. Faig servir `soroll += 0.00615 * (potència - soroll)`.
- Quan confirmo un canvi, poso el límit al primer bloc que havia deixat pendent.
- El tros final que no omple un bloc també queda dins del fitxer de sortida.

No necessito llegir tot l’àudio de cop. Guardo un bloc i uns quants nombres. Les etiquetes que ha fet una persona només les faig servir després, per comprovar si el programa ho ha fet bé.

## Coses que ja havia provat

Vaig anar canviant el marge, el temps inicial, les duracions mínimes i la velocitat amb què canvia el soroll. La primera versió donava 95,474 %. Canviant només el marge vaig arribar a 95,653 %. Després vaig provar els cinc valors junts i vaig arribar a 95,829 %.

També havia provat dos llindars: un per començar la veu i un altre per acabar-la. Amb 6 i 5 dB donava 95,376 %, per sota del 95,474 % de la base d’aquell moment. Per això no ho vaig afegir.

He dibuixat els creuaments per zero per mirar-los, però no els faig servir per decidir. No sempre separen bé la veu del soroll.

## Tres proves noves, cadascuna pel seu costat

Les tres surten de la mateixa versió, `ac4e32a`. No he canviat el marge ni els altres valors. Així puc veure què passa quan canvio només una cosa.

### 1. Treure el bloc més fort del començament

Si hi ha un cop al principi, pot semblar que el soroll normal és molt alt. Provo de deixar fora el bloc més fort dels nou primers i fer la mitjana dels altres vuit.

Només guardo el màxim i la suma dels altres. Quan arriba un màxim nou, el màxim anterior passa a la suma. No cal guardar els nou blocs.

La prova amb un cop funciona, però amb tota la base de dades el TOTAL baixa a **95,669 %**. Detecta una mica més de veu, però també confon més soroll amb veu. No ho afegeixo a la base.

Branca: [jordi-albareda-prova-soroll](https://github.com/victor836768/P2/tree/jordi-albareda-prova-soroll).

### 2. Permetre una baixada curta mentre comença la veu

Abans, qualsevol bloc baix feia començar de zero el recompte de veu. Provo de permetre un sol bloc baix de 10 ms.

Continuo demanant vuit blocs alts. El bloc baix no compta entre els vuit blocs alts. Si confirmo la veu, queda dins del mateix segment. Si apareix una segona baixada abans de confirmar la veu, descarto l’intent. Per tant, la confirmació tarda 80 ms sense baixada o 90 ms amb una baixada.

A la gravació personal passa de 98,335 % a **99,014 %**. Però amb tota la base dona **95,791 %**, una mica menys que la versió actual. La deixo com a prova.

Branca: [jordi-albareda-prova-baixada](https://github.com/victor836768/P2/tree/jordi-albareda-prova-baixada).

### 3. Treure el valor mitjà abans de calcular la potència

De vegades el senyal pot estar una mica desplaçat respecte de zero. Provo de fer la mitjana de cada bloc i restar-la de les mostres abans de calcular-ne la potència.

No canvio les mostres de l’àudio original. Només canvio el càlcul de la potència. No hi ha filtres nous.

A la prova amb un valor constant funciona. Amb tota la base dona **95,771 %**, també una mica menys. La deixo separada.

Branca: [jordi-albareda-prova-dc](https://github.com/victor836768/P2/tree/jordi-albareda-prova-dc).

## Resultats de les proves

| Versió | Sensibilitat de veu | Precisió de veu | TOTAL de db.v4 | Gravació personal |
|---|---:|---:|---:|---:|
| Base actual | 98,08 % | 92,54 % | **95,829 %** | 98,335 % |
| Sense el pic inicial | 98,15 % | 91,90 % | 95,669 % | 98,416 % |
| Una baixada curta | 98,17 % | 92,17 % | 95,791 % | **99,014 %** |
| Sense el valor mitjà | 98,20 % | 92,05 % | 95,771 % | 98,460 % |

La sensibilitat diu quanta veu trobo. La precisió diu quina part del que marco com a veu ho és de veritat. El TOTAL és la puntuació que calcula el programa de la pràctica. Miro aquest resultat per comparar les versions.

Les tres proves troben una mica més de veu, però també marquen una mica més de soroll com a veu. Amb aquests valors, **mantinc la base actual**. Que una idea sembli bona no vol dir que millori el resultat.

## Com ho he comprovat

He compilat cada branca des de zero i he passat les mateixes 115 gravacions a cadascuna. He fet servir el mateix `vad_evaluation.pl`, sense tocar les referències. També he comprovat la gravació personal.

A més, he fet àudios petits a 8, 16 i 48 kHz: silenci, un cop al principi, una o dues baixades i un senyal desplaçat respecte de zero. A cada branca comprovo el cas que correspon al seu canvi.

No he tornat a ajustar els paràmetres de cada prova ni he combinat les tres idees. Les gravacions de `db.v4` ja s’havien fet servir per ajustar la base. Per tant, aquests resultats no ens diuen com anirà amb àudios nous.
