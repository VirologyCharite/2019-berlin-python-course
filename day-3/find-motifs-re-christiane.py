#!/usr/bin/env python

import re
import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser(
    description=('Find motifs in sequences in a FASTA file.'))

parser.add_argument(
    'filename',
    help='The alignment file.')

parser.add_argument(
    '--verbose', default=False, action='store_true',
    help='If given, print extra info.')

parser.add_argument(
    '--motif', required=True,
    help='The motif to look for in the sequences.')

parser.add_argument(
    '--limit', type=int,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--start', type=int, default=0,
    help='The start position of the motif.')

parser.add_argument(
    '--stop', type=int, default=100, 
    help='The stop position of the motif.')

parser.add_argument(
    '--minpatternlength', type=int, default=1,
    help='The minimal pattern length.')

parser.add_argument(
    '--maxpatternlength', type=int, default=20, 
    help='The maximal pattern length.')

args = parser.parse_args()

if args.start >= args.stop:
    print('Error: Stop needs to be bigger than start.')
    exit()

if args.start < 0 or args.stop < 0:
    print('Error: Start and stop cannot be negative.')
    exit()

recordCount = 0
subsequence = {}

pattern = re.compile(args.motif)

for record in SeqIO.parse(args.filename, 'fasta'): 

    subseq = str(record.seq[args.start:args.stop])

    for match in pattern.finditer(subseq):
        if match is not None:
            if len(match.group(0)) >= args.minpatternlength and len(match.group(0)) <= args.maxpatternlength:
                subsequence = match.group(0)
                print('Found motif %r at position %d in sequence %s' % (subsequence, match.start(), record.id))

#        print('No matches found in %s.' % record.id)

    recordCount += 1

    if recordCount == args.limit:
        break
