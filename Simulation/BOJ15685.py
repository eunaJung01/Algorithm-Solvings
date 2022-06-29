# 드래곤 커브 (solution 1)

import sys

N = int(sys.stdin.readline().strip())

dragon_input = []  # 시작점 x, 시작점 y, 시작 방향, 세대
for _ in range(N):
    dragon_input.append(list(map(int, sys.stdin.readline().split())))

grid = []  # 100 x 100
for _ in range(101):
    grid.append(list([False for _ in range(101)]))

direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 시작 방향
rotate_90 = {(-1, 0): (0, 1), (1, 0): (0, -1), (0, 1): (1, 0), (0, -1): (-1, 0)}  # 시계 방향 90도 회전 시 벡터

for start_x, start_y, d, g in dragon_input:
    dragon = [[start_y, start_x], [start_y + direction[d][0], start_x + direction[d][1]]]  # 드래곤 커브 좌표 (0세대)

    for _ in range(g):
        i = len(dragon) - 1

        # 드래곤 커브 좌표 구하기
        while i >= 1:
            y = dragon[i][0] - dragon[i - 1][0]
            x = dragon[i][1] - dragon[i - 1][1]

            vector = rotate_90.get((y, x))
            new_point = [dragon[-1][0] - vector[0], dragon[-1][1] - vector[1]]
            dragon.append(new_point)

            i -= 1

    # 위치 표시
    for d_y, d_x in dragon:
        grid[d_y][d_x] = True

# 정사각형 개수 구하기
result = 0
for y in range(100):
    for x in range(100):
        if grid[y][x] and grid[y + 1][x] and grid[y][x + 1] and grid[y + 1][x + 1]:
            result += 1
print(result)
