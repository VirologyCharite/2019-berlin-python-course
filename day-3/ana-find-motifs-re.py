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
    '--start', type=int, default = 0,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--stop', type=int, default = 10,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--minpatternlength', type=int, default = 0,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--maxpatternlength', type=int, default = 20,
    help='The maximum number of sequences to process.')


args = parser.parse_args()


recordCount = 0
subsequence = {}

if args.start < 0 or args.stop < 0:
    print('Error: start and or stop negative!')
    exit()

if args.start > args.stop:
    print('Error: start bigger than stop!')
    exit()


pattern = re.compile(args.motif) 

for record in SeqIO.parse(args.filename, 'fasta'):

    subseq = str(record.seq[args.start:args.stop])


    for match in pattern.finditer(subseq):
        if match is not None and len(match.group(0)) > args.minpatternlength and len(match.group(0)) < args.maxpatternlength:
            subsequence = match.group(0)
            print('Found motif %r at position %d in sequence %s' %
                  (subsequence, match.start(), record.id))

    recordCount += 1

    if recordCount == args.limit:
        break
