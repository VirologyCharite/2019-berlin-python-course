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
                    else:
                        # Are they ints?  Error check.
                        start = int(start)
                        stop = int(stop)

                else:
                    stop = start

                start -= 1

                # Error checking! Less than zero? start < stop?

                # print('%s: %d %d' % (line, start, stop))
                self.offsets.append((start, stop))

    def extract(self, sequence):
        for start, stop in self.offsets:
            subsequence = sequence[start:stop]
            # Make sure that the subsequence we extract is of the expected
            # length. If not, we've probably hit the end of the sequence
            # and we don't return this result.
            if len(subsequence) == stop - start:
                yield (start, stop, subsequence)
