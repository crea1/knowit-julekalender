#!/usr/bin/env python

def hamming(num):
    numbers = []
    numbers.append(1)
    x2, x3, x5 = 2,3,5
    i = j = k = 0

    for n in range(1, num):
        numbers.append(min(x2, x3, x5))
        if x2 == numbers[n]:
            i += 1
            x2 = 2 * numbers[i]
        if x3 == numbers[n]:
            j += 1
            x3 = 3 * numbers[j]
        if x5 == numbers[n]:
            k += 1
            x5 = 5 * numbers[k]

    return numbers[-1]

print hamming(10000)

#288325195312500000
