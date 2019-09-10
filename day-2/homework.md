## Homework for day 2

* If the `--start` value is bigger than the `--stop` value, print an error
  message and exit!
* Check that `--start` and `--stop` are not negative.
* Keep a dictionary of the sub-sequences and count how many times each
  sub-sequence occurs and print a summary.
* Add command line arg called `--limit` that limits the number of sequences
  processed (hint: use `break`).
* If the length of the sub-sequences is not `stop - start` then there's a
  problem.
* If all sub-sequences are the same, print an exta line of output (hint:
  use `if len(dictionary) == 1:`).
* Extra credit: In the summary, don't print sequences that are all `N`s.
