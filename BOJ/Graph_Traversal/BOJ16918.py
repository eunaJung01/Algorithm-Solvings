# 봄버맨

import sys
from collections import deque

input = sys.stdin.readline

R, C, N = map(int, input().split())
map = []
empty = deque()
bomb = deque()

for i in range(R):
    line = list(input().strip())
    temp = []
    for j in range(C):
        if line[j] == "O":
            temp.append(["O", 0])
            bomb.append((i, j))
        else:
            temp.append([".", 0])
            empty.append((i, j))
    map.append(temp)

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

if N != 1:
    now = 1
    while True:
        now += 1
        for _ in range(len(empty)):
            y, x = empty.popleft()
            if map[y][x][0] == ".":
                map[y][x] = ["O", now]
                bomb.append((y, x))
        if N > 4 and now == (N % 4) + 4:
            break
        else:
            if now == N:
                break

        now += 1
        for _ in range(len(bomb)):
            y, x = bomb.popleft()
            if map[y][x][0] == "O":
                if map[y][x][1] == now - 3:
                    map[y][x] = [".", 0]
                    empty.append((y, x))
                    for n in range(4):
                        ny = y + dy[n]
                        nx = x + dx[n]
                        if 0 <= ny < R and 0 <= nx < C and map[ny][nx][0] == "O" and map[ny][nx][1] != now - 3:
                            map[ny][nx] = [".", 0]
                            empty.append((ny, nx))
                else:
                    bomb.append((y, x))
        if N > 4 and now == (N % 4) + 4:
            break
        else:
            if now == N:
                break

for row in map:
    for r, num in row:
        print(r, end="")
    print()
