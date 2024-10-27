# 숨바꼭질 3

# BFS

# import copy
# import sys
# from collections import deque
#
# N, K = map(int, sys.stdin.readline().split())
#
# MAX = 100000
# line = [False for _ in range(MAX + 1)]
# result = 0
#
#
# def BFS(N):
#     line[N] = True
#     q1 = deque()  # 최상위 우선순위 (순간이동)
#     q2 = deque()
#     q1.append((N, 0))
#
#     while q1:
#         cur, num = q1.popleft()
#         if cur == K:
#             return num
#
#         # 순간이동
#         x = cur * 2
#         if x <= MAX and not line[x]:
#             q1.append((x, num))
#             line[x] = True
#
#         # 걷기 + 1
#         x = cur + 1
#         if x <= MAX and not line[x]:
#             q2.append((x, num + 1))
#             line[x] = True
#
#         # 걷기 - 1
#         x = cur - 1
#         if x >= 0 and not line[x]:
#             q2.append((x, num + 1))
#             line[x] = True
#
#         if len(q1) == 0:
#             q1 = copy.deepcopy(q2)
#             q2 = deque()
#
#
# if N != K:
#     result = BFS(N)
# print(result)

# ---

# Dijkstra

import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
MAX = 100000
INF = 2147000000


def dijkstra():
    line = [INF] * (MAX + 1)  # x에 도달하는데까지 걸리는 최소 시간을 저장
    line[N] = 0
    heap = []
    heapq.heappush(heap, (N, 0))  # N, time

    while heap:
        cur, t = heapq.heappop(heap)
        for nx, w in [(cur + 1, 1), (cur - 1, 1), (cur * 2, 0)]:  # 이동할 위치, 가중치
            if 0 <= nx < MAX + 1 and line[nx] > t + w:
                line[nx] = t + w
                heapq.heappush(heap, (nx, line[nx]))

    print(line[K])


dijkstra()
