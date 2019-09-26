import sys

#RosalindProblem2.py

s = sys.stdin.read().strip()

#Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' with 'U'.

string_output = s.replace('T','U')

print(string_output)