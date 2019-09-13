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
                        # Alternatively:
                        # raise ValueError('Error Message with more 
                        # useful text')
                        continue
                    else:
                        try:
                            start = int(start)
                        except ValueError:
                            print('Start is not a number.')
                            continue
                        try:
                            stop = int(stop)
                        except ValueError:
                            print('Stop is not a number.')
                            continue

                else:
                    stop = start

                start -= 1

                if stop - start < 0:
                    print('Subsequence is smaller than 0.')
                    exit()

               

                print('%s: %d %d' % (line, start, stop))
                self.offsets.append((start, stop))

    def extract(self, sequence):
        for start, stop in self.offsets:
            subsequence = sequence[start:stop]
            if len(subsequence) == stop - start:
                #otherwise stop is higher than sequence length
                yield (start, stop, subsequence)
