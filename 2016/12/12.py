#!/usr/bin/env python
import string

msg = "Your message was received with gratitude! We do not know about you, but Christmas is definitely our favourite holiday. The tree, the lights, all the presents to unwrap. Could there be anything more magical than that?! We wish you a happy holiday and a happy new year!"
roman = {0: "0", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI", 12: "XII", 13: "XIII"}

msg = msg.lower().translate(None, string.punctuation).replace(' ', '')
result = [None] * len(msg) * 2

count = 0
for c in msg:
    n = ord(c) - 96
    if n % 2 == 0:
        result[count] = roman[n / 2]
        result[len(msg) * 2 - count - 1] = roman[n / 2]
    else:
        result[count] = roman[((n + 1) / 2)]
        result[len(msg) * 2 - count - 1] = roman[((n - 1) / 2)]
    count += 1

print ", ".join(result)
