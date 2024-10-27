# 숨바꼭질 6

import math
import sys

input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split()))

dist = set()
for a in A:
    dist.add(abs(S - a))
dist = list(dist)
dist.sort()

result = abs(A[0] - S)
for d in dist:
    result = math.gcd(result, d)
print(result)
