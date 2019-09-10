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

#arg.start = parser.add_argument('--start', type=int, default=0)

parser.add_argument(
    '--stop', type=int, default=10,
    help=('The stop position in the sequences.'))

parser.add_argument(
    '--limit', type=int, default=None,
    help=('The limit of sequences being aligned.'))

#arg.stop = parser.add_argument('--stop', type=int, default=10)


args = parser.parse_args()

if args.start > args.stop:
    print('Do you want to count backwards? Fix your start and stop position!')
    exit()
#else: print('Good news, everyone!')

if args.start < 0:
    print('Start can not be negative!')
    exit()

if args.stop < 0:
    print('Stop can not be negative!')
    exit()

if args.limit:
    print('Limit is set to ' + str(args.limit) + '.')
else:
    print('No limit set.')




if args.verbose:
    print('OK, here we go.... working on file', args.file)


#defining the length of the alignment
expected_value = args.stop - args.start
#print(expected_value)

alignment = AlignIO.read(args.file, 'fasta')

#created library
dict_of_subsequences = {}

#creating a counter
counter = 0


#takes values and puts them in the library by if statement
for record in alignment:
    counter += 1
    if args.limit:
        if counter > args.limit:
            break

    if len(record.seq[args.start:args.stop]) != expected_value:
        print('You exceeded the length of your sequence.')
        exit()

    if record.seq[args.start:args.stop] in dict_of_subsequences:
        dict_of_subsequences[record.seq[args.start:args.stop]] += 1
    else:
        dict_of_subsequences[record.seq[args.start:args.stop]] = 1


#printing the name and the number of each entry
print('Summary of sequence alignment:')
for key, value in dict_of_subsequences.items():
    print(key, value)

print()

counter = 0

print('Sequence alignment:')

for record in alignment:
    counter += 1
    if args.limit:
        if counter > args.limit:
            break
        else:
            print("%s - %s" % (record.seq[args.start:args.stop], record.id))

if len(dict_of_subsequences) == 1:
    print('All your sequences are the same!')
