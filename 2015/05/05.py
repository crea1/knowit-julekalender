#!/usr/bin/env python
words_split = []
anagrams = 0

def find(l):
    hits = 0
    for word in words_split:
        if word == l:
            hits += 1
        if hits > 1: # if more than one hit there is no need to find additional words
            return hits
    return hits


with open('words.txt') as file:
    for word in file:
        words_split.append(sorted(list(word)))

words_split.sort()

for word in words_split:
    wa = sorted(list(word))
    if find(wa) > 1:
        anagrams += 1

print anagrams
