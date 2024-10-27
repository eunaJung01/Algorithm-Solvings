# 내려가기

import sys

input = sys.stdin.readline

N = int(input().strip())

dp_max = [[0 for _ in range(3)] for _ in range(N)]
dp_min = [[int(1e6) for _ in range(3)] for _ in range(N)]
dx = (-1, 0, 1)

for y in range(N):
    line = list(map(int, input().split()))

    if y == 0:
        dp_max[y] = line
        dp_min[y] = line
        continue

    ny = y - 1
    for x in range(3):
        for i in range(3):
            nx = x + dx[i]
            if 0 <= nx < 3:
                dp_max[y][x] = max(dp_max[y][x], dp_max[ny][nx] + line[x])
                dp_min[y][x] = min(dp_min[y][x], dp_min[ny][nx] + line[x])

print(max(dp_max[-1]), min(dp_min[-1]))
