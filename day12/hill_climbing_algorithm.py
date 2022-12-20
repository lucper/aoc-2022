#!/usr/bin/env python

import fileinput
from string import ascii_lowercase

START = 'S' # elevation 'a'
END = 'E'   # elevation 'z'
## TODO: need to treat E as z

def are_neighbors(x, y):
    if x == END:
        x = 'z'
    if y == END:
        y = 'z'
    return (abs(ord(x) - ord(y)) <= 1 and x in ascii_lowercase and y in ascii_lowercase)

def get_neighbors(grid, pos):
    i, j = pos
    neighbors = []
    # up
    if i - 1 >= 0 and are_neighbors(grid[i - 1][j], grid[i][j]):
        neighbors.append((i - 1, j))
    # down
    if i + 1 < len(grid) and are_neighbors(grid[i + 1][j], grid[i][j]):
        neighbors.append((i + 1, j))
    # left
    if j - 1 >= 0 and are_neighbors(grid[i][j - 1], grid[i][j]):
        neighbors.append((i, j - 1))
    # right
    if j + 1 < len(grid[0]) and are_neighbors(grid[i][j + 1], grid[i][j]):
        neighbors.append((i, j + 1))
    return neighbors

def search(grid, start):
    parent = {start: None}
    visited = {start}
    q = [start]
    while q:
        i, j = q.pop(0)
        if grid[i][j] == END:
            print(f'reached goal at ({i}, {j})!')
            goal = (i, j)
            break
        for v in get_neighbors(grid, (i, j)):
            if v not in visited:
                visited.add(v)
                q.append(v)
                parent[v] = (i, j)

                i, j = v
                print(f'{grid[i][j]}: {v}')
    curr = goal
    path = [goal]
    while curr := parent[curr]:
        path.append(curr)
    print(list(reversed(path)))
    print(len(list(path)))

def get_start_pos(grid):
    return ((i, j) for i, row in enumerate(grid)
                   for j, col in enumerate(row)
                   if col == START)

if __name__ == '__main__':
    with fileinput.input() as fin:
        puzzle = [list(line.strip()) for line in fin]

    # can be better
    i, j = next(get_start_pos(puzzle))
    puzzle[i][j] = 'a'

    search(puzzle, (i, j))
