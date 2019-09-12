#!/usr/bin/env python

import argparse
from Bio import SeqIO
from urllib.parse import quote

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
    '--text', default=False, type=bool,
    help='The file will be exported in text format when any value is entered.')

args = parser.parse_args()


extractor = SubsequenceExtractor(args.offsetsFile)


def printHeader():
    print('''
<!DOCTYPE html>
<html>
  <head>
  <title>My fabulous web page.</title>
  </head>
  <body>
''')


def printFooter():
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

if args.text == False: #condition for html formatting
    printHeader()

    for record in SeqIO.parse(args.filename, 'fasta'):
        print('<p>%s</p><ol>' % NCBISequenceLink(record.id))
        for start, stop, subsequence in extractor.extract(str(record.seq)):
            print('<li>start=%d, stop=%d, %s</li>' % (start, stop, subsequence))
        print('</ol>')

    printFooter()

else: #condition for text formatting
    for record in SeqIO.parse(args.filename, 'fasta'):
        print(record.id)
        for start, stop, subsequence in extractor.extract(str(record.seq)):
            print(start, stop, subsequence)