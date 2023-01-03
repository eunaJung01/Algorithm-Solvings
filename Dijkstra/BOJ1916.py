# 최소비용 구하기

import sys
import heapq

input = sys.stdin.readline
INF = 2147000000

N, M = int(input().strip()), int(input().strip())
dp = [INF for _ in range(N + 1)]

buses = [[] for i in range(N + 1)]
for _ in range(M):
    A, B, W = map(int, input().split())  # 출발 도시, 도착 도시, 비용
    buses[A].append([B, W])

start_city, end_city = map(int, input().split())


def dijkstra(start):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (start, 0))

    while heap:
        u, w = heapq.heappop(heap)
        if dp[u] < w:
            continue
        for v, v_w in buses[u]:
            new_w = w + v_w
            if dp[v] > new_w:
                dp[v] = new_w
                heapq.heappush(heap, (v, new_w))


dijkstra(start_city)
print(dp[end_city])
