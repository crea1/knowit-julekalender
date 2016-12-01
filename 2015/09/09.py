#!/usr/bin/env python
letters = 'ABCDEFGHIJKLMNOPQRSTUVWZYZ'

def convert(num):
    column = ""
    current = num
    rest = num
    while (current > 0):
        rest = current % 26
        current = int(current / 26)

        if rest == 0:
            current -= 1

        column = letters[rest -1] + column

    return column

# print convert(30) + " == AD"
# print convert(26) + " == Z"
# print convert(27) + " == AA"
# print convert(52) + " == AZ"
# print convert(79) + " == CA"
print convert(142453146368)
