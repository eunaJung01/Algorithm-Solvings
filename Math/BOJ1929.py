# 소수 구하기

import sys
from math import sqrt

M, N = map(int, sys.stdin.readline().split())


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


for num in range(M, N+1):
    if is_prime_number(num):
        print(num)
