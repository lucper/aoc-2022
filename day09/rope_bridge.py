#!/usr/bin/env python

import fileinput

def touching(pos1, pos2):
    a, b = pos1
    c, d = pos2
    return abs(a - c) <= 1 and abs(b - d) <= 1

## TODO
## if not in_same_axis(tail, head), then
## tail := (x+1,y+1) if a < c and b < d
## or
## tail := (x-1,y-1) if a > c and b > d
##
## if in_same_axis(tail, head), then
## ...
def in_same_axis(pos1, pos2):
    a, b = pos1
    c, d = pos2
    return a == c or b == d

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

with fileinput.input() as fin:
    head = (0, 0)
    for line in fin:
        direction, steps = line.strip().split()
        steps = int(steps)
        if direction == 'L':
            *track, head = walk_left(head, steps)
            print(track + [head])
        elif direction == 'R':
            *track, head = walk_right(head, steps)
            print(track + [head])
        elif direction == 'U':
            *track, head = walk_up(head, steps)
            print(track + [head])
        elif direction == 'D':
            *track, head = walk_down(head, steps)
            print(track + [head])
        else:
            raise ValueError('invalid command')
