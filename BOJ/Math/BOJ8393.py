# 합

import sys

n = int(sys.stdin.readline().strip())
result = 0
for i in range(1, n + 1):
    result += i
print(result)
