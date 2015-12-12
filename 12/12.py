#!/usr/bin/env python
numbers = []
for i in range(100000000 + 1):
    if i % 7 == 0 and i % 5 != 0:
        numbers.append(i)

print str(sum(numbers))
