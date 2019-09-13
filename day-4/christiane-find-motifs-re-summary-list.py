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

args = parser.parse_args()

recordCount = 0

pattern = re.compile(args.motif)

summary = []

for record in SeqIO.parse(args.filename, 'fasta'):

    seq = str(record.seq)
    
    duplicate = False
    for entry in summary:
        if record.id == entry['id']:
            duplicate = True
            print("Detected duplicate: %s" % record.id)
            break
    
    if not duplicate:
        entry = {
            'id': record.id,
            'matches': [],
        }

        for match in pattern.finditer(seq):
            if match is not None:
                position = match.start()
                subsequence = match.group(0)
                entry['matches'].append(
                    (position, subsequence)
                )

        summary.append(entry)

        recordCount += 1

        if recordCount == args.limit:
            break

for entry in summary:
    print(entry['id'])

    for position, subsequence in entry['matches']:
        print('  ', position, subsequence)

    # for match in entry['matches']:
        # print('  ', match[0], match[1])
