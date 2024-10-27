# 최대 힙

import sys
import heapq

N = int(sys.stdin.readline().strip())

heap = []
result = []

for _ in range(N):
    num = int(sys.stdin.readline().strip())

    if num == 0:
        if len(heap) == 0:
            result.append(0)
        else:
            result.append(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-num, num))

for r in result:
    print(r)
