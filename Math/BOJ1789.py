# 수들의 합

import sys

N = int(sys.stdin.readline().strip())

result = 0
for i in range(1, N + 1):
    if N - i < 0:
        break
    N -= i
    result = i
print(result)
