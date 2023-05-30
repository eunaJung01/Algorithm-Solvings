# 알파벳

# DFS

import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

visited = [[False for _ in range(C)] for _ in range(R)]
hasMetAlpha = [False for _ in range(26)]  # A(65) ~ Z(90)

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def DFS(y, x, cnt):
    global result

    temp = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
            a = ord(board[ny][nx]) - 65
            if not hasMetAlpha[a]:
                temp += 1
                visited[ny][nx] = True
                hasMetAlpha[a] = True
                if DFS(ny, nx, cnt + 1) == -1:
                    result = max(result, cnt + 1)
                hasMetAlpha[a] = False
                visited[ny][nx] = False
    if temp == 0:
        return -1


result = 1
visited[0][0] = True
hasMetAlpha[ord(board[0][0]) - 65] = True
DFS(0, 0, 1)
print(result)

# ---

# BFS

import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS():
    global result
    q = {(0, 0, board[0][0])}

    while q:
        y, x, alphas = q.pop()
        result = max(result, len(alphas))

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and board[ny][nx] not in alphas:
                q.add((ny, nx, board[ny][nx] + alphas))


result = 1
BFS()
print(result)
