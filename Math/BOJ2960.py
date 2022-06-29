# 에라토스테네스의 체

import sys
from math import sqrt

N, K = map(int, sys.stdin.readline().split())


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


numList = [i for i in range(2, N + 1)]  # 2 ~ N 모든 정수
delete = []

i = 0
while len(numList) != 0:
    if is_prime_number(numList[i]):
        prime = numList[i]
        delete.append(prime)
        numList.remove(prime)

        for j in numList:
            if j % prime == 0:
                delete.append(j)
                numList.remove(j)
    else:
        i += 1

print(delete[K - 1])
