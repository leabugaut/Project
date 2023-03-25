#!/bin/bash

pop=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp1">)[\d,]+(?=</div>)' | sed 's/,/./g')
pop_m=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp2">)[\d,]+(?=</div>)' | sed 's/,/./g')
pop_f=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp3">)[\d,]+(?=</div>)' | sed 's/,/./g')

# pour le rapport
# naissances depuis l'année dernière 
bytd=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp6">)[\d,]+(?=</div>)' | sed 's/,/./g')
btoday=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp7">)[\d,]+(?=</div>)' | sed 's/,/./g')
# morts depuis l'année dernière
dytd=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp8">)[\d,]+(?=</div>)' | sed 's/,/./g')
dtoday=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp9">)[\d,]+(?=</div>)' | sed 's/,/./g')
# migration depuis l'année dernière
mytd=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp10">)[\d,]+(?=</div>)' | sed 's/,/./g')
# migrations aujourd'hui
mtoday=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp11">)[\d,]+(?=</div>)' | sed 's/,/./g')
# population growth year to date
pgytd=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp12">)[\d,]+(?=</div>)' | sed 's/,/./g')
# population growth today
pop_growth=$(curl -s https://countrymeters.info/en/France | grep -Po '(?<=<div id="cp13">)[\d,]+(?=</div>)' | sed 's/,/./g')


timestamp=$(date +%s)

#  nom du fichier CSV
CSV_FILE="/home/ubuntu/Project/data.csv"

#  si le fichier CSV est vide
if [ ! -s "$CSV_FILE" ]; then
  # Ajoutez les noms des colonnes si le fichier est vide
  echo "timestamp,pop,pop_m,pop_f,bytd,btoday,dytd,dtoday,mytd,mtoday,pgytd,pop_growth" > $CSV_FILE
fi

echo $timestamp,$pop,$pop_m,$pop_f,$bytd,$btoday,$dytd,$dtoday,$mytd,$mtoday,$pgytd,$pop_growth >> $CSV_FILE

