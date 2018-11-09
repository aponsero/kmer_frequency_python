#!/usr/bin/env python3

import argparse
import itertools
from Bio import SeqIO

def get_args(): 
  parser = argparse.ArgumentParser(description='Count kmers in file')
  parser.add_argument('-f', '--fasta', help='FASTA input file',
    type=str, metavar='FILE', required=True)
  parser.add_argument('-k', '--kmer', help='Kmer length', default=4,
    type=int, metavar='KMER', required=False)

  return parser.parse_args()

def find_reverse(seq):
    reverse=""
    for base in seq :
        if base == 'A':
            reverse=reverse+'T'
        elif base =='T':
            reverse=reverse+'A'
        elif base == 'C':
            reverse=reverse+'G'
        elif base =='G':
            reverse=reverse+'C'
        else :
            reverse=reverse+'X'
    return reverse


def gen_kmers(k):
  bases=['A','T','G','C']
  return [''.join(p) for p in itertools.product(bases, repeat=k)]

def uniq_kmers(kmers):
  didthat=[]
  uniq =[]
    
  for kmer in kmers:
    if kmer not in didthat :
        didthat.append(kmer)
        reverse=find_reverse(kmer)
        didthat.append(reverse)
        uniq.append(kmer)
        
  return uniq

def main():
  args = get_args()
  k = args.kmer
  all_kmers = gen_kmers(k)
  un_kmers = uniq_kmers(all_kmers)

  print("\t".join(['seq_id'] + un_kmers))

  for record in SeqIO.parse(args.fasta, "fasta") :
    seq    = record.seq
    seqUp  = seq.upper()
    nkmers = len(seq) - k + 1
    kmers  = dict()
    
    for i in list(range(0, nkmers - 1)):
        kmer = str(seqUp[i:i + k])
        
        if kmer in un_kmers :
            if kmer in kmers:
                kmers[kmer] += 1
            else:
                kmers[kmer] = 1
        else :
            rev = find_reverse(kmer)
            if rev in kmers:
                kmers[rev] += 1
            else:
                kmers[rev] = 1
                
    counts = [ (kmers[x]/float(nkmers)) if x in kmers else 0 for x in un_kmers ]
    
    print("\t".join([record.id] + [str(x) for x in counts]))    
        

if __name__ == '__main__': 
  main()
