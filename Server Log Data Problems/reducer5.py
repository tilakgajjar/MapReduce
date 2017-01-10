#!/usr/bin/python

import sys

currentPath = None
requestedCount = 0

for line in sys.stdin:
    newPath = line.strip().split()
    if len(newPath) != 1:
	continue
    if currentPath and currentPath != newPath:
	print currentPath,"\t", requestedCount
	requestedCount = 0

    currentPath = newPath
    requestedCount += 1


if currentPath != None:
    print currentPath,"\t", requestedCount
