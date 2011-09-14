#!/usr/bin/python

import sys, csv

def die(msg):
  print msg
  print "Exiting"
  sys.exit()

path = sys.argv[1]
try:
  f = open(path,'rU')
except:
  die("Bad file path: "+path) 

col = sys.argv[2]

sniffer = csv.Sniffer()
first = f.read(2048)
f.seek(0)
format = sniffer.sniff(first)

set = set([])
reader = csv.reader(f,format)

cols = dict()
if sniffer.has_header(first):
  for k, v in enumerate(reader.next()):
    cols[v] = k
else:
  for i in range(50):
    cols[str(i)] = i
  
for row in reader:
  set.add(row[cols[col]])

for x in set:
  print x

