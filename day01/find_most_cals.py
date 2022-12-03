#!/usr/bin/env python

import fileinput

with fileinput.input() as fin:
    vals, acc = [], 0
    for line in fin:
        line = line.strip()
        if line:
            acc += int(line)
        else:
            vals.append(acc)
            acc = 0
    vals.append(acc)

print(max(vals))
print(sum(sorted(vals, reverse=True)[:3]))
