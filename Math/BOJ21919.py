# 소수 최소 공배수

import sys
from math import sqrt
from math import lcm


def is_prime_number(x):
    if x == 0 and x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


N = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

primeNum_list = []
for num in num_list:
    if is_prime_number(num):
        primeNum_list.append(num)

if len(primeNum_list) == 0:
    print(-1)
else:
    result_lcm = primeNum_list[0]
    idx = 1
    for _ in range(len(primeNum_list) - 1):
        result_lcm = lcm(result_lcm, primeNum_list[idx])
        idx += 1
    print(result_lcm)
