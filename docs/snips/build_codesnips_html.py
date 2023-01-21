#!/usr/bin/python

import os

wdir="./codesnips" # where *.snip files are located

#newdir="../codesnips" # where new .html files are written to
#if not os.path.exists(newdir):
#    os.makedirs(newdir)

class Codesnip:
  def __init__(self,heading,tag):
    self.heading=heading
    self.tag=tag # basename of snipfile, used for internal references
    self.snipfile= wdir + "/" + tag + ".snip" #file ending in .snip
    #self.htmlfile= newdir + "/" + tag + ".html" #file ending in .html

  def display(self):
    print "%s %s" % (self.heading,self.htmlfile)

def AppendFileIntoFile(readfilename, writefile):
  fin = open(readfilename,'r')
  for line in fin:
      writefile.write("%s" % line)
  fin.close()

preamble='''
    <section class="content container">
    <h1> Codesnips </h1>
    
    <p>
    This page organizes various pieces of code or tips that I've learned along a way while working in a scientific computing environment.
    They're mostly for my own reference and are strongly biased toward the tools that I use and the types of simulations and pre/post processing I tend to perform.
    Nonetheless, I hope they're useful to anyone who works regularly at the command line.
    </p>

'''

inputfile="%s/config" % wdir
header="header.snip"
footer="footer.snip"
statsend="stats-end.snip"

codesnips=[];

f = open(inputfile,'r')
for line in f:
   if line[0] == '#':
     continue;

   l=line.split() 
   if len(l) != 2:
     print "Ignoring Line \"%s\". Expected only two arguments" % line
   else:
     # put into a struct
     codesnips.append(Codesnip(l[0],l[1]))
f.close()


# ============================================
# write codesnips.html
# ============================================

fnme = "./codesnips.html"
f = open (fnme,"w")

# write header
AppendFileIntoFile(header, f)

# write initial content
f.write(preamble) 

f.write("<h2> Table of Contents </h2>\n")
f.write("<ul>\n")
# Link to other codesnips files
for codesnip in codesnips:
  line = "<li> <a href=\"#%s\">%s</a> </li>\n" % (codesnip.tag, codesnip.heading)
  f.write(line)
f.write("</ul>\n")

# write aggregated codesnips
for codesnip in codesnips:
  f.write("<h2 id=\"%s\"> %s </h2>\n" % (codesnip.tag, codesnip.heading))
  AppendFileIntoFile(codesnip.snipfile,f)

f.write("</section>")

# write footer
AppendFileIntoFile(footer,f)

# write footer
AppendFileIntoFile(statsend,f)

f.close()

## ============================================
## write codesnips/combined.html
## ============================================
#
#fnme = "%s/combined.html" % newdir
#f = open (fnme,"w")
#
## write header
#AppendFileIntoFile(header, f)
#
## write initial content
#f.write(preamble) 
#
## write aggregated codesnips
#for codesnip in codesnips:
#  AppendFileIntoFile(codesnip.snipfile,f)
## write footer
#AppendFileIntoFile(footer,f)
#
#f.close()

# write codesnips/linux.html, codesnips/combined.html



