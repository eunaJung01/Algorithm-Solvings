# 단어 격자

# 메모리 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# H, W, L = map(int, input().split())  # H : 높이 / W : 너비 / L : 단어의 길이
#
# grid = [input().strip() for _ in range(H)]
# target = input().strip()
#
# # 8방향
# dy = (-1, -1, 0, 1, 1, 1, 0, -1)
# dx = (0, -1, -1, -1, 0, 1, 1, 1)
#
#
# def BFS(y, x):
#     q = deque()
#     q.append((y, x, 1))
#     cnt = 0
#
#     while q:
#         y, x, idx = q.popleft()
#         for i in range(8):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] == target[idx]:
#                 if idx + 1 == len(target):
#                     cnt += 1
#                 else:
#                     q.append((ny, nx, idx + 1))
#
#     return cnt
#
#
# result = 0
# for i in range(H):
#     for j in range(W):
#         if grid[i][j] == target[0]:
#             result += BFS(i, j)
# print(result)

# ---

# 왜 틀린거지???
# import sys
#
# input = sys.stdin.readline
#
# H, W, L = map(int, input().split())  # H : 높이 / W : 너비 / L : 단어의 길이
#
# grid = [input().strip() for _ in range(H)]
# target = input().strip()
#
# idx = {}  # target 알파벳 순서
# for i, t in enumerate(target):
#     if t in idx:
#         idx[t].append(i)
#     else:
#         idx[t] = [i]
#
# idx_grid = [[[] for _ in range(W)] for _ in range(H)]  # target 알파벳 중 몇 번째에 속하는지 저장
# pos = {}  # target 알파벳 별 격자 상 위치
# for i in range(H):
#     for j in range(W):
#         if grid[i][j] in idx:
#             idx_grid[i][j] = idx[grid[i][j]]
#             if grid[i][j] in pos:
#                 pos[grid[i][j]].append((i, j))
#             else:
#                 pos[grid[i][j]] = [(i, j)]
#
# # 8방향
# dy = (-1, -1, 0, 1, 1, 1, 0, -1)
# dx = (0, -1, -1, -1, 0, 1, 1, 1)
#
# dp = [[0 for _ in range(W)] for _ in range(H)]
# for y, x in pos[target[0]]:
#     dp[y][x] = 1
#
# for idx, t in enumerate(target[:-1]):
#     temp = [[0 for _ in range(W)] for _ in range(H)]
#
#     for y, x in pos[t]:
#         for i in range(8):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < H and 0 <= nx < W:
#                 for num in idx_grid[ny][nx]:
#                     if num == idx + 1:
#                         temp[ny][nx] += dp[y][x]
#                         break
#
#     for i in range(H):
#         for j in range(W):
#             dp[i][j] = max(dp[i][j], temp[i][j])
#
# # for row in idx_grid:
# #     print(row)
# # for row in dp:
# #     print(row)
#
# result = 0
# for y, x in pos[target[-1]]:
#     result += dp[y][x]
# print(result)

# ---

import sys

input = sys.stdin.readline

H, W, L = map(int, input().split())  # H : 높이 / W : 너비 / L : 단어의 길이

grid = [input().strip() for _ in range(H)]
target = input().strip()

# # 8방향
dy = (-1, -1, 0, 1, 1, 1, 0, -1)
dx = (0, -1, -1, -1, 0, 1, 1, 1)

dp = [[[-1 for _ in range(100)] for _ in range(W)] for _ in range(H)]


def DFS(y, x, depth):
    if depth == L - 1:
        dp[y][x][depth] = 1
        return

    val = 0
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < H and 0 <= nx < W:
            if grid[ny][nx] == target[depth + 1]:
                if dp[ny][nx][depth + 1] == -1:
                    DFS(ny, nx, depth + 1)
                val += dp[ny][nx][depth + 1]
    dp[y][x][depth] = val


result = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == target[0]:
            DFS(i, j, 0)
            result += dp[i][j][0]
print(result)
