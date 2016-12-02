#!/usr/bin/env python

a, b = 1, 1
max_value = 4000000000
sum_value = 0
while a <= max_value:
    if a % 2 == 0:
        sum_value += a
    a, b = b, a+b

print sum_value
