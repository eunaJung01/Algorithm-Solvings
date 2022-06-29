# 마법사 상어와 비바라기

import sys

N, M = map(int, sys.stdin.readline().split())  # NxN 격자 / M번의 이동

grid = []  # 격자
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

direction = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
diagonal = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

move = []  # [이동 방향, 이동 칸 수]
for _ in range(M):
    move.append(list(map(int, sys.stdin.readline().split())))

cloud = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]  # 구름 위치

for d, num in move:
    visited = []  # 구름 위치 기록
    for _ in range(N):
        visited.append(list([False for _ in range(N)]))

    for i, c in enumerate(cloud):
        # 구름 이동
        c_y = (c[0] + num * direction[d - 1][0]) % N
        c_x = (c[1] + num * direction[d - 1][1]) % N
        cloud[i] = [c_y, c_x]

        # 비 -> 구름이 있는 칸의 물 + 1
        grid[c_y][c_x] += 1
        visited[c_y][c_x] = True

    # 물복사 버그 마법 시전
    for c_y, c_x in cloud:
        for d_y, d_x in diagonal:
            y = c_y + d_y
            x = c_x + d_x

            if 0 <= x < N and 0 <= y < N:
                if grid[y][x] > 0:
                    grid[c_y][c_x] += 1

    # 구름 생성
    cloud = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] >= 2 and not visited[i][j]:
                cloud.append([i, j])
                grid[i][j] -= 2


# 물의 양 합 계산
water = 0
for row in grid:
    for r in row:
        water += r
print(water)
