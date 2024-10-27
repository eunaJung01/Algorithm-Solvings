# 상범 빌딩

import sys
from collections import deque

input = sys.stdin.readline

# 동, 서, 남, 북, 상, 하
dz = (0, 0, 0, 0, 1, -1)  # 층
dy = (0, 0, 1, -1, 0, 0)  # 행
dx = (1, -1, 0, 0, 0, 0)  # 열


def BFS(start, end):
    global building, L, R, C

    q = deque()
    q.append((start[0], start[1], start[2], 0))

    visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visited[start[0]][start[1]][start[2]] = True

    while q:
        z, y, x, t = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < L and 0 <= ny < R and 0 <= nx < C and not visited[nz][ny][nx] and (
                    building[nz][ny][nx] == "." or building[nz][ny][nx] == "E"):
                if nz == end[0] and ny == end[1] and nx == end[2]:
                    return True, t + 1
                visited[nz][ny][nx] = True
                q.append((nz, ny, nx, t + 1))
    return False, 0


result = []
while True:
    L, R, C = map(int, input().split())  # 층, 행, 열
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    start, end = (0, 0, 0), (0, 0, 0)
    for i in range(L):
        floor = []
        for j in range(R):
            line = input().strip()
            for k, cell in enumerate(line):
                if cell == 'S':
                    start = (i, j, k)
                elif cell == 'E':
                    end = (i, j, k)
            floor.append(line)
        temp = input()  # 층 입력 사이의 한 줄
        building.append(floor)

    status, x = BFS(start, end)
    if status:
        result.append("Escaped in " + str(x) + " minute(s).")
    else:
        result.append("Trapped!")

for r in result:
    print(r)
