#/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <input file> <output file>"
    exit
fi

# from http://stackoverflow.com/questions/1729824/transpose-a-file-in-bash
#awk 'BEGIN { FS=OFS="\t" }
#{
#    for (rowNr=1;rowNr<=NF;rowNr++) {
#        cell[rowNr,NR] = $rowNr
#    }
#    maxRows = (NF > maxRows ? NF : maxRows)
#    maxCols = NR
#}
#END {
#    for (rowNr=1;rowNr<=maxRows;rowNr++) {
#        for (colNr=1;colNr<=maxCols;colNr++) {
#            printf "%s%s", cell[rowNr,colNr], (colNr < maxCols ? OFS : ORS)
#        }
#    }
#}' $1 >$2

awk '
{ 
    for (i=1; i<=NF; i++)  {
        a[NR,i] = $i
    }
}
NF>p { p = NF }
END {    
    for(j=1; j<=p; j++) {
        str=a[1,j]
        for(i=2; i<=NR; i++){
            str=str" "a[i,j];
        }
        print str
    }
}' $1 >$2
