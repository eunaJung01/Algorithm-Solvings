# 단지번호붙이기

import sys
from collections import deque

N = int(sys.stdin.readline().strip())

house = []
for _ in range(N):
    house.append(list(map(int, sys.stdin.readline().strip())))

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def BFS(r, c):
    global house
    house[r][c] = 0
    count = 1

    q = deque([])
    q.append([r, c])

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and house[ny][nx] == 1:
                count += 1
                house[ny][nx] = 0
                q.append([ny, nx])

    return count


count = []
for i in range(N):
    for j in range(N):
        if house[i][j] == 1:
            count.append(BFS(i, j))

count.sort()
print(len(count))
for c in count:
    print(c)
