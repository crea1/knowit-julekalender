#!/usr/bin/env python

puzzleWord = "aeteesasrsssstaesersrrsse"


def ngram(n, word):
    wordlist = []
    for i, ch in enumerate(word):
        if i <= len(word) - n:
            wordlist.append(str(word[i:i + n]))
    return ''.join(part for part in wordlist)


def findword(word):
    sorted_word = ''.join(sorted(word))
    with open('wordlist.txt') as file:
        for file_word in file:
            for i in range(2, 6):
                ngramword = ''.join(sorted(ngram(i, file_word.strip().lower())))
                if ngramword == sorted_word:
                    print str(i) + "-" + file_word


findword(puzzleWord)