# 최단경로

import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
start_node = int(input().strip())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

INF = 2147000000
dp = [INF for _ in range(V + 1)]


def dijkstra(start):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        u_w, u = heapq.heappop(heap)
        if dp[u] < u_w:
            continue
        for v, v_w in graph[u]:
            new_w = dp[u] + v_w
            if dp[v] > new_w:
                dp[v] = new_w
                heapq.heappush(heap, (new_w, v))


dijkstra(start_node)
for i in range(1, V + 1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
