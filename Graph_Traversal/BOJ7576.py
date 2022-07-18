# 토마토

import sys
from collections import deque

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def BFS():
    global q
    ans = 0

    q.append(-1)
    while q:
        temp = q.popleft()
        if temp == -1:
            if len(q) != 0:
                q.append(-1)
                ans += 1
            else:
                break
        else:
            y, x = temp[0], temp[1]
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and tomato[ny][nx] == 0:
                    tomato[ny][nx] = 1
                    q.append((ny, nx))

    return ans


M, N = map(int, sys.stdin.readline().split())  # M : 가로 / N : 세로

result = 0
status = False

tomato = []
q = deque()
for n in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for m in range(M):
        if line[m] == 0:
            status = True
        if line[m] == 1:
            q.append((n, m))
    tomato.append(line)

if status:
    result = BFS()

    for n in range(N):
        for m in range(M):
            if tomato[n][m] == 0:
                result = -1

print(result)
