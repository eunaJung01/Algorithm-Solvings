# 로프

import sys

N = int(sys.stdin.readline().strip())

rope = []
for _ in range(N):
    rope.append(int(sys.stdin.readline().strip()))
rope.sort(reverse=True)

result = -999999
while rope:
    result = max(result, rope[-1] * len(rope))
    rope.pop()

print(result)
