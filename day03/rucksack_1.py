#!/usr/bin/env python

import fileinput
from string import ascii_letters

def priotiry(rucksack):
    mid = len(rucksack) // 2
    first, second = set(rucksack[:mid]), set(rucksack[mid:])
    return sum(ascii_letters.index(char) + 1 for char in first & second)

with fileinput.input() as fin:
    print(sum(priotiry(line.strip()) for line in fin))
