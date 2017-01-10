#!/usr/bin/python

import sys


mostPopularPathname = None
mostPopularPathnameCount = 0
currentPathname = None
currentPathnameCount = 0


for line in sys.stdin:
    path = line.strip().split()
    if len(path) != 1:
	continue

    if currentPathname and currentPathname != path:
	if currentPathnameCount > mostPopularPathnameCount:
	    mostPopularPathnameCount = currentPathnameCount
	    mostPopularPathname = currentPathname
        currentPathnameCount = 0
	
    currentPathname = path
    currentPathnameCount += 1

print mostPopularPathname, "\t" ,mostPopularPathnameCount
