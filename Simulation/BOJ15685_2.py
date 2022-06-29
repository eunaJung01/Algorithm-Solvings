# 드래곤 커브 (solution 2)

import sys

N = int(sys.stdin.readline().strip())

dragon_input = []  # 시작점 x, 시작점 y, 시작 방향, 세대
for _ in range(N):
    dragon_input.append(list(map(int, sys.stdin.readline().split())))

grid = []  # 100 x 100
for _ in range(101):
    grid.append(list([False for _ in range(101)]))

# 방향
d_y = [0, -1, 0, 1]
d_x = [1, 0, -1, 0]

for start_x, start_y, d, g in dragon_input:
    direction = [d]

    for _ in range(g):
        for i in range(len(direction) - 1, -1, -1):  # range(start, stop, step)
            direction.append((direction[i] + 1) % 4)

    # 위치 표시
    grid[start_y][start_x] = True
    for i in direction:
        start_y += d_y[i]
        start_x += d_x[i]
        grid[start_y][start_x] = True

# 정사각형 개수 구하기
result = 0
for y in range(100):
    for x in range(100):
        if grid[y][x] and grid[y + 1][x] and grid[y][x + 1] and grid[y + 1][x + 1]:
            result += 1
print(result)
