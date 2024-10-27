# 치즈

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())  # n(세로) x m(가로)
cheese = [list(map(int, input().split())) for _ in range(n)]  # 치즈 O : 1 / 치즈 X : 0
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS(i, j):
    global visited
    visited[i][j] = True

    q = deque()
    q.append((i, j))

    melt = []
    status = False  # 공기 접촉 유무

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx]:
                visited[ny][nx] = True
                if cheese[ny][nx] == 0:
                    q.append((ny, nx))
                else:
                    melt.append((ny, nx))
                if ny == 0 or ny == n - 1 or nx == 0 or nx == m - 1:  # 공기 접촉
                    status = True

    if status:
        return melt
    else:
        return []


result = 0
melt_num = []
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    melt = []
    cnt = 0

    for i in range(n):
        for j in range(m):
            if cheese[i][j] == 0 and not visited[i][j]:
                melt.append(BFS(i, j))
            if cheese[i][j] == 1:
                cnt += 1

    if cnt == 0:
        break
    for c in melt:
        if c:
            melt_num.append(len(c))
            for i, j in c:
                cheese[i][j] = 0
    result += 1

print(result)
print(melt_num[-1])
