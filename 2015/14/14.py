#!/usr/bin/env python
import re

def reverse(num):
    return int(str(num)[::-1])

def flip(num):
    flipped = ""
    for c in str(num):
        if c == '6':
            flipped = flipped + '9'
        elif c == '9':
            flipped = flipped + '6'
        else:
            flipped = flipped + str(c)
    return int(flipped)


count = 0
for i in range(0, 100000 + 1):
    if re.match('^[01689.]+$', str(i)) and i == flip(reverse(i)):
        count += 1

print count
