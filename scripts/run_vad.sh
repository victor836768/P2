#!/bin/bash
# Aturo el procés si falla el detector o l'avaluació.
set -e
set -o pipefail

# Localitzo P2 a partir del directori d'aquest script.
DIR_P2="$(cd "$(dirname "$0")/.." && pwd)"
DB="$DIR_P2/db.v4"
CMD="$DIR_P2/bin/vad"
llindar="${1:-6}" # Faig servir el primer argument o el valor per defecte de 6 dB.
if [[ $# -gt 1 || ! "$llindar" =~ ^[0-9]+([.][0-9]+)?$ ]]; then
    echo "Ús: $0 [marge_en_dB]" >&2 # Indico com passar el marge.
    exit 1
fi
OUT="$DIR_P2/resultats/db/llindar_$llindar" # Separo els fitxers de cada prova.

# Comprovo que he compilat el programa abans d'avaluar-lo.
if [[ ! -x "$CMD" ]]; then
    echo "Primer executa: meson setup bin; ninja -C bin" >&2
    exit 1
fi

# Creo la carpeta on guardaré l'avaluació.
mkdir -p "$DIR_P2/resultats"

# Recorro les carpetes i copio les referències una sola vegada per grup.
gravacions=0 # Comprovo que realment hagi analitzat algun fitxer.
for groupdir in "$DB"/*; do
    [[ -d "$groupdir" ]] || continue # Salto els elements que no són carpetes.
    group="${groupdir##*/}" # Obtinc el nom de la carpeta amb Bash.
    mkdir -p "$OUT/$group" # Creo el directori una sola vegada per grup.
    cp "$groupdir"/*.lab "$OUT/$group/" # Copio les referències sense modificar-les.
    for filewav in "$groupdir"/*.wav; do # Analitzo totes les gravacions del grup.
        if [[ ! -f "$filewav" ]]; then
            echo "No he trobat àudio a $groupdir" >&2
            exit 1
        fi
        name="${filewav##*/}" # Retiro el camí del fitxer.
        name="${name%.wav}" # Retiro l'extensió.
        filevad="$OUT/$group/$name.vad" # Indico on guardaré la predicció.
        "$CMD" -i "$filewav" -o "$filevad" -l "$llindar" # Passo el marge al detector.
        gravacions=$((gravacions + 1)) # Compto aquesta gravació.
    done
done

if [[ $gravacions -eq 0 ]]; then
    echo "No he trobat la base de dades a $DB" >&2 # Evito avaluar resultats antics si no hi ha àudio.
    exit 1
fi

# Comparo amb les etiquetes originals i deso el resultat complet.
perl "$DIR_P2/scripts/vad_evaluation.pl" "$OUT"/*/*.lab | tee "$DIR_P2/resultats/evaluacio_llindar_$llindar.txt"
