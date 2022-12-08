#!/usr/bin/env python

import fileinput

class Dir:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        self.size = 0
    def __repr__(self):
        return f'<{self.name} {self.size} {self.pos}>'
    def __hash__(self):
        return self.pos
    def __eq__(self, other):
        return self.pos == other.pos and \
                self.name == other.name and \
                self.size == other.size

stack = []
visited = set()

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
        print(stack, visited)
    print(sum(d.size for d in visited if d.size <= 100000))
