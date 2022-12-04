#!/usr/bin/env python

import fileinput
from itertools import chain

def get_intervals(pair):
    return chain.from_iterable(tuple(map(int, interval.split('-'))) 
            for interval in pair.split(','))

def overlap(x, y, z, w):
    return x <= w and z <= y

with fileinput.input() as fin:
    print(sum(overlap(*get_intervals(line.strip())) for line in fin))
