#!/bin/bash

echo "Building html for joshlequieu.com"
SNIPS="."
ROOT="../"

#cat $SNIPS/header.snip $SNIPS/stats-end.snip > $ROOT/index.html

for i in codesnips ; do
  cat $SNIPS/header.snip $SNIPS/$i.snip $SNIPS/footer.snip $SNIPS/stats-end.snip > $ROOT/$i.html
done
