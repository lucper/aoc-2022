#!/usr/bin/env python

import fileinput
from string import ascii_letters
from itertools import islice

total = 0

with fileinput.input() as fin:
    lines = [line.strip() for line in fin]
    start, end = 0, 3
    while end <= len(lines):
        group = [set(line) for line in islice(lines, start, end)]
        badge, *rest = set.intersection(*group)
        total += ascii_letters.index(badge) + 1
        start += 3
        end += 3

print(total)
