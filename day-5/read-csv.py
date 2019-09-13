#!/usr/bin/env python

import argparse
import csv


parser = argparse.ArgumentParser(
    description=('Read a CSV file!'))

parser.add_argument(
    'filename', help='The CSV file to read')


args = parser.parse_args()

with open(args.filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    firstRow = True
    for row in reader:
        if firstRow:
            print('I found a header row!!!', row)
            firstRow = False
        else:
            print('Name: %s,  Sex: %s,  Postcode: %s' %
                  (row[0], row[1], row[2]))
