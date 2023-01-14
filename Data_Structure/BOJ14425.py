# 문자열 집합

import sys

N, M = map(int, sys.stdin.readline().split())
S = []
lines = []

for _ in range(N):
    S.append(sys.stdin.readline())
for _ in range(M):
    lines.append(sys.stdin.readline())

S = set(S)  # HashSet
count = 0

for line in lines:
    if line in S:
        count += 1

print(count)
