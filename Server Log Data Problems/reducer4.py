#!/usr/bin/python

import sys

currentIP = None
requestedCount = 0

for line in sys.stdin:
    newIP = line.strip().split()
    if len(newIP) != 1:
	continue
    if currentIP and currentIP != newIP:
	print currentIP,"\t", requestedCount
	requestedCount = 0

    currentIP = newIP
    requestedCount += 1


if currentIP != None:
    print currentIP,"\t", requestedCount
