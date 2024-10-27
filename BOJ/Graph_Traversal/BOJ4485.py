# 녹색 옷 입은 애가 젤다지?

import sys
import heapq

input = sys.stdin.readline

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)


def BFS(N):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True
    h = []
    heapq.heappush(h, (cave[0][0], 0, 0))  # 루피, y, x

    while h:
        lupy, y, x = heapq.heappop(h)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = True
                heapq.heappush(h, (lupy + cave[ny][nx], ny, nx))
                if ny == N - 1 and nx == N - 1:
                    return lupy + cave[ny][nx]


result = []
while True:
    N = int(input().strip())
    if N == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    result.append(BFS(N))

for i, r in enumerate(result):
    print("Problem " + str(i + 1) + ": " + str(r))
