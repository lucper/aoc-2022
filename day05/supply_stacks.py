#!/usr/bin/env python

import fileinput

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

## run instructions on stacks
for inst in instructions:
    # move <n> from <source> to <target>
    n, source, target = parse(inst)

    for _ in range(n):
        if stacks_col[source]:
            stacks_col[target].append(stacks_col[source].pop())

    print(stacks_col)
