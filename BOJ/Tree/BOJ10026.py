# 적록색약

import sys
from collections import deque

N = int(sys.stdin.readline().strip())

pic = []
for _ in range(N):
    pic.append(list(sys.stdin.readline().strip()))

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)

visited = [[False for _ in range(N)] for _ in range(N)]

def BFS(i, j, color):
    global pic
    visited[i][j] = True

    q = deque([])
    q.append((i, j))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and pic[ny][nx] == color and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))


c_normal, c_weak = 0, 0  # 정상, 적록색약

# 정상 BFS
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            c_normal += 1
            BFS(i, j, pic[i][j])

# G -> R
for i in range(N):
    for j in range(N):
        pic[i][j] = 'R' if pic[i][j] == 'G' else pic[i][j]

visited = [[False for _ in range(N)] for _ in range(N)]  # 초기화

# 적록색약 BFS
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            c_weak += 1
            BFS(i, j, pic[i][j])

print(c_normal, c_weak)
