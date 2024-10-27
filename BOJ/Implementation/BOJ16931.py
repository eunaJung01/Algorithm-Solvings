# 겉넓이 구하기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
square = [list(map(int, input().split())) for _ in range(N)]
result = 0

# 위 & 아래
result += N * M * 2

# 옆
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

for y in range(N):
    for x in range(M):
        cnt = square[y][x] * 4

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if square[ny][nx] > square[y][x]:
                    cnt -= square[y][x]
                else:
                    cnt -= square[ny][nx]

        result += cnt

print(result)
