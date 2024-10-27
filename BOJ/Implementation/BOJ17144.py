# 미세먼지 안녕!

import copy
import sys
from math import trunc

input = sys.stdin.readline

R, C, T = map(int, input().split())  # 격자판 크기 R X C, T초

dusts, air_cleaner = [], []
for i in range(R):
    line = list(map(int, input().split()))
    for j, l in enumerate(line):
        if l == -1:
            air_cleaner.append((i, j))
    dusts.append(line)

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


# 미세먼지 확산
def move_dust():
    new_dusts = [[0 for _ in range(C)] for _ in range(R)]

    for y in range(R):
        for x in range(C):
            dust = dusts[y][x]
            if dust > 0:
                n = 0  # 확산된 방향의 개수
                new_dust = trunc(dust / 5)  # 소수점 버림
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < R and 0 <= nx < C and dusts[ny][nx] != -1:
                        n += 1
                        new_dusts[ny][nx] += new_dust
                new_dusts[y][x] += dust - new_dust * n  # 확산 후 남은 미세먼지 양

    for y, x in air_cleaner:
        new_dusts[y][x] = -1
    return new_dusts


# 윗쪽 : 반시계방향 순환
def rotate_upper(upper):
    bottom = air_cleaner[0][0]
    new_upper = copy.deepcopy(upper)

    # TODO: 순환
    # 아래 (bottom, 1) ~ (bottom, C-2) 이동
    for x in range(1, C - 1):
        new_upper[bottom][x + 1] = upper[bottom][x]

    # 오른쪽 (bottom, C-1) ~ (1, C-1) 이동
    for y in range(bottom, 0, -1):
        new_upper[y - 1][C - 1] = upper[y][C - 1]

    # 위 (0, C-1) ~ (0, 1) 이동
    for x in range(C - 1, 0, -1):
        new_upper[0][x - 1] = upper[0][x]

    # 왼쪽 (0, 0) ~ (bottom-1, 0) 이동
    for y in range(0, bottom):
        new_upper[y + 1][0] = upper[y][0]

    # TODO: 공기 청정기
    new_upper[bottom][0] = -1
    new_upper[bottom][1] = 0  # 나온 바람

    return new_upper


# 아랫쪽 : 시계방향 순환
def rotate_lower(lower):
    bottom = R - air_cleaner[1][0] - 1
    new_lower = copy.deepcopy(lower)

    # TODO: 순환
    # 위 (0, 1) ~ (0, C-2) 이동
    for x in range(1, C - 1):
        new_lower[0][x + 1] = lower[0][x]

    # 오른쪽 (0, C-1) ~ (bottom-1, C-1) 이동
    for y in range(bottom):
        new_lower[y + 1][C - 1] = lower[y][C - 1]

    # 아래 (bottom, C-1) ~ (bottom, 1) 이동
    for x in range(C - 1, 0, -1):
        new_lower[bottom][x - 1] = lower[bottom][x]

    # 위 (bottom, 0) ~ (1, 0) 이동
    for y in range(bottom, 0, -1):
        new_lower[y - 1][0] = lower[y][0]

    # TODO: 공기 청정기
    new_lower[0][0] = -1
    new_lower[0][1] = 0  # 나온 바람

    return new_lower


# 공기 청정기 작동 (1초 당 한 칸씩 이동)
def activate_dust_cleaner():
    upper = rotate_upper(dusts[:air_cleaner[0][0] + 1])
    lower = rotate_lower(dusts[air_cleaner[1][0]:])
    return upper + lower


for _ in range(T):
    dusts = move_dust()
    dusts = activate_dust_cleaner()

result = 2
for i in range(R):
    result += sum(dusts[i])
print(result)
