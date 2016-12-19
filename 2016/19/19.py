#!/usr/bin/env python

with open('text.txt') as fil:
    for line in fil:
        new_line = ''
        for c in line.strip():
            if int(c) % 2 == 0:
                new_line += '#'
            else:
                new_line += ' '
        print new_line
