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
                        
                    try:
                    # Are they ints?  Error check.
                        start = int(start)
                        stop = int(stop)
                    except ValueError:
                        print('Invalid entry %s' % line)
                        continue

                else:
                    stop = start

                start -= 1
                
                if start > stop:
                    print('Wrong: Start > stop %s' % line)
                    continue
                    
                if start < 0 or stop < 0:
                    print('Negative values are forbidden %s' % line)
                    continue
                
                # Error checking! Less than zero? start < stop?

                # print('%s: %d %d' % (line, start, stop))
                else:
                    self.offsets.append((start, stop))

    def extract(self, sequence):
        for start, stop in self.offsets:
            subsequence = sequence[start:stop]
            yield (start, stop, subsequence)
