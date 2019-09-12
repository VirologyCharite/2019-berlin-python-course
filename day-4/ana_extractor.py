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
                        continue
                    else:
                        try:
                            start = int(start)
                        except ValueError:
                            print('Input not integer')
                            continue
                        try:   
                            stop = int(stop)
                        except ValueError:
                            print('Input not integer')
                            continue

                else:
                    stop = start

                start -= 1

                # Error checking! Less than zero? start < stop?

                # print('%s: %d %d' % (line, start, stop))
                self.offsets.append((start, stop))

    def extract(self, sequence):
        for start, stop in self.offsets:
            subsequence = sequence[start:stop]
            yield (start, stop, subsequence)
