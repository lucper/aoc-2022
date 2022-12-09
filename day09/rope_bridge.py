#!/usr/bin/env python

import fileinput
from math import copysign

def sign(n):
    return int(copysign(1, n)) if n != 0 else 0

def touching(pos1, pos2):
    (a, b), (c, d) = pos1, pos2
    return abs(c - a) <= 1 and abs(d - b) <= 1

def catch_up(src, dest):
    c, d = dest
    path = []
    while not touching(src, dest):
        a, b = src
        src = (a + sign(c - a), b + sign(d - b))
        path.append(src)
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

head = tail = (0, 0)
visited = {tail}

with fileinput.input() as fin:
    for line in fin:
        direction, steps = line.strip().split()
        steps = int(steps)
        if direction == 'L':
            *_, head = walk_left(head, steps)
        elif direction == 'R':
            *_, head = walk_right(head, steps)
        elif direction == 'U':
            *_, head = walk_up(head, steps)
        elif direction == 'D':
            *_, head = walk_down(head, steps)
        else:
            raise ValueError('invalid command')
        if not touching(tail, head):
            *path, tail = catch_up(tail, head)
            visited.update(path + [tail])

## Part 1
print(len(visited))
