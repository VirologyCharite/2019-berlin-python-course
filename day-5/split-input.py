#!/usr/bin/env python

import sys
import argparse


parser = argparse.ArgumentParser(
    description=('Split input!'))

parser.add_argument(
    '--pattern1', default='a',
    help='pattern 1')

parser.add_argument(
    '--pattern2', default='b',
    help='pattern 2')

parser.add_argument(
    '--pattern3', default='c',
    help='pattern 3')

parser.add_argument(
    '--filename1', default='out.1',
    help='The file that gets lines matching pattern 1')

parser.add_argument(
    '--filename2', default='out.2',
    help='The file that gets lines matching pattern 2')

parser.add_argument(
    '--filename3', default='out.3',
    help='The file that gets lines matching pattern 3')

args = parser.parse_args()

fp1 = open(args.filename1, 'w')
fp2 = open(args.filename2, 'w')
fp3 = open(args.filename3, 'w')

for line in sys.stdin:
    line = line.strip()
    if line.find(args.pattern1) > -1:
        print('Write %r to file %s' % (line, args.filename1), file=sys.stderr)
        print(line, file=fp1)
    elif line.find(args.pattern2) > -1:
        print('Write %r to file %s' % (line, args.filename2), file=sys.stderr)
        print(line, file=fp2)
    elif line.find(args.pattern3) > -1:
        print('Write %r to file %s' % (line, args.filename3), file=sys.stderr)
        print(line, file=fp3)
    else:
        print('Ignoring %r' % line, file=sys.stderr)

fp1.close()
fp2.close()
fp3.close()
