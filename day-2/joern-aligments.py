#!/usr/bin/env python

import argparse
from Bio import AlignIO


def allNs_func(string):
	for char in string:
		if char != 'N':
			return False
	return True

# string function excamples
# string.count   # string.upper


parser = argparse.ArgumentParser(
    description=("Extract sub-sequences from an alignment and sumarize them."))

parser.add_argument(
    '--file', required=True,
    help=('The alignment file.'))

parser.add_argument(
    '--verbose', default=False, action='store_true',
    help=('If True, print extra info.'))

parser.add_argument(
    '--start', type=int, default=0,
    help=('The starting position in the sequences.'))

parser.add_argument(
    '--stop', type=int, default=10,
    help=('The stop position in the sequences.'))

parser.add_argument(
	'--limit', type=int,default=1000,
	help=('The limit of processed sequences'))

args = parser.parse_args()

if args.start >= args.stop:
    print("Error - Start has to be less than stop.")
    exit()

if args.start < 0 or args.stop < 0:
    print("Error - negative Number not allowed")
    exit()

if args.verbose:
    print('OK, here we go.... working on file', args.file)

alignment = AlignIO.read(args.file, 'fasta')


sub_basket = {}						# empty dictionary for subsequences

count=0								# counter for limits

for record in alignment:

    subseq = str(record.seq[args.start:args.stop])

    count+=1
    
    if args.limit is not None and count > args.limit:			# limit the aligment #
    	break

    # elif allNs_fun(subseq):								# other option to get all Ns out
    #	continue

    elif subseq in sub_basket:		# value of subseq in dictionary increased by 1 
        sub_basket[subseq] +=1

    else:
        sub_basket[subseq] = 1		# fill dictionary with subseq and link it to value 1

#---------------------------- Delete All Ns-------------------------------------------#
all_Ns= "N"*len(subseq)

if all_Ns in sub_basket:
    	del sub_basket[all_Ns]

#------------------------Check Sequence Length----------------------------------------#
seq_length = args.stop - args.start   

if len(subseq) != seq_length:
    	print("There is a Problem! Check Seqence Length")


#-------------------------All Seq are same -----------------------------------------#
if len(sub_basket) ==1:
	print("All sub-sequences are the same!")


#-------------------------Output------------------------------------------------#
for subseq, count in sub_basket.items():
    print(subseq, "Sum of subseq=", count, "length=", seq_length)

    # print("%s - %s" % (record.seq[args.start:args.stop], record.id))