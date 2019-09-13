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
    '--start', required=True,
    help='The motif to look for in the sequences.')

parser.add_argument(
    '--stop', required=True,
    help='The motif to look for in the sequences.')


args = parser.parse_args()

recordCount = 0

pattern = re.compile(args.motif)

for record in SeqIO.parse(args.filename, 'fasta'):

    seq = str(record.seq)

    for match in pattern.finditer(seq):
        if match is not None:
            subsequence = match.group(0)
            print('Found motif %r at position %d in sequence %s' %
                  (subsequence, match.start(), record.id))

    recordCount += 1

    if recordCount == args.limit:
        break
