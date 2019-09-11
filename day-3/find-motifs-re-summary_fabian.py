#!/usr/bin/env python

import re
import argparse
from Bio import SeqIO


parser = argparse.ArgumentParser(
    description=('Find motifs in sequences in a FASTA file.'))

parser.add_argument(
    '--file',
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
    help=('The starting position in the sequences.'))

parser.add_argument(
    '--stop', type=int, default=10,
    help=('The stop position in the sequences.'))

parser.add_argument(
    '--max_pattern_length', type=int, default=10,
    help=('The maximum length of the pattern.'))

parser.add_argument(
    '--min_pattern_length', type=int, default=0,
    help=('The minmum length of the pattern.'))

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

recordCount = 0

pattern = re.compile(args.motif)

summary = {}

for record in SeqIO.parse(args.file, 'fasta'):

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
            if len(match.group(0)) > args.max_pattern_length:
                continue
            if len(match.group(0)) < args.min_pattern_length:
                continue
            else:
                summary[record.id]['positions'].append(match.start())
                summary[record.id]['matchedText'].append(match.group(0))

        #match_length = len()
        #if match_length > max-pattern-length:
        #    continue

    recordCount += 1

    if recordCount == args.limit:
        break

for seqId in summary:
    print(seqId)
    for index in range(len(summary[seqId]['positions'])):
        print('  %5d: %s' % (summary[seqId]['positions'][index],
                             summary[seqId]['matchedText'][index]))
