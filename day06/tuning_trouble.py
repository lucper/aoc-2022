#!/usr/bin/env python

import fileinput

PACKET_LEN = 4
MSG_LEN = 14

with fileinput.input() as fin:
    signal = fin.readline().strip()

i = 0
while len(set(signal[i:i + MSG_LEN])) != MSG_LEN:
    i += 1

print(i + MSG_LEN)
