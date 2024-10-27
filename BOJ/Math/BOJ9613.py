# GCD 합

import sys
from math import gcd

t = int(input())

numList_list = []
for i in range(t):
    numList_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(t):
    result = 0
    for j in range(1, numList_list[i][0] + 1):
        for k in range(j + 1, numList_list[i][0] + 1):
            result += gcd(numList_list[i][j], numList_list[i][k])
    print(result)
