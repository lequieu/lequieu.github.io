#!/bin/bash

# Loop through all codesnips and do the following

for i in *.snip; do
  echo $i

  oldfile=$i
  newfile=$i
  # replace <code> with <pre> and </code> with </pre>
  sed -e 's:<code>:<pre>:g' -e 's:</code>:</pre>:g' < $oldfile > tmp


  # remove all whitespace in front of text between <pre> and </pre>
  #awk 'BEGIN{flag=0} {if ($1 == "<code>") {flag=1}  if (flag==1) {$1=$1; print;} else {print}; if ($1 == "</code>") flag=0;}'  tmp > tmp2
  awk 'BEGIN{flag=0} {if ($1 == "<pre>") {flag=1}  if (flag==1) {$1=$1; print;} else {print}; if ($1 == "</pre>") flag=0;}'  tmp > tmp2
    
    
  mv tmp2 $newfile
  rm tmp

done
