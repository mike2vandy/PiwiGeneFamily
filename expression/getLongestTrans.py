#! /usr/bin/env python

import sys

#retrieves the longest transcript per gene
#when ensemble header resembles: >geneID|transID|geneName
genes = {}
with open(sys.argv[1]) as f:
  for line in f:
    line = line.strip()
    if line.startswith('>'):
      head = line.replace('>', '')
      genes[head] = ''
    else:
      genes[head] += line

gene2 = {}
for head, seq in genes.items():
  geneId = head.split('|')[0]
  if geneId in gene2:
    gene2[geneId].append([head, len(seq), seq])
  else:
    gene2[geneId] = [[head, len(seq), seq]]

for gene, seqs in gene2.items():
  seqs.sort(key = lambda x: x[1], reverse = True)
  if seqs[0][2] != 'Sequence unavailable':
    name = seqs[0][0]
    if seqs[0][1] >= 100:
      print ">{}\n{}".format(name, seqs[0][2])
