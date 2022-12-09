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

def scenic_score(i, j, grid):
    k, top_score = i - 1, 0
    while k >= 0 and grid[k][j] < grid[i][j]:
        top_score += 1
        k -= 1
    if k >= 0 and grid[k][j] >= grid[i][j]:
        top_score += 1
    
    k, bottom_score = i + 1, 0
    while k < len(grid) and grid[k][j] < grid[i][j]:
        bottom_score += 1
        k += 1
    if k < len(grid) and grid[k][j] >= grid[i][j]:
        bottom_score += 1
    
    k, right_score = j + 1, 0
    while k < len(grid[0]) and grid[i][k] < grid[i][j]:
        right_score += 1
        k += 1
    if k < len(grid[0]) and grid[i][k] >= grid[i][j]:
        right_score += 1

    k, left_score = j - 1, 0
    while k >= 0 and grid[i][k] < grid[i][j]:
        left_score += 1
        k -= 1
    if k >= 0 and grid[i][k] >= grid[i][j]:
        left_score += 1

    return left_score * bottom_score * right_score * top_score

def count_interior_trees(grid):
    return sum(1 for i in range(1, len(grid) - 1) 
                 for j in range(1, len(grid[0]) - 1)
                 if left_visible(i, j, grid) or
                    right_visible(i, j, grid) or
                    top_visible(i, j, grid) or
                    bottom_visible(i, j, grid))

def best_scenic_score(grid):
    return max(scenic_score(i, j, grid)
               for i in range(1, len(grid) - 1)
               for j in range(1, len(grid[0]) - 1))

with fileinput.input() as fin:
    trees = [[int(c) for c in list(line.strip())] for line in fin]

## Part 1
outer_trees = (2 * len(trees)) + (2 * len(trees[0])) - 4
print(count_interior_trees(trees) + outer_trees)

## Part 2
print(best_scenic_score(trees))
