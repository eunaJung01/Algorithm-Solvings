# 선 긋기

import sys

input = sys.stdin.readline

N = int(input().strip())
lines = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    lines[i].sort()
lines.sort(key=lambda x: (x[0], x[1]))

result = abs(lines[0][0] - lines[0][1])
pre_y = lines[0][1]
for i in range(1, N):
    x, y = lines[i][0], lines[i][1],
    if x < pre_y:
        if y <= pre_y:
            continue
        result += abs(y - pre_y)
    else:
        result += abs(y - x)
    pre_y = y
print(result)
