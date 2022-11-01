# 골드바흐의 추측

import sys
from math import sqrt

input = sys.stdin.readline


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


results = []
while True:
    n = int(input().strip())
    if n == 0:
        break

    result = [n]
    check = False
    for i in range(3, n, 2):
        if is_prime_number(i):
            j = n - i
            if is_prime_number(j):
                result.append(i)
                result.append(j)
                check = True
                break

    if not check:
        result.append(-1)
    results.append(result)

for result in results:
    if len(result) == 2:
        print("Goldbach's conjecture is wrong.")
    else:
        print("{0:d} = {1:d} + {2:d}".format(result[0], result[1], result[2]))
