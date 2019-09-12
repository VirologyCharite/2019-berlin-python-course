#!/usr/bin/env python

import argparse
from Bio import SeqIO
from six.moves.urllib.parse import quote
from pprint import pprint

from extractor import SubsequenceExtractor


parser = argparse.ArgumentParser(
    description=('Find motifs in sequences in a FASTA file.'))

parser.add_argument(
    'filename',
    help='The alignment file.')

parser.add_argument(
    '--offsetsFile', required=True,
    help='The file of offsets to extract.')

parser.add_argument(
    '--format', choices=('html', 'csv', 'text'), default='text',
    help='The output format.')

args = parser.parse_args()


extractor = SubsequenceExtractor(args.offsetsFile)


def printCSVHeader():
    print('Sequence,Start,Stop,Subsequence')


def printHTMLHeader():
    print('''
<!DOCTYPE html>
<html>
  <head>
  <title>My fabulous web page.</title>
  </head>
  <body>
''')


def printHTMLFooter():
    print('''
    </div>
  </body>
</html>
''')


def NCBISequenceLinkURL(title, field=None, delim='|'):
    """
    Given a sequence title, like
        "acc|GENBANK|AY516849.1|GENBANK|42768646 Homo sapiens",
    return the URL of a link to the info page at NCBI.

    @param title: The C{str} sequence title to produce a link URL for.
    @param field: The C{int} field number to use (as delimited by C{delim})
        or C{None} if no field splitting should be done.
    @param delim: The C{str} to split the title on (if C{field} is not
        C{None}).
    @return: A C{str} URL.
    """
    if field is None:
        ref = title
    else:
        try:
            ref = title.split(delim)[field]
        except IndexError:
            raise IndexError(
                'Could not extract field %d from sequence title %r' %
                (field, title))
    return 'http://www.ncbi.nlm.nih.gov/nuccore/' + quote(ref)


def NCBISequenceLink(title, field=None, delim='|'):
    """
    Given a sequence title, like
        "acc|GENBANK|AY516849.1|GENBANK|42768646 Homo sapiens",
    return an HTML <A> tag displaying a link to the info page at NCBI.

    @param title: The C{str} sequence title to produce a link URL for.
    @param field: The C{int} field number to use (as delimited by C{delim})
        or C{None} if no field splitting should be done.
    @param delim: The C{str} to split the title on (if C{field} is not
        C{None}).
    @return: A C{str} HTML <A> tag.
    """
    return '<a href="%s" target="_blank">%s</a>' % (
        NCBISequenceLinkURL(title, field, delim), title)


fmt = args.format

if fmt == 'html':
    printHTMLHeader()
elif fmt == 'csv':
    printCSVHeader()

summary = {}

for record in SeqIO.parse(args.filename, 'fasta'):
    if fmt == 'html':
        print('<p>%s</p><ol>' % NCBISequenceLink(record.id))
    for start, stop, subsequence in extractor.extract(str(record.seq)):
        if fmt == 'html':
            print('<li>start=%d, stop=%d, %s</li>' %
                  (start, stop, subsequence))
        elif fmt == 'csv':
            start += 1
            if start == stop:
                print('%s,%d,,%s' % (record.id, start, subsequence))
            else:
                print('%s,%d,%d,%s' % (record.id, start, stop, subsequence))

            # Test if (start, stop) is in summary. If not, put it in with
            # an empty list value.
            if (start, stop) not in summary:
                summary[(start, stop)] = []

            summary[(start, stop)].append({
                'id': record.id,
                'subsequence': subsequence,
            })

        else:
            print('%d %d %s' % (start, stop, subsequence))

    if fmt == 'html':
        print('</ol>')

if fmt == 'html':
    printHTMLFooter()
elif fmt == 'csv':
    pprint(summary)
