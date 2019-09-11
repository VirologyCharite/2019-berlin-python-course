
import argparse

parser = argparse.ArgumentParser(
    description=('Calculates a 10, 15, or 20% tip.'))

parser.add_argument(
    '--tip10',
    help='Calculates 10% tip.')

parser.add_argument(
    '--tip15',
    help='Calculates 15% tip.')

parser.add_argument(
    '--tip20',
    help='Calculates 20% tip.')

parser.add_argument(
    '--tipAll',
    help='Calculates 20% tip.')

args = parser.parse_args()

if args.tip10:
	tip = int(args.tip10) * 0.1
	print('The tip is', tip, '€. Total is', int(args.tip10)+tip, '€.')

if args.tip15:
	tip = int(args.tip15) * 0.15
	print('The tip is', tip, '€. Total is', int(args.tip15)+tip, '€.')

if args.tip20:
	tip = int(args.tip20) * 0.20
	print('The tip is', tip, '€. Total is', int(args.tip20)+tip, '€.')

if args.tipAll:
	tip10 = int(args.tipAll) * 0.10
	tip15 = int(args.tipAll) * 0.15
	tip20 = int(args.tipAll) * 0.20
	print('A 10% tip would be', tip10, '€. Total would be', int(args.tipAll)+tip10, '€.')

	print('A 15% tip would be', tip15, '€. Total would be', int(args.tipAll)+tip15, '€.') 

	print('A 20% tip would be', tip20, '€.Total would be', int(args.tipAll)+tip20, '€.')


