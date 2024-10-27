# 신아를 만나러

import sys
from collections import deque

input = sys.stdin.readline

X, Y, N = map(int, input().split())

pool_y = []
pool_x = []
for _ in range(N):
    temp = list(map(int, input().split()))
    pool_y.append(temp[1])
    pool_x.append(temp[0])

# 정규화 작업이 필요!
ty, tx = 1, 1

if min(pool_y) < 0:
    ty += abs(min(pool_y))
else:
    ty += 1
if min(pool_y) < 0:
    tx += abs(min(pool_x))
else:
    tx += 1

for i in range(N):
    pool_y[i] += ty
    pool_x[i] += tx
Y += ty
X += tx
n = max(pool_y) + ty
m = max(pool_x) + tx

map = [[0 for _ in range(m)] for _ in range(n)]
for i in range(N):
    map[pool_y[i]][pool_x[i]] = 1
map[Y][X] = 2

status = [[False for _ in range(m)] for _ in range(n)]
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS(y, x):
    cnt = 0
    q = deque()
    q.append((y, x, cnt))

    result = 0
    while q:
        if result != 0:
            break
        else:
            y, x, cnt = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m and map[ny][nx] != 1 and not status[ny][
                    nx]:
                    status[ny][nx] = True
                    if map[ny][nx] == 2:
                        result = cnt + 1
                        break
                    q.append((ny, nx, cnt + 1))

    return result


print(BFS(ty, tx))
