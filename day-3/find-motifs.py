#!/usr/bin/env python

import argparse
from Bio import SeqIO


def findMotifs(motif, sequence):
    """
    Find the instances of a motif in a sequence.

    @param sequence: A sequence string.
    @param motif: A ....
    @return: A list of location in sequence where motif occurs.
    """
    positions = []
    lastPosition = -1

    while True:
        position = sequence.find(motif, lastPosition + 1)

        if position == -1:
            return positions
        else:
            positions.append(position)
            lastPosition = position


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

args = parser.parse_args()

recordCount = 0

for record in SeqIO.parse(args.filename, 'fasta'):

    seq = str(record.seq)

    for position in findMotifs(args.motif, seq):
        foundSubseq = seq[position:position + len(args.motif)]
        print('Found motif %r at position %d in sequence %s' %
              (foundSubseq, position, record.id))

    recordCount += 1

    if recordCount == args.limit:
        break
