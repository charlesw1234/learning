#!/usr/bin/python
from random import random, seed, shuffle

seed()

xorbytes = map(lambda idx: int(random() * 256), range(48))
seq = range(48)
shuffle(seq)
conv = []
for idx in range(48):
    conv.append(seq[idx])
    conv.append(xorbytes[idx])

open('conv.c', 'wt').write('static const uint8_t conv[] = { %s };\n' %\
                           ', '.join(map(lambda value: str(value), conv)))
