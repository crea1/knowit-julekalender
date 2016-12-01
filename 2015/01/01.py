#!/usr/bin/env python
import re # for regexp

matchCount = 0

with open('ids.txt') as file:
    for id in file:
        match = re.match('(\A[a-z]{0,3})(\d{2,8})([A-Z]{3,}\Z)', id.strip())
        if match:
	    print id.strip() + " -> Gyldig (" + match.group(1) + ", " + match.group(2) + ", " + match.group(3) + ")"
            matchCount += 1

print "\nMatch count: " + str(matchCount)
