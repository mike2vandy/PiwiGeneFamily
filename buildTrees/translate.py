#! /usr/bin/env python2.7

import sys

#Standard DNA to protein translation function
def translate(seq):

  #Standard Translation table
  dna_table = {'TTT':'F','TTC':'F','TTA':'L','TTG':'L' # correct
            ,'TCT':'S','TCC':'S','TCA':'S','TCG':'S' # correct
            ,'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*' # correct
            ,'TGT':'C','TGC':'C','TGA':'*','TGG':'W' # correct
            ,'CTT':'L','CTC':'L','CTA':'L','CTG':'L' # correct
            ,'CCT':'P','CCC':'P','CCA':'P','CCG':'P' # correct
            ,'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q' # correct
            ,'CGT':'R','CGC':'R','CGA':'R','CGG':'R' # correct
            ,'ATT':'I','ATC':'I','ATA':'I','ATG':'M' # correct
            ,'ACT':'T','ACC':'T','ACA':'T','ACG':'T' # correct
            ,'AAT':'N','AAC':'N','AAA':'K','AAG':'K' # correct
            ,'AGT':'S','AGC':'S','AGA':'R','AGG':'R' # correct
            ,'GTT':'V','GTC':'V','GTA':'V','GTG':'V' # correct
            ,'GCT':'A','GCC':'A','GCA':'A','GCG':'A' # correct
            ,'GAT':'D','GAC':'D','GAA':'E','GAG':'E' # correct
            ,'GGT':'G','GGC':'G','GGA':'G','GGG':'G'} # correct

  amino_acid = ''
  first = 0

  while first < len(seq):
      third = first + 3
      codon = seq[first:third]
      if 'N' in codon or 'X' in codon:
        amino_acid += '?'
        first += 3
      elif codon in dna_table:
        amino_acid += dna_table[codon]
        first += 3
      else:
        amino_acid += '?'
        first += 3

  return amino_acid


def build_fas_dict(f):
    seq_dict = {}
    for line in f:
        line = line.strip()
        if line.startswith('>'):
            header = line
            seq_dict[header] = ''
        else:
            seq_dict[header] += line.upper()

    return seq_dict

##MAIN##

if len(sys.argv) < 2:
    inf = sys.stdin
else:
    inf = open(sys.argv[1])

seqs = build_fas_dict(inf)

if inf is not sys.stdin:
  inf.close()

for header, seq in seqs.items():
    aa = translate(seq)
    print header
    count = 0
    while count <= len(aa):
      print aa[count:count + 50]
      count += 50
