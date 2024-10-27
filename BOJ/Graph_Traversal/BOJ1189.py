# 컴백홈

import sys

input = sys.stdin.readline

R, C, K = map(int, input().split())

map = []
for _ in range(R):
    line = input().strip()
    temp = []
    for l in line:
        if l == "T":
            temp.append(1)
        else:
            temp.append(0)
    map.append(temp)

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
status = [[False for _ in range(C)] for _ in range(R)]
status[R - 1][0] = True


def DFS(y, x, n):
    global result

    if n == K:
        if y == 0 and x == C - 1:
            result += 1
            return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < R and 0 <= nx < C and map[ny][nx] == 0 and not status[ny][nx]:
            status[ny][nx] = True
            DFS(ny, nx, n + 1)
            status[ny][nx] = False


result = 0
DFS(R - 1, 0, 1)
print(result)
