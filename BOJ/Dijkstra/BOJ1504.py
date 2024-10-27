# 특정한 최단 경로

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

INF = sys.maxsize

N, E = map(int, input().split())
nodes = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    nodes[a].append((c, b))
    nodes[b].append((c, a))
v1, v2 = map(int, input().split())


def dijkstra(start):
    dp = [INF for _ in range(N + 1)]
    dp[start] = 0

    h = []
    heapq.heappush(h, (0, start))

    while h:
        w, node = heapq.heappop(h)
        for nw, n in nodes[node]:
            if dp[node] + nw < dp[n]:
                dp[n] = dp[node] + nw
                heapq.heappush(h, (dp[n], n))
    return dp


one = dijkstra(1)
v1_ = dijkstra(v1)
v2_ = dijkstra(v2)
result = min(one[v1] + v1_[v2] + v2_[N], one[v2] + v2_[v1] + v1_[N])
print(result if result < INF else -1)
