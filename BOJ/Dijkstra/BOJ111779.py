# 최소비용 구하기 2

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n = int(input().strip())  # 도시의 개수
m = int(input().strip())  # 버스의 개수

buses = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    buses[a].append((b, w))
start, end = map(int, input().split())

INF = int(10e9)


def dijkstra(start, end):
    costs = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

    q = []
    for next_city, next_w in buses[start]:
        costs[start][next_city] = next_w
        heapq.heappush(q, (next_w, next_city, [start, next_city]))

    while q:
        cur_w, cur_city, route = heapq.heappop(q)
        if cur_city == end:
            return cur_w, route
        for next_city, next_w in buses[cur_city]:
            if costs[cur_city][next_city] > cur_w + next_w:
                costs[cur_city][next_city] = cur_w + next_w
                heapq.heappush(q, (cur_w + next_w, next_city, route + [next_city]))


min_cost, min_route = dijkstra(start, end)

print(min_cost)
print(len(min_route))
for r in min_route:
    print(r, end=' ')
