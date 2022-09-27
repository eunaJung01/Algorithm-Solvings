# 인구 이동

import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS(y, x):
    global visited

    union = deque()
    total, cnt = 0, 0
    visited[y][x] = True

    while q:
        y, x = q.popleft()
        union.append((y, x))
        cnt += 1
        total += people[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if L <= abs(people[y][x] - people[ny][nx]) <= R:
                    visited[ny][nx] = True
                    q.append((ny, nx))

    while union:
        y, x = union.popleft()
        people[y][x] = total // cnt

    if cnt == 1:
        return 0
    return 1


result = 0
while True:
    q = deque()
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                q.append((i, j))
                cnt += BFS(i, j)
    if cnt == 0:
        break
    else:
        result += 1
print(result)
