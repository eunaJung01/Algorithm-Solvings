# 카잉 달력

# 시간 초과
# import sys
#
# input = sys.stdin.readline
#
# T = int(input().strip())
#
# result = []
# for _ in range(T):
#     M, N, x, y = map(int, input().split())
#     year, dx, dy = 1, 1, 1
#
#     while True:
#         if dx == x and dy == y:
#             result.append(year)
#             break
#         if dx == M and dy == N:
#             result.append(-1)
#             break
#
#         dx += 1
#         dy += 1
#
#         if dx > M:
#             dx -= M
#         if dy > N:
#             dy -= N
#
#         year += 1
#
# for r in result:
#     print(r)

# ---

import sys
from math import lcm

input = sys.stdin.readline

T = int(input().strip())

result = []
for _ in range(T):
    M, N, x, y = map(int, input().split())
    max_year = lcm(M, N)

    while True:
        if x > max_year:
            result.append(-1)
            break

        if (x - 1) % N + 1 == y:
            result.append(x)
            break

        x += M

for r in result:
    print(r)
