#!/usr/bin/env python

import sys
import re
import collections

invertedIndex = collections.defaultdict(list)
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue

    word = data[1].lower()
    invertedIndex[word].append(data[0])

for word in invertedIndex:
    print "{0}\t{1}\t{2}".format(word, len(invertedIndex[word]), invertedIndex[word])
