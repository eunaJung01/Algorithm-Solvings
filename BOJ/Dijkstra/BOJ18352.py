# 특정 거리의 도시 찾기

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M, K, X = map(int, input().split())

INF = int(1e10)
dp = [INF for _ in range(N + 1)]

roads = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())
    roads[A].append(B)


def dijkstra():
    q = []
    heapq.heappush(q, X)
    dp[X] = 0

    while q:
        x = heapq.heappop(q)
        if x in roads:
            for next_x in roads[x]:
                if dp[x] + 1 < dp[next_x]:
                    dp[next_x] = dp[x] + 1
                    heapq.heappush(q, next_x)


if X not in roads:
    print(-1)
else:
    dijkstra()
    cnt = 0
    for i, d in enumerate(dp):
        if d == K:
            print(i)
            cnt += 1
    if cnt == 0:
        print(-1)
