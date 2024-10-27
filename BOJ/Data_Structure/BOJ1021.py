# 회전하는 큐

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
targets = list(map(int, input().split()))

numbers = deque([i for i in range(1, N + 1)])
cnt = 0

for target in targets:
    out_idx = numbers.index(target)

    if target == numbers[0]:
        numbers.popleft()
    else:
        half_idx = int(len(numbers) // 2)
        if out_idx <= half_idx:
            numbers.rotate(-out_idx)
            cnt += out_idx
        else:
            numbers.rotate(len(numbers) - out_idx)
            cnt += len(numbers) - out_idx
        numbers.popleft()

print(cnt)
