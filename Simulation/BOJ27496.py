# 발머의 피크 이론

import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
alcohols = list(map(int, input().split()))

q = deque()
fever_time, blood_alcohol_level = 0, 0
idx = 0

while idx < min(N, L):
    q.append(alcohols[idx])
    blood_alcohol_level += alcohols[idx]

    if 129 <= blood_alcohol_level <= 138:
        fever_time += 1
    idx += 1

while idx < N:
    alcohol = q.popleft()
    blood_alcohol_level -= alcohol

    q.append(alcohols[idx])
    blood_alcohol_level += alcohols[idx]

    if 129 <= blood_alcohol_level <= 138:
        fever_time += 1
    idx += 1

print(fever_time)
