#!/usr/bin/env python

import argparse
from Bio import AlignIO


parser = argparse.ArgumentParser(
    description=())

parser.add_argument(
    '--file', required=True,
    help=('The alignment file.'))

parser.add_argument(
    '--verbose', default=False, action='store_true',
    help=('If True, print extra info.'))

parser.add_argument(
    '--start', type=int, default=0,
    help=('The starting position in the sequences.'))

parser.add_argument(
    '--stop', type=int, default=10,
    help=('The stop position in the sequences.'))

args = parser.parse_args()

if args.verbose:
    print('OK, here we go.... working on file', args.file)

alignment = AlignIO.read(args.file, 'fasta')

for record in alignment:
    print("%-30s\t-\t%30s" % (record.seq[args.start:args.stop], record.id))
