#!/usr/bin/env python

import fileinput

def left_visible(i, j, grid):
    return grid[i][j] > max(grid[i][k] for k in range(0, j))

def right_visible(i, j, grid):
    return grid[i][j] > max(grid[i][k] for k in range(j + 1, len(grid[0])))

def top_visible(i, j, grid):
    return grid[i][j] > max(grid[k][j] for k in range(0, i))

def bottom_visible(i, j, grid):
    return grid[i][j] > max(grid[k][j] for k in range(i + 1, len(grid)))

def count_interior_trees(grid):
    return sum(1 for i in range(1, len(grid) - 1) 
                 for j in range(1, len(grid[0]) - 1)
                 if left_visible(i, j, grid) or
                    right_visible(i, j, grid) or
                    top_visible(i, j, grid) or
                    bottom_visible(i, j, grid))

with fileinput.input() as fin:
    trees = [[int(c) for c in list(line.strip())] for line in fin]

outer_trees = (2 * len(trees)) + (2 * len(trees[0])) - 4
print(count_interior_trees(trees) + outer_trees)
