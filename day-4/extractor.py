class SubsequenceExtractor:
    def __init__(self, offsetsFile):
        self.offsets = []

        with open(offsetsFile) as fp:
            for line in fp:
                origLine = line
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                try: #branch1 check if the whole line is an integer
                    start = int(line)
                except ValueError: #the whole line is not an integer
                    try: #check if there is a hyphen in the line
                        start, stop = line.split('-')
                    except ValueError: #there is no hyphen, the input is unacceptable, close the program
                        print('Could not parse line %r!' % origLine)
                        continue
                    else: #there is a hyphen in the line, split into start and stop variables was successful
                        try: #check if start is an integer
                            start = int(start)
                        except ValueError:
                            print('Could not parse line %r!' % origLine)
                            continue
                        try: #check if stop is an integer
                            stop = int(stop)
                        except ValueError:
                            print('Could not parse line %r!' % origLine)
                            continue
                        if start > stop:
                            print('Invalid window selection, start is larger than stop %r!' % origLine)                            
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
