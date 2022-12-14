#!/usr/bin/env python

import fileinput
from ast import literal_eval

def right_order(left, right):
    ##  1 => true, in order
    ## -1 => false, not in order
    ##  0 => continue
    if isinstance(left, int) and isinstance(right, int):
        return 1 if left < right else -1 if left > right else 0
    elif isinstance(left, int):
        return right_order([left], right)
    elif isinstance(right, int):
        return right_order(left, [right])
    else:
        if left and not right:
            return -1
        if not left and right:
            return 1
        if not left and not right:
            return 0
        if (r := right_order(left[0], right[0])) != 0:
            return r
        return right_order(left[1:], right[1:])

with fileinput.input() as fin:
    pairs = [literal_eval(line.strip()) for line in fin if line.strip()]

## Part 1
count = sum(i for i, pair in enumerate(zip(pairs[::2], pairs[1::2]), 1) if right_order(*pair) > 0)
print(count)
