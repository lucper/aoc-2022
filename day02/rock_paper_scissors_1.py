#!/usr/bin/env python
"""
Part 1
total score = sum of scores of each round
scores: shape(rock (A,X) = 1 | paper (B,Y) = 2 | scissors (C,Z) = 3) +
        outcome(loss = 0 | draw = 3 | win = 6)
"""

import fileinput

score = {'A': 1, 'X': 1,
         'B': 2, 'Y': 2, 
         'C': 3, 'Z': 3}

# 0+1 -> 3, 1+1 -> 1, 2+1 -> 2
beats = [3, 1, 2]

total_score = 0

with fileinput.input() as fin:
    for line in fin:
        opp, me = line.strip().split()
        opp_score, my_score = score[opp], score[me]

        if opp_score == my_score:
            total_score += my_score + 3
        elif beats[my_score - 1] == opp_score:
            total_score += my_score + 6
        else:
            total_score += my_score

print(total_score)
