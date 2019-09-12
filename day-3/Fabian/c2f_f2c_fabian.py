
import argparse

parser = argparse.ArgumentParser(
    description=('Convert Celsius to Fahrenheit and the other way around.'))

parser.add_argument(
    '--tempC',
    help='The temperature in Celsius.')

parser.add_argument(
    '--tempF',
    help='The temperature in Fahrenheit.')

args = parser.parse_args()

if args.tempC:
    fahrenheit = (int(args.tempC) * 9/5) + 32
    print(str(args.tempC), '°C is', fahrenheit, '°F.')

if args.tempF:
    celsius = (int(args.tempF)-32) * 5/9
    print(str(args.tempF), '°F is', celsius, '°C.')
