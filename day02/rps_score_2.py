#!/usr/bin/env python
"""
Part 1
total score = sum of scores of each round
scores: shape(rock (A,X) = 1 | paper (B,Y) = 2 | scissors (C,Z) = 3) +
        outcome(loss = 0 | draw = 3 | win = 6)
"""

import fileinput

score = {'A': 1,
         'B': 2, 
         'C': 3}

# 0+1 -> 3, 1+1 -> 1, 2+1 -> 2
beats = [3, 1, 2]

# inverse
beaten = [2, 3, 1]

total_score = 0

with fileinput.input() as fin:
    for line in fin:
        opp, me = line.strip().split()
        opp_score = score[opp]

        if me == 'Y':
            total_score += opp_score + 3
        elif me == 'Z':
            total_score += beaten[opp_score - 1] + 6
        elif me == 'X':
            total_score += beats[opp_score - 1]

print(total_score)
