# 빵집

# 시간 초과
# import sys
# import heapq
#
# input = sys.stdin.readline
#
# R, C = map(int, input().split())
#
# grid = [[0 for _ in range(C)] for _ in range(R)]
# for y in range(R):
#     row = input().strip()
#     for x in range(C):
#         if row[x] == "x":
#             grid[y][x] = -1
#
#
# def addPipe(path):
#     global grid
#     for y, x in path:
#         grid[y][x] = -1
#
#
# # 우선 순위 : 오른쪽 위(1) > 가운데(2) > 오른쪽 아래(3)
# def BFS(y):
#     visited = [[False for _ in range(C)] for _ in range(R)]
#     visited[y][0] = True
#     q = []
#     heapq.heappush(q, (0, [(y, 0)]))  # 우선 순위, [경로]
#
#     while q:
#         score, path = heapq.heappop(q)
#         last_path_y, last_path_x = path[-1][0], path[-1][1]
#         if last_path_x == C - 1:
#             addPipe(path)
#             return 1
#         for w, dy, dx in ((1, -1, 1), (2, 0, 1), (3, 1, 1)):
#             ny, nx = last_path_y + dy, last_path_x + dx
#             if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == 0 and not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 heapq.heappush(q, (score + w, path + [(ny, nx)]))
#     return 0
#
#
# result = 0
# for y in range(R):
#     if grid[y][0] == 0:
#         result += BFS(y)
# print(result)

# ---

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

grid = [[0 for _ in range(C)] for _ in range(R)]
for y in range(R):
    row = input().strip()
    for x in range(C):
        if row[x] == "x":
            grid[y][x] = -1


def DFS(y, x):
    global visited, result
    if x == C - 1:
        return True
    for dy, dx in ((-1, 1), (0, 1), (1, 1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == 0 and not visited[ny][nx]:
            visited[ny][nx] = True
            if DFS(ny, nx):
                return True


result = 0
visited = [[False for _ in range(C)] for _ in range(R)]
for y in range(R):
    if grid[y][0] == 0 and DFS(y, 0):
        result += 1
print(result)
