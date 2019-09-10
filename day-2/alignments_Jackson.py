#!/usr/bin/env python

import argparse
import sys
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

dictionary_of_sub_sequences = {}
checker = ''
replacer = ''

for char in range(0,expected_range):
    checker = checker + 'N'
    replacer = replacer + '.'

counter = 0
for record in alignment:
    counter += 1
    if args.limit:
        if counter > args.limit:
            break

    if len(record.seq[args.start:args.stop]) != expected_range:
        print('Error message: selected range invalid.')
        exit()    

    if record.seq[args.start:args.stop] in dictionary_of_sub_sequences:
        dictionary_of_sub_sequences[record.seq[args.start:args.stop]] += 1
    else:
        dictionary_of_sub_sequences[record.seq[args.start:args.stop]] = 1
print()
print('Summary:')
for key,value in dictionary_of_sub_sequences.items():
    print(key,value)

counter = 0
for record in alignment:
    counter += 1
    if args.limit:
        if counter > args.limit:
            break
    if record.seq[args.start:args.stop] == checker:
        print("%s - %s" % (replacer, record.id))
    else:
        print("%s - %s" % (record.seq[args.start:args.stop], record.id))


if len(dictionary_of_sub_sequences) == 1:
    print('Wow, all these sequences are the same!')