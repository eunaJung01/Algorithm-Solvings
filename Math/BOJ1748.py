# 수 이어 쓰기 1

import sys

N = int(sys.stdin.readline().strip())
result, i = 0, 1

while True:
    result += (N - i + 1)
    i *= 10

    if i > N:
        break

print(result)
