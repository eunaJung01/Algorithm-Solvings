# 알고스팟

# 틀렸습니다

# import copy
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# M, N = map(int, input().split())  # 가로 M, 세로 N
#
# maze = [list(map(int, input().strip())) for _ in range(N)]
# visited = [[False for _ in range(M)] for _ in range(N)]
#
# dy = (0, 1, 0, -1)
# dx = (1, 0, -1, 0)
#
# M -= 1
# N -= 1
#
# result = []
#
#
# def BFS(start_y, start_x):
#     q1, q2 = deque(), deque()
#     q1.append((start_y, start_x, 0))
#     visited[start_y][start_x] = True
#
#     while q1:
#         print("---")
#         print(q1)
#         print(q2)
#         y, x, cnt = q1.popleft()
#
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny <= N and 0 <= nx <= M and not visited[ny][nx]:
#                 if ny == N and nx == M:
#                     print(cnt)
#                     return
#                 visited[ny][nx] = True
#
#                 if maze[ny][nx] == 0:
#                     q1.append((ny, nx, cnt))
#                     continue
#                 else:
#                     q2.append((ny, nx, cnt + 1))
#
#                 if len(q1) == 0 and len(q2) != 0:
#                     q1 = copy.deepcopy(q2)
#                     q2 = deque()
#
#
# BFS(0, 0)

"""
반례

23 3
00101110111000000110100
01001111101010010001100
11000001010110010110000

답 : 5
출력 : 7
"""

# ---

import sys
import heapq

input = sys.stdin.readline

INF = 2147000000
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

M, N = map(int, input().split())  # 가로 M, 세로 N
maze = [list(map(int, input().strip())) for _ in range(N)]
block = [[INF for _ in range(M)] for _ in range(N)]


def dijkstra(start_y, start_x):
    heap = []
    heapq.heappush(heap, (start_y, start_x))
    block[start_y][start_x] = 0

    while heap:
        y, x = heapq.heappop(heap)

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and block[ny][nx] > block[y][x] + maze[ny][nx]:
                block[ny][nx] = block[y][x] + maze[ny][nx]
                heapq.heappush(heap, (ny, nx))


dijkstra(0, 0)
print(block[N - 1][M - 1])
