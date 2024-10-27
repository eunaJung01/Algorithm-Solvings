# 벽 부수고 이동하기

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())  # 행, 열
board = [input().strip() for _ in range(N)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
INF = int(1e9)


def BFS():
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]  # 벽을 뚫지 않고 온 경우, 벽을 뚫고 온 경우
    visited[0][0][0] = 1
    q = deque()
    q.append((0, 0, 0))  # y, x, 벽 부순 유무

    while q:
        y, x, wall = q.popleft()
        if y == N - 1 and x == M - 1:
            return visited[y][x][wall]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx][wall] == 0:
                if board[ny][nx] == "0":
                    q.append((ny, nx, wall))
                    visited[ny][nx][wall] = visited[y][x][wall] + 1
                if wall == 0 and board[ny][nx] == "1":
                    q.append((ny, nx, 1))
                    visited[ny][nx][1] = visited[y][x][wall] + 1
    return -1


print(BFS())
