# 탈출

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
end_y, end_x = 0, 0
forest = []
q = deque()

for y in range(R):
    line = list(input().strip())
    for x in range(C):
        if line[x] == "D":
            end_y, end_x = y, x
        elif line[x] == "S":
            q.append((y, x))
    forest.append(line)

for y in range(R):
    for x in range(C):
        if forest[y][x] == "*":
            q.append((y, x))

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS():
    cnt = [[0 for _ in range(C)] for _ in range(R)]
    while q:
        if forest[end_y][end_x] == "S":
            return cnt[end_y][end_x]
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if forest[y][x] == "S" and (forest[ny][nx] == "." or forest[ny][nx] == "D"):
                    forest[ny][nx] = "S"
                    cnt[ny][nx] = cnt[y][x] + 1
                    q.append((ny, nx))
                elif forest[y][x] == "*" and (forest[ny][nx] == "." or forest[ny][nx] == "S"):
                    forest[ny][nx] = "*"
                    q.append((ny, nx))
    return "KAKTUS"


print(BFS())
