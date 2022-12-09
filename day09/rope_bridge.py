#!/usr/bin/env python

import fileinput

def touching(pos1, pos2):
    a, b = pos1
    c, d = pos2
    return abs(a - c) <= 1 and abs(b - d) <= 1

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
    curr_pos = (0, 0)
    for line in fin:
        direction, steps = line.strip().split()
        steps = int(steps)
        if direction == 'L':
            *track, curr_pos = walk_left(curr_pos, steps)
            print(track + [curr_pos])
        elif direction == 'R':
            *track, curr_pos = walk_right(curr_pos, steps)
            print(track + [curr_pos])
        elif direction == 'U':
            *track, curr_pos = walk_up(curr_pos, steps)
            print(track + [curr_pos])
        elif direction == 'D':
            *track, curr_pos = walk_down(curr_pos, steps)
            print(track + [curr_pos])
        else:
            raise ValueError('invalid command')
