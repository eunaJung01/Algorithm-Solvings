# 최소공배수

import sys
from math import lcm

T = int(sys.stdin.readline())

for i in range(T):
    numList = list(map(int, sys.stdin.readline().split()))
    print(lcm(numList[0], numList[1]))
