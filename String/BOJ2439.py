# 별 찍기 - 2

import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N + 1):
    print(" " * (N - i) + "*" * i)
