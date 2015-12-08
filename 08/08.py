#!/usr/bin/env python
primtall = 0

def reverse(num):
    return int(str(num)[::-1])

def isPrime(num):
    for i in range(2, 1001):
        if num % i == 0 and num != i:
            return False
    return True


for i in range(2, 1001):
    reversed = reverse(i)
    if reversed != i and isPrime(i) and isPrime(reversed):
        primtall += 1


print primtall
