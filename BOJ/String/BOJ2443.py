# 별 찍기 - 6

import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N + 1):
    print((' ' * (i - 1) + '*' * (2 * (N - i) + 1)))
