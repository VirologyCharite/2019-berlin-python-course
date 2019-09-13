#!/usr/bin/env python

import argparse
import pandas as pd


parser = argparse.ArgumentParser(
    description=('Read a CSV file!'))

parser.add_argument(
    'filename', help='The CSV file to read')


args = parser.parse_args()

df = pd.read_csv(args.filename)

print(df.Sex == 'F')

print(df[df.Sex == 'F'])
