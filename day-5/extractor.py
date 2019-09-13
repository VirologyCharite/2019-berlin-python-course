class SubsequenceExtractor:
    def __init__(self, fp):
        self.offsets = []

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
                    raise ValueError('Could not parse line %r!' % origLine)
                else:
                    # Are they ints?  Error check.
                    start = int(start)
                    stop = int(stop)

            else:
                if start < 0:
                    raise ValueError('Start cannot be negative.')

                stop = start

            start -= 1

            # Error checking! Less than zero? start < stop?

            # print('%s: %d %d' % (line, start, stop))
            self.offsets.append((start, stop))

    def extract(self, sequence):
        for start, stop in self.offsets:
            subsequence = sequence[start:stop]
            if len(subsequence) == stop - start:
                yield (start, stop, subsequence)
