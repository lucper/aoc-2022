#!/usr/bin/env python

import fileinput
import re

## read input
with fileinput.input() as fin:
    puzzle = [line.strip('\n') for line in fin]

## split stacks and instructions
sep_idx = puzzle.index('')
stacks = puzzle[:sep_idx]
instructions = puzzle[sep_idx + 1:]

## get stack numbers from line containing with indices in input
stacks_idx = [i for i in range(1, len(stacks[-1]), 4)]

## build stack internal representation
stacks_ir = [tuple(reversed([stack[i] for stack in stacks if not stack[i].isspace()])) 
             for i in stacks_idx]
stacks_col = {int(k):list(v) for k, *v in stacks_ir}

## function to parse instruction
def parse(inst):
    """TODO: make order of move, from, to be arbitrary
    """
    imove, ifrom, ito = re.findall(r'[a-z]+ [0-9]', inst)
    n, source, target = int(imove[-1]), int(ifrom[-1]), int(ito[-1]),
    return n, source, target

## run instructions on stacks
def run(instructions, stacks):
    for inst in instructions:
        n, source, target = parse(inst)
        for _ in range(n):
            if stacks[source]:
                stacks[target].append(stacks[source].pop())
    return stacks

def get_tops(stacks):
    return ''.join(stack[-1] for stack in stacks.values())

last_state = run(instructions, stacks_col)
print(get_tops(last_state))
