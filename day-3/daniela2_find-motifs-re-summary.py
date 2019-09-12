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
    '--maxpatternlength', type=int, default=10,
    help='Maximum length of a pattern in regular expression.')

parser.add_argument(
    '--minpatternlength', type=int, default=0,
    help='Minimum length of a pattern in regular expression.')


args = parser.parse_args()

recordCount = 0

pattern = re.compile(args.motif)

summary = {}

for record in SeqIO.parse(args.filename, 'fasta'):

    seq = str(record.seq[args.start:args.stop])

    if record.id in summary:
        print('hey, sequence %s has already been seen!' % record.id)
        exit()
    else:
        summary[record.id] = {           #an dieser Stelle wird gesagt was ins Dictionary übertragen wird
            'positions': [],
            'matchedText': [],
        }

    for match in pattern.finditer(seq):
        if match is not None:                                   #wenn man einen Hit gefunden hat gehe folgendermaßen damit vor:
            if len(match.group(0)) > args.maxpatternlength:     #wenn kleiner als die maximale Anzahl an Buchstaben, dann mache weiter
                continue
            if len(match.group(0)) < args.minpatternlength:     #wenn größer als die minimale Anzahl an Buchstaben, dann mache weiter
                continue
            else:
                summary[record.id]['positions'].append(match.start())       #Postion ins Dictionary aufnehmen
                summary[record.id]['matchedText'].append(match.group(0))    #Sequenz ins Dictionary aufnehmen



    recordCount += 1                    #Zähle Anzahl der untersuchten Sequenzen und höre auf, wenn das Limit-Argument überschritten wird

    if recordCount == args.limit:
        break


for seqId in summary:
    print(seqId)
    for index in range(len(summary[seqId]['positions'])):
        print('  %5d: %s' % (summary[seqId]['positions'][index],
                             summary[seqId]['matchedText'][index]))
