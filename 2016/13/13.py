#!/usr/bin/env python
import re

grid_size = 10000
grid = [[False for x in range(grid_size)] for y in range(grid_size)]

with open('instruksjoner.txt') as fil:
    for line in fil:
        m = re.match(r'^\D*(\d*),(\d*)\D*(\d*),(\d*)', line, re.M | re.I)
        x_from = int(m.group(1))
        y_from = int(m.group(2))
        x_to = int(m.group(3))
        y_to = int(m.group(4))
        if line.startswith('turn on'):
            for y in range(y_from, y_to + 1):
                grid[y][x_from:x_to + 1] = [True] * ((x_to + 1) - x_from)
        elif line.startswith('turn off'):
            for y in range(y_from, y_to + 1):
                grid[y][x_from:x_to + 1] = [False] * ((x_to + 1) - x_from)
        elif line.startswith('toggle'):
            for y in range(y_from, y_to + 1):
                for x in range(x_from, x_to + 1):
                    grid[y][x] = not grid[y][x]

lights_on = 0
for g in grid:
    lights_on += g.count(True)

print lights_on
