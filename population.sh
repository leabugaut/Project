#!/bin/bash

pop=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp1">)[\d,]+(?=</div>)' | sed 's/,/./g')
pop_m=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp2">)[\d,]+(?=</div>)' | sed 's/,/./g')
pop_f=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp3">)[\d,]+(?=</div>)' | sed 's/,/./g')


timestamp=$(date +%s)

#  nom du fichier CSV
CSV_FILE="/home/ubuntu/Project/data.csv"

#  si le fichier CSV est vide
if [ ! -s "$CSV_FILE" ]; then
  # Ajoutez les noms des colonnes si le fichier est vide
  echo "timestamp,pop,pop_m,pop_f" > $CSV_FILE
fi

echo $timestamp,$pop,$pop_m,$pop_f >> $CSV_FILE

