# 분수 합

import sys
from math import lcm, gcd

input = sys.stdin.readline

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

B3 = lcm(B1, B2)
A3 = (B3 // B1) * A1 + (B3 // B2) * A2
d = gcd(A3, B3)

print(A3 // d, B3 // d)
