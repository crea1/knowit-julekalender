#!/usr/bin/env python
priser = []
delta = 0.0
diffs = {}

# open file and add prices to list
with open('aksjer.txt') as file:
    for pris in file:
        priser.append(float(pris.strip()))



# populate dictionary with diffs for a litte faster lookup
print "Creating dictionary with diffs..."
for i, pris in enumerate(priser):
    for j in range(i+1, len(priser)):
        diffs[str(i)+','+str(j)] = max(priser[i+1:j+1]) - pris
        #diffs.append({str(i)+','+str(j): max(priser[i+1:j+1]) - pris})



for i, pris in enumerate(priser):
    print "Processing " + str(i) + "..."
    for j in range(i + 1, len(priser)):
        if i + 1 == j:
            continue
        key = str(i)+','+str(j)
        deltaFirst = diffs[key]
        #print str(i) + " -> " + str(j) + " = " + str(deltaFirst)
        for k in range(j+1, len(priser)):
            if j + 1 == k:
                continue
            key = str(j+1)+','+str(k)
            deltaSecond = diffs[key]
            if (deltaFirst + deltaSecond) > delta:
                delta = deltaFirst + deltaSecond
                print "New max delta: " + "{0:.4f}".format(delta)

print "Max: " + "{0:.4f}".format(delta)
