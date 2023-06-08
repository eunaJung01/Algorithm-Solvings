# 게임 개발

import sys
from collections import defaultdict, deque

input = sys.stdin.readline
N = int(input().strip())

times2build = [0 for _ in range(N + 1)]
rules = defaultdict(list)
inDegrees = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    times2build[i] = line[0]
    for n in line[1:-1]:
        rules[n].append(i)
        inDegrees[i] += 1

times = [0 for _ in range(N + 1)]
q = deque()
for i in range(1, N + 1):
    if inDegrees[i] == 0:
        q.append(i)

while q:
    num = q.popleft()
    times[num] += times2build[num]
    for nextNum in rules[num]:
        inDegrees[nextNum] -= 1
        times[nextNum] = max(times[nextNum], times[num])
        if inDegrees[nextNum] == 0:
            q.append(nextNum)

for time in times[1:]:
    print(time)
