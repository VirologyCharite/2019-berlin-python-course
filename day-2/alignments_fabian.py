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
    help=('The maximum number of sequences being aligned.'))



args = parser.parse_args()

print('')

if args.start >= args.stop:
    print('Fix your start and stop position!')
    exit()
#else: print('Good news, everyone!')

if args.start < 0:
    print('Start can not be negative!')
    exit()

if args.stop < 0:
    print('Stop can not be negative!')
    exit()

if args.limit:
    print('Maximum number of sequences is set to ' + str(args.limit) + '.')
else:
    print('No maximum number of sequences set.')

print('')

#if not args.stop:
#    print('No stop defined')
#    exit()

if args.verbose:
    print('OK, here we go.... working on file', args.file)


#defining the length of the alignment
expected_value = args.stop - args.start
#print(expected_value)

#taking out the N strings from the library
nsString = 'N' * expected_value

alignment = AlignIO.read(args.file, 'fasta')

#created library
dict_of_subsequences = {}

#creating a counter
record_counter = 0
#be precise naming stuff like counters - what does if count?


#takes values and puts them in the library by if statement
for record in alignment:
    subseq = str(record.seq[args.start:args.stop])
    #added variable for records.seq to avoid pulling out the subsequences multiple times
    record_counter += 1
    #adding +1 per loop
    if args.limit:
        if record_counter > args.limit:
            break

    if len(subseq) != expected_value:
        print('You exceeded the length of your sequence.')
        exit()

    if subseq == nsString:
        continue
        #do not put it in library


    if subseq in dict_of_subsequences:
        dict_of_subsequences[subseq] += 1
        #add one to counter
    else:
        dict_of_subsequences[subseq] = 1
        #do not add one to counter


#printing the name and the number of each entry
print('Summary of sequence alignment:')
for key, value in dict_of_subsequences.items():
    print(key, value)

print()

record_counter = 0

print('Sequence alignment:')

for record in alignment:
    subseq = str(record.seq[args.start:args.stop])
    #added variable for records.seq to avoid pulling out the subsequences multiple times
    record_counter += 1

    if subseq == nsString:
        continue

    if args.limit:
        if record_counter > args.limit:
            break
        else:
            print("%s - %s" % (subseq, record.id))
    else:
        print("%s - %s" % (subseq, record.id))
        #without the second else command, no sequence alignment was printed
        #if no limit was set

print('')

if len(dict_of_subsequences) == 1:
    print('All your sequences are the same!')
    #length of a dictionary tell you how many things are in the library
print('')
