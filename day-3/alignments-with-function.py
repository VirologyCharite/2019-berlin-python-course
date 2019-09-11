#!/usr/bin/env python

import argparse
from Bio import AlignIO


def allNs(string):
    """
    Determine whether a string is composed only of N characters.

    @param string: A string.
    @return: A Boolean, True if the string is all Ns, False otherwise.
    """
    print('I was called with', string)
    for character in string:
        if character != 'N':
            # print('  Found a non-N (%s), returning False' % character)
            return False

    # print('  All Ns, returning True')
    return True


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
    '--limit', type=int,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--start', type=int, default=0,
    help='The start position in the sequences.')

parser.add_argument(
    '--stop', type=int, default=10,
    help='The stop position in the sequences.')

args = parser.parse_args()

if args.start >= args.stop:
    print('Start has to be less than stop.')
    exit()

if args.start < 0 or args.stop < 0:
    print('Start and stop cannot be negative.')
    exit()

if args.verbose:
    print('OK, here we go.... working on file', args.filename)

alignment = AlignIO.read(args.filename, 'fasta')

subsequences = {}

recordCount = 0
expectedLength = args.stop - args.start
nsCount = 0

for record in alignment:
    subseq = str(record.seq[args.start:args.stop])

    if len(subseq) != expectedLength:
        print('Found a sub-sequence of unexpected length.')
        exit()

    if allNs(subseq):
        nsCount += 1
        if args.verbose:
            print('Found a sub-sequence of Ns.')
        continue

    if subseq in subsequences:
        subsequences[subseq] += 1
    else:
        subsequences[subseq] = 1

    recordCount += 1

    if recordCount == args.limit:
        break

if len(subsequences) == 1:
    print("There was only one sub-sequence!")

if nsCount and args.verbose:
    print("There were %d sub-sequences composed of Ns" % nsCount)

for subseq in subsequences:
    print("%s\t%s" % (subseq, subsequences[subseq]))
