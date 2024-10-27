# 수리공 항승

import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
holes = deque(holes)

result = 0
while holes:
    hole = holes.popleft()
    result += 1
    while True:
        if not holes:
            break
        if holes[0] < hole + L:
            holes.popleft()
        else:
            break

print(result)
