#!/usr/bin/env python

def find2s(num):
    print num
    if len(num) == 1:
        return 1 if num == '2' else 0
    else:
        toerRest = 0
        digit = int(num[0:1])
        if digit == 2:
            toerRest = int(num[1: len(num)]) + 1
        elif digit > 2:
            toerRest = 10 ** (len(num) -1)
        return int(find2s(num[1: len(num)])) + toerRest + (len(num) - 1) * (digit * 10 ** (len(num)-2))
#
print find2s('12345678987654321')
