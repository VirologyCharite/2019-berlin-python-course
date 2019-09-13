#!/usr/bin/env python

import argparse
import sys
from Bio import AlignIO

def allNs_v3(string):
    for char in string:
        if char != 'N':
            return False
    return True

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

parser.add_argument(
    '--limit', type=int, default=None,
    help=('The stop position in the sequences.'))

args = parser.parse_args()

if args.start >= args.stop:
    print('Error message: selected range invalid.')
    exit()

if args.start < 0:
    print('Error message: selected range invalid.')
    exit()

if args.stop < 0:
    print('Error message: selected range invalid.')
    exit()    

expected_range = args.stop - args.start

if args.verbose:
    print('OK, here we go.... working on file', args.file)

alignment = AlignIO.read(args.file, 'fasta')

checker = ''
replacer = ''

for char in range(0,expected_range):
    checker = checker + 'N'
    replacer = replacer + '.'

counter = 0
dictionary_of_sub_sequences = {}

for record in alignment:
    counter += 1
    subseq = str(record.seq[args.start:args.stop])

    if args.limit:
        if counter > args.limit:
            break

    if len(subseq) != expected_range:
        print('Error message: selected range invalid.')
        exit()    

    if subseq in dictionary_of_sub_sequences:
        dictionary_of_sub_sequences[subseq] += 1
    else:
        dictionary_of_sub_sequences[subseq] = 1
print()
print('Summary:')
for key,value in dictionary_of_sub_sequences.items():
    print(key,value)

counter = 0
for record in alignment:
    counter += 1
    subseq = str(record.seq[args.start:args.stop])
    if args.limit:
        if counter > args.limit:
            break
    if subseq == checker:
        print("%s - %s" % (replacer, record.id))
    else:
        print("%s - %s" % (subseq, record.id))

if len(dictionary_of_sub_sequences) == 1:
    print('Wow, all these sequences are the same!')

