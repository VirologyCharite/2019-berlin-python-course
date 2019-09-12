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
    '--target', required=True,
    help='The target to look for in the sequences.')

parser.add_argument(
    '--limit', type=int,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--start', type=int, default = 0,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--stop', type=int, default = 10,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--mismatch', type=int, default = 1,
    help='The maximum number of sequences to process.')

parser.add_argument(
    '--step', type=int, default = 1,
    help='The maximum number of sequences to process.')


args = parser.parse_args()

if args.start < 0 or args.stop < 0:
    print('Error: start and or stop negative!')
    exit()

if args.start > args.stop:
    print('Error: start bigger than stop!')
    exit()

def slidingWindow(sequence,winSize,step=1):
    """Returns a generator that will iterate through
    the defined chunks of input sequence.  Input sequence
    must be iterable."""
 
    # Verify the inputs
    try: it = iter(sequence)
    except TypeError:
        raise Exception("**ERROR** sequence must be iterable.")
    if not ((type(winSize) == type(0)) and (type(step) == type(0))):
        raise Exception("**ERROR** type(winSize) and type(step) must be int.")
    if step > winSize:
        raise Exception("**ERROR** step must not be larger than winSize.")
    if winSize > len(sequence):
        raise Exception("**ERROR** winSize must not be larger than sequence length.")
 
    # Pre-compute number of chunks to emit
    numOfChunks = int(((len(sequence)-winSize)/step)+1) 
 
    # Do the work
    for i in range(0,numOfChunks*step,step):
        yield (sequence[i:i+winSize], i)


def matches_with_tolerance(subseq, target, tolerance=0):
	total_strikes = 0

	for index in range(len(target)):
		if subseq[index] != target[index]:
			total_strikes += 1

	return total_strikes <= tolerance

recordCount = 0
target = str(args.target)
winSize = len(target)

for record in SeqIO.parse(args.filename, 'fasta'):
    subseq = str(record.seq[args.start:args.stop])

    gen = slidingWindow(subseq, winSize)

    for x in gen:
        if matches_with_tolerance(x[0], target, args.mismatch):
            print('Found target %r at position %d in sequence %s' % 
                (x[0], x[1], record.id))

    recordCount += 1
    if recordCount == args.limit:
        break
