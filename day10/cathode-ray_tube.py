#!/usr/bin/env python

import fileinput

## value at index i corresponds to X *during* cycle i
X_hist = [1, 1]

## Part 1
c = 20
res = 0

with fileinput.input() as fin:
    for line in fin:
        op, *val = line.strip().split()
        if op == 'addx':
            X_hist += [X_hist[-1], X_hist[-1] + int(*val)]
        elif op == 'noop':
            X_hist += [X_hist[-1]]
        else:
            raise ValueError('invalid operation')

        ## Part 1
        if c < len(X_hist) and c <= 220:
            res += X_hist[c] * c
            #print(f'c: {c}\tX: {X_hist[c]}\tsignal strength: {c * X_hist[c]}')
            c += 40

print(res)

## Part 2
## TODO: fix this "off-by-two"
CRT_screen = ['.'] * 40 * 6

for c, X in enumerate(X_hist[1:]):
    sprite_pos = (X - 1, X, X + 1)
    #print(f'c: {c}\tX: {X}\tsignal strength: {c * X}\tsprite at {sprite_pos}')
    if c in sprite_pos:
        CRT_screen[c] = '#'

print(CRT_screen)
