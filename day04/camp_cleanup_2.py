#!/usr/bin/env python

import fileinput

count = 0

with fileinput.input() as fin:
    for line in fin:
        p1, p2 = [interval.split('-') for interval in line.strip().split(',')]
        x, y = int(p1[0]), int(p1[-1])
        z, w = int(p2[0]), int(p2[-1])
        count += 1 if x <= w and z <= y else 0

print(count)
