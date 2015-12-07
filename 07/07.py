#!/usr/bin/env python
sum = 0

def reverse(num):
    return int(str(num)[::-1])

for i in range(1, 1001):
    if i % 7 == 0 and reverse(i) % 7 == 0:
        sum += i


print sum
