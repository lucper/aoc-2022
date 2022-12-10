#!/usr/bin/env python

import fileinput

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
            c += 40

print(res)
