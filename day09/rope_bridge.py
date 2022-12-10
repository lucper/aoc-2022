#!/usr/bin/env python

import fileinput
from math import copysign
from operator import add

def sign(n):
    return int(copysign(1, n)) if n != 0 else 0

def catch_up(src, dest):
    (a, b), (c, d) = src, dest
    if abs(c - a) > 1 or abs(d - b) > 1:
        a, b = a + sign(c - a), b + sign(d - b)
    return a, b

## change number_of_knots to 2 for Part 1
number_of_knots = 10
rope = [(0,0) for _ in range(number_of_knots)]
visited = {rope[-1]}
vector = {'L': (-1, 0),
          'R': (1, 0),
          'U': (0, 1),
          'D': (0, -1)}

with fileinput.input() as fin:
    for line in fin:
        direction, steps = line.strip().split()
        for _ in range(int(steps)):
            rope[0] = tuple(map(add, rope[0], vector[direction]))
            for head, (tail_idx, tail) in zip(rope, enumerate(rope[1:], 1)):
                rope[tail_idx] = catch_up(tail, head)
            visited.add(rope[tail_idx])

print(len(visited))
