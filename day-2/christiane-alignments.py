#!/usr/bin/env python

import argparse
from Bio import AlignIO

parser = argparse.ArgumentParser(
    description=('Extract sub-sequences from FASTA files and summarize them.'))

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

parser.add_argument(
    '--limit', type=int,
    help=('The maximum number of sequences processed.'))

args = parser.parse_args()

if args.verbose:
    print('OK, here we go.... working on file', args.file)

alignment = AlignIO.read(args.file, 'fasta')

count = 0
subsequences = {}
seq_strings = {}
expectedlength = args.stop - args.start
NString = 'N' * expectedlength
NCounter = 0

if args.start >= args.stop:
    print('Error: Stop needs to be bigger than start.')
    exit()

elif args.start < 0 or args.stop < 0:
    print('Error: Start and stp cannot be negative.')
    exit()

for record in alignment:
    subseq = str(record.seq[args.start:args.stop])

    if len(subseq) != expectedlength:
        print('Error: Subsequence length does not match with input length.')
        exit()

    if subseq == NString:
        NCounter += 1
        if args.verbose:
            print('Found a sub-sequence of Ns')
        continue

    if subseq in subsequences:
        subsequences[subseq] += 1
    else:
        subsequences[subseq] = 1

    print("%s - %s" % (record.seq[args.start:args.stop], record.id))

    count += 1
    if count == args.limit:
        break

if args.limit == None:
    print('No limit.')
else:
    print('Limit:', args.limit)

print('Summary:')
for subseq in subsequences:
    print(subseq, subsequences[subseq])

if len(subsequences) == 1:
    print('All sequences are the same.')

if NCounter != 0:
    print('There are %s Sequences of Ns' % NCounter)