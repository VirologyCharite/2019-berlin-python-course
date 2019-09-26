import sys

#RosalindProblem1

#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

s = sys.stdin.read().strip()

string_output = str(s.count('A'))+' '+str(s.count('C'))+' '+str(s.count('G'))+' '+str(s.count('T'))

print(string_output)