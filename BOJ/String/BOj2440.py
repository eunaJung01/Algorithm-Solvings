# 별 찍기 - 3

import sys

N = int(sys.stdin.readline().strip())
for i in range(N + 1):
    print('*' * (N - i))
