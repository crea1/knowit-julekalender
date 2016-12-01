#!/usr/bin/env python
streng = 'evdhtiqgfyvcytohqppcmdbultbnzevdbakvkcdpbatbtjlmzaolfqfqjifkoanqcznmbqbeswglgrzfroswgxoritbw'

operations = 0
for pos in range(len(streng)/2):
        left = streng[pos: pos + 1]
        right = streng[-(pos + 1): len(streng) - pos]
        operations += abs(ord(left) - ord(right))

print operations
