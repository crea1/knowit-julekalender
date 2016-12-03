#!/usr/bin/env python
import re
hatelist = []
friendlist = []
hatecount = {}


def is_friends(hater, hated):
    for f in friendlist:
        if (f[1] == hater or f[2] == hater) and (f[1] == hated or f[2] == hated):
            return True
    return False


def is_also_hated(hater, hater2):
    for hl in hatelist:
        if hl[0] == hater2 and hl[2] == hater:
            return True
    return False


with open('venner.txt') as file:
    for word in file:
        x = re.split(' *', word.strip())
        if x[1] == 'hates':
            hatelist.append(x)
            hatecount[x[0]] = 0
        else:
            friendlist.append(x)

for h in hatelist:
    if not is_also_hated(h[0], h[2]) and is_friends(h[0], h[2]):
        hatecount[h[0]] += 1

print(max(hatecount, key=hatecount.get))
