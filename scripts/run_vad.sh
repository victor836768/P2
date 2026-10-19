#!/bin/bash
# Aturo el procés si falla el detector o l'avaluació.
set -e
set -o pipefail

# Localitzo P2 a partir del directori d'aquest script.
DIR_P2="$(cd "$(dirname "$0")/.." && pwd)"
DB="$DIR_P2/db.v4"
CMD="$DIR_P2/bin/vad"
OUT="$DIR_P2/resultats/db" # Separo les prediccions de la base de dades original.

# Comprovo que he compilat el programa abans d'avaluar-lo.
if [[ ! -x "$CMD" ]]; then
    echo "Primer executa: meson setup bin; ninja -C bin" >&2
    exit 1
fi

# Creo la carpeta on guardaré l'avaluació.
mkdir -p "$DIR_P2/resultats"

# Genero un .vad per a cada gravació de la base de dades.
for filewav in "$DB"/*/*.wav; do
    if [[ ! -f "$filewav" ]]; then
        echo "No he trobat la base de dades a $DB" >&2
        exit 1
    fi
    group="$(basename "$(dirname "$filewav")")" # Conservo el nom del grup de gravacions.
    name="$(basename "${filewav%.wav}")" # Obtinc el nom sense extensió.
    mkdir -p "$OUT/$group" # Creo el directori dels resultats d'aquest grup.
    cp "${filewav%.wav}.lab" "$OUT/$group/$name.lab" # Copio la referència sense modificar-la.
    filevad="$OUT/$group/$name.vad" # Indico on guardaré la predicció.
    "$CMD" -i "$filewav" -o "$filevad"
done

# Comparo amb les etiquetes originals i deso el resultat complet.
perl "$DIR_P2/scripts/vad_evaluation.pl" "$OUT"/*/*.lab | tee "$DIR_P2/resultats/evaluacio_db.txt"
