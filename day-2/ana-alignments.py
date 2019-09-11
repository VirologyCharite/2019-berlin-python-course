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
    '--stop', type=int, default=100,
    help=('The stop position in the sequences.'))

parser.add_argument(
    '--limit', type=int, default=0,
    help=('Number of processed sequences.'))


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

if args.limit < 0:
    print('Error: limit negative!')
    exit()


firstRecord = True

#To treat 0 as option to run all of the records
recordProcessed = alignment[0:-1 if args.limit == 0 else args.limit]



for record in recordProcessed:

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



if len(subsequences) == 1:
    print("All subsequences are same!")


for subsequence in subsequences:
    if len(subsequence) != args.stop - args.start:
        print("Chosen subsequences length not suitable!")



for subsequence, value in subsequences.items():
    print(subsequence[:50], value)

print()

for subsequence in sorted(subsequences):
    print(subsequence[:50], subsequences[subsequence])



