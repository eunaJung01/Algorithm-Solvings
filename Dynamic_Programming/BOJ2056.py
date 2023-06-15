# 작업

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input().strip())
times = [0 for _ in range(N + 1)]
rules = defaultdict(list)

q = []
for task in range(1, N + 1):
    line = list(map(int, input().split()))
    times[task] = line[0]
    if line[1] == 0:
        continue
    for prevTask in line[2:]:
        rules[task].append(prevTask)

for task in range(1, N + 1):
    time = 0
    for prevTask in rules[task]:
        time = max(time, times[prevTask])
    times[task] += time

print(max(times))
