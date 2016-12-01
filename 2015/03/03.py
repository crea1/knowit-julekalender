#!/usr/bin/env python
def is_leap(y):
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True

day_count = 0
fridays = 0
for year in range(1, 2016):
    if (day_count + 256) % 7 == 0:
        fridays += 1

    day_count += 366 if is_leap(year) else 365

print fridays
