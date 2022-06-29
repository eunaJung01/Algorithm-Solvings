# 소수 찾기

import sys
from math import sqrt

N = int(input())
numList = list(map(int, sys.stdin.readline().split()))


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


count = 0
for j in numList:
    if is_prime_number(j):
        count += 1

print(count)
