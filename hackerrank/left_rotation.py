#!/bin/python

import math
import os
import random
import re
import sys

def rotateArray(n,d,a):
    if d > n:
        mod_rotation = d%n
    else:
        mod_rotation = d
    a1 = [0] * n
    for i in range(1,n+1):
        a1[i-1] = a[i + mod_rotation -1 -n]

    print(' '.join(str(e) for e in a1))

if __name__ == '__main__':
    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())
    rotateArray(n,d,a)