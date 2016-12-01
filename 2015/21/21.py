#!/usr/bin/env python
import re # for regexp

words = []

with open('words.txt') as f:
    for a_word in f:
        words.append(a_word.strip())

def find_permutations(word):
    p_words = []
    for i, c in enumerate(word):
        regex = word[:i] + '[\w]' + word[i+1:]
        filter = re.compile(regex).search
        p_words.extend([ (m.group(0) ) for l in words for m in (filter(l),) if m])

    return p_words


words_searched = ['sand']
sequence = 1
while 'hold' not in words_searched:
    more_words = []
    for a_word in words_searched:
        more_words.extend(find_permutations(a_word))

    words_searched = list(set(more_words))
    sequence += 1

print sequence
#8