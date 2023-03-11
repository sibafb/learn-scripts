#!/bin/bash

# 現在時刻を文字列で取得する - シェルスクリプト
# https://keruu.netlify.app/1384f6c44240b788416f1128d81f7d08/

DATE=`date`
echo $DATE

DATETOKYO=`TZ='Asia/Tokyo' date`
echo $DATETOKYO

DATEYMD=`date '+%Y-%m-%d'`
echo $DATEYMD"day!"

echo "Hello" >> $DATETMD"file.txt"