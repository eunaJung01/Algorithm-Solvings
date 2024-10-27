# 다리 만들기

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
island = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def define_island(start_y, start_x, island_num):
    global island, visited
    island[start_y][start_x] = island_num
    visited[start_y][start_x] = True

    q = deque()
    q.append((start_y, start_x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and island[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                island[ny][nx] = island_num
                q.append((ny, nx))


def set_bridge(island_num):
    global ans
    bridgeLen = [[-1 for _ in range(N)] for _ in range(N)]

    q = deque()
    for y in range(N):
        for x in range(N):
            if island[y][x] == island_num:
                q.append((y, x))
                bridgeLen[y][x] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if island[ny][nx] > 0 and island[ny][nx] != island_num:
                    ans = min(ans, bridgeLen[y][x])
                    return
                if island[ny][nx] == 0 and bridgeLen[ny][nx] == -1:
                    bridgeLen[ny][nx] = bridgeLen[y][x] + 1
                    q.append((ny, nx))


# 섬 구분
visited = [[False for _ in range(N)] for _ in range(N)]
island_num = 1
for y in range(N):
    for x in range(N):
        if island[y][x] == 1 and not visited[y][x]:
            define_island(y, x, island_num)
            island_num += 1

# 다리 놓기
ans = sys.maxsize
for i in range(1, island_num):
    set_bridge(i)
print(ans)
