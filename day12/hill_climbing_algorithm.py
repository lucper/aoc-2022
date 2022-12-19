#!/usr/bin/env python

import fileinput

def get_neighbors(grid, pos):
    i, j = pos
    neighbors = []
    # up
    if i - 1 >= 0 and ord(grid[i - 1][j]) - ord(grid[i][j]) <= 1:
        neighbors.append((i - 1, j))
    # down
    if i + 1 < len(grid) and ord(grid[i + 1][j]) - ord(grid[i][j]) <= 1:
        neighbors.append((i + 1, j))
    # left
    if j - 1 >= 0 and ord(grid[i][j - 1]) - ord(grid[i][j]) <= 1:
        neighbors.append((i, j - 1))
    # right
    if j + 1 < len(grid[0]) and ord(grid[i][j + 1]) - ord(grid[i][j]) <= 1:
        neighbors.append((i, j + 1))
    return neighbors

def search(grid, start=(0, 0)):
    pass 
    
if __name__ == '__main__':
    with fileinput.input() as fin:
        puzzle = [list(line.strip()) for line in fin]

    ## TODO: start is always 'S' and end is always 'E'
    print(puzzle[1][0])
    print(get_neighbors(puzzle, (1,0)))
