#!/usr/bin/env python

import sys


b_rates = float(input("Type in the intrest rates your bank gives you  "))
infl = float(input("Type in the inflation rate  "))
s_cap= int(input("Type in your start capital "))
time = int(input("Type in the years the money is saved at your bank  "))

end_cap= s_cap*(1+((b_rates-infl)/100))**time
delta= end_cap-s_cap

if end_cap > s_cap:
	print("Your money worked for you and increased by %s Euro" % delta)

else:
	print("Your money got burned and you lost %s Euro" %delta)