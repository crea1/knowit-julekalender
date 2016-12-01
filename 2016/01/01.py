#!/usr/bin/env python

number = 6

while number * 4 != int(str(number)[-1:] + str(number)[:-1]):
    number = number + 10
print number
