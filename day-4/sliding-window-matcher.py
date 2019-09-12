#!/usr/bin/env python

import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser(
    description=('Find motifs in sequences in a FASTA file.'))

parser.add_argument(
    'filename',
    help='The alignment file.')

parser.add_argument(
    '--verbose', default=False, action='store_true',
    help='If given, print extra info.')

parser.add_argument(
    '--target', required=True,
    help='The target to look for in the sequences.')

parser.add_argument(
    '--limit', type=int,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--start', type=int, default=0,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--stop', type=int,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--mismatch', type=int, default=0,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--step', type=int, default=1,
    help='The maximum number of sequences to process.')


args = parser.parse_args()

if args.start < 0:
    print('Error: start negative!')
    exit()

if args.stop is not None:
    if args.stop < 0:
        print('Error: stop negative!')
        exit()

    if args.start > args.stop:
        print('Error: start bigger than stop!')
        exit()


def countMismatches_v1(string1, string2):
    mismatches = 0

    for char1, char2 in zip(string1, string2):
        if char1 != char2:
            mismatches += 1

    return mismatches


def countMismatches(string1, string2):
    return sum((char1 != char2) for char1, char2 in zip(string1, string2))


def findMatches(subseq, target, targetLen, maxMismatches=0):
    for index in range(len(subseq) - targetLen):
        subsubseq = subseq[index:index+targetLen]
        distance = countMismatches(target, subsubseq)
        if distance <= maxMismatches:
            yield (index, subsubseq, distance)


recordCount = 0
target = str(args.target)
targetLen = len(target)


for record in SeqIO.parse(args.filename, 'fasta'):
    subseq = str(record.seq[args.start:args.stop])

    print(record.id)

    for (position, subsubseq, distance) in findMatches(
            subseq, target, targetLen, args.mismatch):
        print('  ', position, subsubseq, distance)

    recordCount += 1
    if recordCount == args.limit:
        break
