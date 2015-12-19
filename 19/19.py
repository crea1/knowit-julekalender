#!/usr/bin/env python
def F(n):
    if n == 0: return 1
    elif n < 1: return 0
    else:
        return F(n-1) + F(n-2) + F(n-3)

print F(30)
