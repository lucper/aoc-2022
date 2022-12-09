#!/usr/bin/env python

import fileinput
from itertools import takewhile

def left_visible(i, j, grid):
    return grid[i][j] > max(grid[i][k] for k in range(0, j))

def right_visible(i, j, grid):
    return grid[i][j] > max(grid[i][k] for k in range(j + 1, len(grid[0])))

def top_visible(i, j, grid):
    return grid[i][j] > max(grid[k][j] for k in range(0, i))

def bottom_visible(i, j, grid):
    return grid[i][j] > max(grid[k][j] for k in range(i + 1, len(grid)))

def scenic_score(i, seq):
    """Right score of seq[i]; for left score, call:
    >>> _scenic_score(len(seq)-i-1, list(reversed(seq)))
    Negative indices will yield unexpected behavior.
    """
    score = sum(1 for _ in takewhile(lambda x: x < seq[i], seq[i + 1:]))
    ## check if last tree (if it exists) has greater or same height
    score += 1 if score + i + 1 < len(seq) and seq[score + i + 1] >= seq[i] else 0
    return score

def top_and_bottom_scenic_scores(i, j, grid):
    column = [grid[k][j] for k, _ in enumerate(grid)]
    return scenic_score(i, column) * scenic_score(len(column) - i - 1, list(reversed(column)))

def left_and_right_scenic_scores(i, j, grid):
    return scenic_score(j, grid[i]) * scenic_score(len(grid[i]) - j - 1, list(reversed(grid[i])))

def count_interior_trees(grid):
    return sum(1 for i in range(1, len(grid) - 1) 
                 for j in range(1, len(grid[0]) - 1)
                 if left_visible(i, j, grid) or
                    right_visible(i, j, grid) or
                    top_visible(i, j, grid) or
                    bottom_visible(i, j, grid))

def best_scenic_score(grid):
    return max(top_and_bottom_scenic_scores(i, j, grid) * left_and_right_scenic_scores(i, j, grid)
               for i in range(1, len(grid) - 1)
               for j in range(1, len(grid[0]) - 1))

with fileinput.input() as fin:
    trees = [[int(c) for c in list(line.strip())] for line in fin]

## Part 1
outer_trees = (2 * len(trees)) + (2 * len(trees[0])) - 4
print(count_interior_trees(trees) + outer_trees)

## Part 2
print(best_scenic_score(trees))
