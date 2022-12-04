#!/usr/bin/env python

import fileinput
from string import ascii_letters

total = 0

with fileinput.input() as fin:
    for line in fin:
        line = line.strip()
        mid = len(line) // 2
        first, second = set(line[:mid]), set(line[mid:])
        total += sum(ascii_letters.index(char) + 1 for char in first & second)

print(total)
