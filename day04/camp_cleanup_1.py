#!/usr/bin/env python

import fileinput
from itertools import chain

def get_intervals(pair):
    return chain.from_iterable(tuple(map(int, interval.split('-'))) 
            for interval in pair.split(','))

def fully_overlap(x, y, z, w):
    return (x <= z and y >= w) or (z <= x and w >= y)

with fileinput.input() as fin:
    print(sum(fully_overlap(*get_intervals(line.strip())) for line in fin))
