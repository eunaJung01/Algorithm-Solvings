# 블로그2

import sys

N = int(sys.stdin.readline().strip())
color = list(sys.stdin.readline().strip())

result = 0

# 1. 파란색 -> 빨간색
count = 1
pre = 0
for i in range(N):
    c = color[i]
    if i == 0 and c == 'R':
        count += 1
    elif c == 'R' and pre == 'B':
        count += 1
    pre = c
result = count

# 2. 빨간색 -> 파란색
count = 1
pre = 0
for i in range(N):
    c = color[i]
    if i == 0 and c == 'B':
        count += 1
    elif c == 'B' and pre == 'R':
        count += 1
    pre = c
result = min(result, count)

print(result)
