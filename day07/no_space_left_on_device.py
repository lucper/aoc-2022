#!/usr/bin/env python

import fileinput

DISK_SPACE = 70_000_000
REQ_SPACE = 30_000_000

class Dir:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.size = 0
    def __hash__(self):
        return self.pos
    def __eq__(self, other):
        return self.pos == other.pos and \
                self.name == other.name and \
                self.size == other.size

stack = []
visited = set()

## I assume this never happens:
##   $ cd a
##   $ cd ..
##   $ cd a
##   $ ls
## Otherwise, there would be two "different" directories 'a'
## that should be the same.
with fileinput.input() as fin:
    for line in fin:
        match line.strip().split():
            case ['$', 'cd', '..']:
                if stack:
                    top = stack.pop()
                    if top not in visited:
                        visited.add(top)
                        stack[-1].size += top.size
            case ['$', 'cd', dir_name]:
                stack.append(Dir(dir_name, len(stack)))
            case ['$', 'ls']:
                pass
            case ['dir', _]:
                pass
            case [file_size, file_name]:
                stack[-1].size += int(file_size)

## root is never "visited", but it always has size > 100_000
print(sum(d.size for d in visited if d.size <= 100_000))

## Part 2
unused_space = DISK_SPACE - sum(d.size for d in stack)
print(min(d.size for d in visited if d.size >= REQ_SPACE - unused_space))
