#!/usr/bin/env python
roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
numbers = []


def parse_roman(roman):
    values = []
    last_value = 0
    current_value = 0

    for i, letter in enumerate(roman):
        current_value = roman_dict[letter]
        if i > 0 and values[i -1 ] < current_value:
            values[i - 1] = -1 * values[i - 1]
            values.append(current_value)
        else:
            values.append(current_value)

    return sum(values)


def getIntValue(num):
    try:
        return int(num)
    except ValueError:
        try:
            return int(num,2)
        except ValueError:
            return parse_roman(num)


with open('tall.txt') as file:
    for number in file:
        num = number.strip()
        numbers.append(str(getIntValue(num)).zfill(5) + " from value " + num)

numbers.sort()
print "Median on position "+ str(numbers[len(numbers) / 2 - 1])
