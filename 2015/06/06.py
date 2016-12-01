#!/usr/bin/env python
def p(l, r):
    if l == 0 and r == 0:
        return 1
    if l == 0:
        return p(0, r-1)
    if r <= l:
        return p(l-1, r)

    return p(l-1, r) + p(l, r-1)

print p(13,13)
