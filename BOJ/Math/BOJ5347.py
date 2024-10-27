# LCM

import sys
from math import lcm

n = int(input())

for i in range(n):
    num1, num2 = map(int, sys.stdin.readline().split())
    print(lcm(num1, num2))
