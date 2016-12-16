#!/usr/bin/env python
import math


def is_perfect_cube(a):
    a = abs(a)
    return int(round(a ** (1. / 3))) ** 3 == a


def is_sum_43(a):
    return sum(int(x) for x in str(a)) == 43


def is_square(a):
    root = math.sqrt(a)
    return int(root + 0.5) ** 2 == a


for n in range(100000, 500000 + 1):
    # is_cube = is_perfect_cube(n) # not needed i found out :)
    if is_square(n) and is_sum_43(n):
        print n

