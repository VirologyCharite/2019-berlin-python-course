import sys

names = {}

for line in sys.stdin:
    line = line.strip()
    if line in names:
        names[line] += 1
    else:
        names[line] = 1

for name in names:
    if names[name] > 1:
        print(name)
