# Temperature_Converter

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
        '--far', type=float,
        help=('The temperature in Farenheit.'))

parser.add_argument(
        '--cel', type=float,
        help=('The temperature in Celsius.'))


def convertFarenheitToCelsius(farenheit_temp):
    return (farenheit_temp - 32) * (5/9)


def convertCelsiusToFarenheit(celsius_temp):
    return celsius_temp * (9/5) + 32


args = parser.parse_args()

if args.far:
    print(str(convertFarenheitToCelsius(args.far)))

if args.cel:
    print(str(convertCelsiusToFarenheit(args.cel)))
