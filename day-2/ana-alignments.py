#!/usr/bin/env python

import argparse
from Bio import AlignIO

subsequences = {}

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



if args.start < 0:
    print('Error: start and or stop negative!')
    exit()

else:
    if args.stop < 0:
        print('Error: start and or stop negative!')
        exit()
    else:
        if args.start > args.stop:
            print('Error: start bigger than stop!')
            exit()


        #else:
            #for record in alignment:
                #print("%s - %s" % (record.seq[args.start:args.stop], record.id))

firstRecord = True
        
for record in alignment:
    subseq = str(record.seq[args.start:args.stop])

    if firstRecord:
        nsString = 'N' * len(subseq)
        firstRecord = False
        # print('Made ns string', nsString)

    if subseq == nsString:
        print('Ignoring', subseq)
        continue

    if subseq in subsequences:
        subsequences[subseq] += 1
    else:
        subsequences[subseq] = 1

for subsequence, value in subsequences.items():
    print(subsequence[:50], value)

print()

for subsequence in sorted(subsequences):
    print(subsequence[:50], subsequences[subsequence])



