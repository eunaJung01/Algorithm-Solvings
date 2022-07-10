# 최소 힙

import heapq
import sys

N = int(sys.stdin.readline().strip())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline().strip()))

q = []
result = []
for l in lst:
    if l == 0:
        if len(q) != 0:
            result.append(heapq.heappop(q))
        else:
            result.append(0)

    else:
        heapq.heappush(q, l)

for r in result:
    print(r)
