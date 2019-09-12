#Temperature_Converter

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '--far', required=False,
    help=('The temperature in Farenheit.'))

parser.add_argument(
    '--cel', required=False,
    help=('The temperature in Celsius.'))

def ConvertFarenheitToCelsius(Farenheit_temp):
	Celsius_temp = (float(Farenheit_temp) - 32) * (5/9)
	Celsius_temp = str(Celsius_temp)[:4]
	return Celsius_temp
 
def ConvertCelsiusToFarenheit(Celsius_temp):
 	Farenheit_temp = (float(Celsius_temp) * (9/5) + 32)
 	Farenheit_temp = str(Farenheit_temp)[:4]
 	return Farenheit_temp

args = parser.parse_args()

if args.far:
	print(str(ConvertFarenheitToCelsius(args.far)))

if args.cel:
	print(str(ConvertCelsiusToFarenheit(args.cel)))