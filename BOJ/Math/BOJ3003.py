# 킹, 퀸, 룩, 비숍, 나이트, 폰

import sys

chess = [1, 1, 2, 2, 2, 8]
line = list(map(int, sys.stdin.readline().split()))
for i in range(6):
    print(chess[i] - line[i], end=' ')
