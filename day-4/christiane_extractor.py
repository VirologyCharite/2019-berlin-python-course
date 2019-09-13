class SubsequenceExtractor:
    def __init__(self, offsetsFile):
        self.offsets = []

        with open(offsetsFile) as fp:
            for line in fp:
                origLine = line
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                try:
                    start = int(line)
                except ValueError:

                    try:
                        start, stop = line.split('-')
                    except ValueError:
                        print('Could not parse line %r!' % origLine)
                        print('No n here %r' % origLine)
                    try:
                        # Are they ints?  Error check.
                        start = int(start)
                        stop = int(stop)
                    except ValueError:
                        print('Entry %r is not a number' % origLine)
                        continue

                else:
                    stop = start

                start -= 1

                # Error checking! Less than zero? start < stop?
                if start >= stop:
                    print('Error: Stop should be bigger than start. %r!' % origLine)

                elif start < 0 or stop < 0:
                    print('Error: Start and Stop cannot be negative. %r!' % origLine)

                # print('%s: %d %d' % (line, start, stop))
                else:
                    self.offsets.append((start, stop))

    def extract(self, sequence):
        for start, stop in self.offsets:
            subsequence = sequence[start:stop]
            yield (start, stop, subsequence)
