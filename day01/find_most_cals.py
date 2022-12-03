#!/usr/bin/env python

import fileinput

with fileinput.input() as fin:
    vals = []
    curr = 0
    for line in fin:
        line = line.strip()
        if line:
            curr += int(line)
        else:
            vals.append(curr)
            curr = 0

print(max(vals))
