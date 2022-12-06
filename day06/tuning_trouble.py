#!/usr/bin/env python

import fileinput

PACKET_LEN = 4
MSG_LEN = 14

with fileinput.input() as fin:
    signal = fin.readline().strip()

for i, _ in enumerate(signal[:-(MSG_LEN - 1)]):
    if len(set(signal[i:i + MSG_LEN])) == MSG_LEN:
        print(i + MSG_LEN)
        break
