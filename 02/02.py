#!/usr/bin/env python
priser = []
delta = 0.0

with open('aksjer.txt') as file:
    for pris in file:
        priser.append(float(pris.strip()))

for i, pris in enumerate(priser):
    current_delta = max(priser[i:]) - pris
    delta = current_delta if current_delta > delta else delta

print "{0:.4f}".format(delta)
