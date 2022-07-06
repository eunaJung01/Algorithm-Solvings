# 아기 상어

import sys
import heapq

N = int(sys.stdin.readline().strip())

# 아기 상어 위치
y, x = 0, 0

fish = []
for i in range(N):
    fish.append(list(map(int, sys.stdin.readline().split())))
    if 9 in fish[i]:
        y = i
        x = fish[i].index(9)

fish[y][x] = 0

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def BFS(r, c):
    ans = 0
    size = 2  # 아기 상어의 크기
    eat = 0  # 먹은 횟수

    q = []
    heapq.heappush(q, (0, r, c))  # 거리, y좌표, x좌표
    visited = [[False for _ in range(N)] for _ in range(N)]

    while q:
        d, y, x = heapq.heappop(q)

        if 0 < fish[y][x] < size:  # 먹을 수 있는 물고기인 경우
            eat += 1
            fish[y][x] = 0
            if size == eat:  # 자신의 크기와 같은 수의 물고기를 먹었을 경우
                size += 1
                eat = 0
            ans += d

            # 초기화
            d = 0
            while q:
                heapq.heappop(q)
            visited = [[False for _ in range(N)] for _ in range(N)]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and fish[ny][nx] <= size:
                visited[ny][nx] = True
                heapq.heappush(q, (d + 1, ny, nx))
    return ans


print(BFS(y, x))
