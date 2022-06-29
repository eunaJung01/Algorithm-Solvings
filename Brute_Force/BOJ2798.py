# 블랙잭

import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().strip().split())  # N : 카드의 개수 / M : 합
numList = list(map(int, sys.stdin.readline().strip().split()))

perm = list(map(list, permutations(numList, 3)))
# print(perm)

result = 0
for p in perm:
    sum_p = p[0] + p[1] + p[2]

    if abs(sum_p - M) <= abs(result - M):  # M에 더 가까울 경우에만
        if sum_p <= M:
            result = sum_p

print(result)
