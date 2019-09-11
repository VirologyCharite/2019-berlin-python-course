#!/usr/bin/env python

import argparse
from Bio import AlignIO


parser = argparse.ArgumentParser(
    description=('Extract sub-sequences from an alignment and '
                 'summarize them.'))

parser.add_argument(
    '--filename', required=True,
    help='The alignment file.')

parser.add_argument(
    '--verbose', default=False, action='store_true',
    help='If given, print extra info.')

parser.add_argument(
    '--start', type=int, default=0,
    help='The start position in the sequences.')

parser.add_argument(
    '--stop', type=int, default=10,
    help='The stop position in the sequences.')

args = parser.parse_args()

if args.verbose:
    print('OK, here we go.... working on file', args.file)

alignment = AlignIO.read(args.file, 'fasta')

for record in alignment:
    print("%s - %s" % (record.seq[args.start:args.stop], record.id))
