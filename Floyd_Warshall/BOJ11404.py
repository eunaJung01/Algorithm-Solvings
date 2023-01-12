# 플로이드

# 다익스트라
# import sys
# import heapq
#
# input = sys.stdin.readline
#
# n, m = int(input().strip()), int(input().strip())
#
#
# def add_bus(a, b, c):
#     global buses
#     for i, w in buses[a]:
#         if i == a:
#             if c < w:
#                 buses[a][i] = c
#                 return
#             else:
#                 return
#     buses[a].append([b, c])
#
#
# buses = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     add_bus(a, b, c)
#
#
# def dijkstra(start, end):
#     visited = [False for _ in range(n + 1)]
#     visited[start] = True
#
#     heap = []
#     for b, c in buses[start]:
#         heapq.heappush(heap, (c, b))
#
#     while heap:
#         w, a = heapq.heappop(heap)
#         if a == end:
#             return w
#         for b, c in buses[a]:
#             if not visited[b]:
#                 heapq.heappush(heap, (w + c, b))
#                 visited[b] = True
#     return 0
#
#
# result = [[] for _ in range(n)]
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             result[i - 1].append(0)
#         else:
#             result[i - 1].append(dijkstra(i, j))
#
# for row in result:
#     for r in row:
#         print(r, end=' ')
#     print()

# ---

import sys

input = sys.stdin.readline

n, m = int(input().strip()), int(input().strip())

INF = int(1e10)
buses = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    buses[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    buses[a][b] = min(buses[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a != b:
                if buses[a][b] > buses[a][k] + buses[k][b]:
                    buses[a][b] = buses[a][k] + buses[k][b]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b or buses[a][b] == INF:
            print(0, end=' ')
            continue
        print(buses[a][b], end=' ')
    print()
