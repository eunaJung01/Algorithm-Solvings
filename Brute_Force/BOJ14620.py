# 꽃길

import sys
from itertools import permutations

N = int(sys.stdin.readline())

garden = []
for _ in range(N):
    garden.append(list(map(int, sys.stdin.readline().split())))

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

price_lst = []  # [y, x, price]
for y in range(1, N - 1):
    for x in range(1, N - 1):
        price = garden[y][x]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                price += garden[ny][nx]
        price_lst.append([y, x, price])

lst = list(permutations(price_lst, 3))

result = 9999999  # 가격 범위 조심!!
for first, second, third in lst:
    if ((first[0] - second[0]) ** 2 + (first[1] - second[1]) ** 2) >= 5 and (
            (second[0] - third[0]) ** 2 + (second[1] - third[1]) ** 2) >= 5 and (
            (third[0] - first[0]) ** 2 + (third[1] - first[1]) ** 2) >= 5:
        result = min(result, first[2] + second[2] + third[2])
print(result)
