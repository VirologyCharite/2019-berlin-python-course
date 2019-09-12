#!/usr/bin/env python


import argparse

parser = argparse.ArgumentParser(
    description=('Find motifs in sequences in a FASTA file.'))

parser.add_argument(
    'tempC', type = float,
    help='Temperature in degrees Celcius.')

parser.add_argument(
    '--verbose', default=False, action='store_true',
    help='If given, print extra info.')




args = parser.parse_args()

tempF = (args.tempC * 9/5) + 32


print('%.2f°F' % tempF)

