# 서로소 평균

import sys
from math import gcd

N = int(input())
A_list = list(map(int, sys.stdin.readline().split()))
X = int(input())

add = 0
count = 0
for A in A_list:
    if gcd(A, X) == 1:
        add += A
        count += 1

print(add / count)
