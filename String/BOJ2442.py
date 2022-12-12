# 별 찍기 - 5

import sys

N = int(sys.stdin.readline().strip())
max_star = 2 * N - 1

for i in range(N):
    star = 2 * i + 1
    print((' ' * int((max_star - star) / 2) + '*' * star))
