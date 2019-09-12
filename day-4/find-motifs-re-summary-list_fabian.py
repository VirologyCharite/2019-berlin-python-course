#!/usr/bin/env python

import re
import argparse
from Bio import SeqIO

def isInSummary(summary, newId):
    for entry in summary:
        if entry['id'] == newId:
            return True
    return False


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
    help=('The starting position in the sequences.'))

parser.add_argument(
    '--stop', type=int, default=10,
    help=('The stop position in the sequences.'))




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

summary = []

for record in SeqIO.parse(args.filename, 'fasta'):

    if isInSummary(summary, record.id):
        print('Sequence %s is present multiple times.' % record.id)
        print('')
        continue


    seq = str(record.seq[args.start:args.stop])

    entry = {
        'id': record.id,
        'matches': [],
        }

    #if 'id' in summary:
    #    print('Sequence %s is present multiple times!' % record.id)
    #    continue
    # this only works if summary is a dictionary {}

    
    for match in pattern.finditer(seq):
        if match is not None:
            position = match.start()
            subsequence = match.group(0)
            entry['matches'].append(
                (position, subsequence)
            )

    summary.append(entry)

    #summary[entry] for dictionary

    recordCount += 1

    if recordCount == args.limit:
        break

for entry in summary:
    print(entry['id'])

    for position, subsequence in entry['matches']:
        print('  ', position, subsequence)


print('')

    # for match in entry['matches']:
        # print('  ', match[0], match[1])
