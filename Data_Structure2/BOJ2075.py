# N번째 큰 수

import sys
import heapq

N = int(sys.stdin.readline().strip())  # N*N개의 수들 중 N번째로 큰 수 찾기

heap = []  # 최소 힙
for _ in range(N):
    numList = list(map(int, sys.stdin.readline().split()))

    for num in numList:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:  # heap 최솟값 < 읽은 값 -> 최솟값 pop, 읽은 값 push
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])
