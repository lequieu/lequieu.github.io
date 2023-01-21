#!/bin/bash
if [ $# -ne 4 ]; then
    echo "Usage: $0 <file> <row> <col> <val>"
    exit
fi

cmd="awk -v row=$2 -v col=$3 'FNR==1{} FNR==row{\$col="$4"}1' ./$1 > mytmp.dat; mv mytmp.dat $1"
echo $cmd
eval $cmd
