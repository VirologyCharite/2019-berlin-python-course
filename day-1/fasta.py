fp = open('xxx.fasta')

maxLength = -1
longestLine = ''
lineNumber = 0

for line in fp:
    lineNumber = lineNumber + 1
    if line.startswith('>'):
        thisLength = len(line) - 2
        if thisLength > maxLength:
            maxLength = thisLength
            longestLine = line
            longestLineNumber = lineNumber

print(longestLineNumber, maxLength, longestLine, end='')
