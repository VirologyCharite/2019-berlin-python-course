#!/usr/bin/env python

import re
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
    '--motif', required=True,
    help='The motif to look for in the sequences.')

parser.add_argument(
    '--limit', type=int,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--start', type=int, default=0,
    help='The start position in the sequences.')

parser.add_argument(
    '--stop', type=int, default=10,
    help='The stop position in the sequences.')

parser.add_argument(
    '--minPatternLength', type=int, default=0,
    help='The minimum length of a pattern.')

parser.add_argument(
    '--maxPatternLength', type=int, default=20,
    help='The maximum length of a pattern.')

args = parser.parse_args()

recordCount = 0

pattern = re.compile(args.motif)

summary = {}

if args.start >= args.stop:
    print('Error message: selected range invalid.')
    exit()

if args.start < 0:
    print('Error message: selected range invalid.')
    exit()

if args.stop < 0:
    print('Error message: selected range invalid.')
    exit() 

for record in SeqIO.parse(args.filename, 'fasta'):

    seq = str(record.seq[args.start:args.stop])

    if record.id in summary:
        print('hey, sequence %s has already been seen!' % record.id)
        exit()
    else:
        summary[record.id] = {
            'positions': [],
            'matchedText': [],
        }

    for match in pattern.finditer(seq):
        if match is not None:
            if match.group(0) > args.minPatternLength:
                if match.group(0) <= args.maxPatternLength:
                    summary[record.id]['matchedText'].append(match.group(0))
                    summary[record.id]['positions'].append(match.start())
                   
    recordCount += 1

    if recordCount == args.limit:
        break

for seqId in summary:
    print(seqId)
    for index in range(len(summary[seqId]['positions'])):
        print('  %5d: %s' % (summary[seqId]['positions'][index],
                             summary[seqId]['matchedText'][index]))
