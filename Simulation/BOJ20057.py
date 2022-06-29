# 마법사 상어와 토네이도

import copy
import sys

N = int(sys.stdin.readline().strip())

grid = []  # N x N 격자
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

# 0 : ← / 1 : ↓ / 2 : → / 3 : ↑
d_y = [0, 1, 0, -1]
d_x = [-1, 0, 1, 0]

# 모래 흩날리는 비율 (a 위치 : -1)
ratio = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, -1, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0],
         [0, 0, 0.02, 0, 0]]


# ratio 반 시계 방향 90도 회전
def rotate_ratio():
    old = copy.deepcopy(ratio)
    for i in range(1, 4):  # 대각선
        ratio[i][i] = old[i][-i - 1]
        ratio[i][-i - 1] = old[-i - 1][-i - 1]
    for i in range(5):  # 십자
        ratio[i][2] = old[2][-i - 1]
        ratio[2][i] = old[i][2]


d = []  # 토네이도 이동 방향
i = 1
d_idx = 0
for _ in range(N - 1):
    for _ in range(2):
        for _ in range(i):
            d.append(d_idx)
        d_idx = (d_idx + 1) % 4
    i += 1
for _ in range(i):
    d.append(d_idx)

y, x = N // 2, N // 2  # 시작점 (y, x)
a_y, a_x = 0, 0  # a 위치 (a_y, a_x)
d_idx = d[0]  # 방향
result = 0  # 격자 밖으로 나간 모래의 양

for a in range(len(d)):
    # 방향 전환 시 비율 회전
    if d_idx != d[a]:
        rotate_ratio()

    d_idx = d[a]
    y += d_y[d_idx]
    x += d_x[d_idx]

    # 모래양 계산
    sand = grid[y][x]
    left = sand  # a로 이동할 모래의 양

    for j in range(5):
        for i in range(5):
            cur_y = y + j - 2
            cur_x = x + i - 2
            if ratio[j][i] == -1:  # a 위치일 경우
                a_y = cur_y
                a_x = cur_x
                continue

            add = int(sand * ratio[j][i])  # 소수점 아래 버림
            if 0 <= cur_y < N and 0 <= cur_x < N:
                grid[cur_y][cur_x] += add
            else:
                result += add
            left -= add

    grid[y][x] = 0

    # a 위치
    if 0 <= a_y < N and 0 <= a_x < N:
        grid[a_y][a_x] += left
    else:
        result += left

print(result)
