#!/usr/bin/env python

import fileinput
from math import copysign

def sign(n):
    return int(copysign(1, n)) if n != 0 else 0

def catch_up(src, dest):
    (a, b), (c, d), path = src, dest, [src]
    while abs(c - a) > 1 or abs(d - b) > 1:
        a, b = a + sign(c - a), b + sign(d - b)
        path.append((a, b))
    return path

def walk_right(pos, k):
    i, j = pos
    return [(x, j) for x in range(i + 1, i + k + 1, 1)]

def walk_left(pos, k):
    i, j = pos
    return [(x, j) for x in range(i - 1, i - k - 1, -1)]

def walk_up(pos, k):
    i, j = pos
    return [(i, y) for y in range(j + 1, j + k + 1, 1)]

def walk_down(pos, k):
    i, j = pos
    return [(i, y) for y in range(j - 1, j - k - 1, -1)]

#number_of_knots = 4
number_of_knots = 10
rope = [(0,0) for _ in range(number_of_knots)]
visited = {rope[-1]}

with fileinput.input() as fin:
    for line in fin:
        direction, steps = line.strip().split()
        steps = int(steps)
        print(direction, steps)
        if direction == 'L':
            *_, rope[0] = walk_left(rope[0], steps)
        elif direction == 'R':
            *_, rope[0] = walk_right(rope[0], steps)
        elif direction == 'U':
            *_, rope[0] = walk_up(rope[0], steps)
        elif direction == 'D':
            *_, rope[0] = walk_down(rope[0], steps)
        else:
            raise ValueError('invalid command')
        print(f'head: {rope[0]}')
        for head, (tail_idx, tail) in zip(rope, enumerate(rope[1:], 1)):
            *path, rope[tail_idx] = catch_up(tail, head)
            #print(f'{path + [rope[tail_idx]]}')
        print(path + [rope[-1]])
        print('-----')
        visited.update(path + [rope[-1]])

print(len(visited))
