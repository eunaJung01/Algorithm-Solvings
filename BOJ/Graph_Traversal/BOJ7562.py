# 나이트의 이동

import sys
from collections import deque

input = sys.stdin.readline

dy = (-2, -1, 1, 2, 2, 1, -1, -2)
dx = (-1, -2, -2, -1, 1, 2, 2, 1)


def BFS(N, start_y, start_x, end_y, end_x):
    global status

    q = deque()
    q.append((start_y, start_x))
    q.append(-1)
    status[start_y][start_x] = True
    cnt = 0
    flag = False

    while q:
        if flag:
            cnt += 1
            break
        else:
            temp = q.popleft()
            if temp == -1:
                cnt += 1
                if len(q) > 0:
                    q.append(-1)
            else:
                y, x = temp[0], temp[1]
                for i in range(8):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and not status[ny][nx]:
                        status[ny][nx] = True
                        q.append((ny, nx))
                        if ny == end_y and nx == end_x:
                            flag = True
    return cnt


T = int(input().strip())
result = []
for _ in range(T):
    N = int(input().strip())
    start_y, start_x = map(int, input().split())
    end_y, end_x = map(int, input().split())

    if start_y == end_y and start_x == end_x:
        result.append(0)
    else:
        status = [[False for _ in range(N)] for _ in range(N)]
        result.append(BFS(N, start_y, start_x, end_y, end_x))

for r in result:
    print(r)
