# ACM Craft

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().split())
    buildingTimes = [0] + list(map(int, input().split()))

    inDegrees = [0 for _ in range(N + 1)]
    rules = defaultdict(list)
    for _ in range(K):
        X, Y = map(int, input().split())
        rules[X].append(Y)
        inDegrees[Y] += 1

    target = int(input().strip())

    q = deque()
    for num in range(1, N + 1):
        if inDegrees[num] == 0:
            q.append(num)

    times = [0 for _ in range(N + 1)]
    while q:
        num = q.popleft()
        times[num] += buildingTimes[num]
        for nextNum in rules[num]:
            times[nextNum] = max(times[num], times[nextNum])
            inDegrees[nextNum] -= 1
            if inDegrees[nextNum] == 0:
                q.append(nextNum)

    print(times[target])
