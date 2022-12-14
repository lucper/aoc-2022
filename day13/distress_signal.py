#!/usr/bin/env python

import fileinput

def right_order(left, right):
    if left and not right:
        return False
    if not left and right:
        return True
    if not left and not right:
        return False
    
    if isinstance(left[0], int) and isinstance(right[0], int):
        return left[0] < right[0] if left[0] != right[0] else right_order(left[1:], right[1:])
    elif isinstance(left[0], int):
        return right_order([[left[0]]] + left[1:], right)
    elif isinstance(right[0], int):
        return right_order(left, [[right[0]]] + right[1:])
    else:
        return right_order(left[0], right[0]) or right_order(left[1:], right[1:])

with fileinput.input() as fin:
    pairs = [eval(line.strip()) for line in fin if line.strip()]
    count = sum(i for i, pair in enumerate(zip(pairs[::2], pairs[1::2]), 1) if right_order(*pair))

print(count)
