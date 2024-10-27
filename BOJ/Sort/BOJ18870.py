# 좌표 압축

import sys

N = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().split()))
num = []
for i, n in enumerate(line):
    num.append((n, i))

num.sort()

rate = 0
pre = num[0][0]
for j in range(N):
    n, i = num[j][0], num[j][1]
    if n != pre:
        rate += 1
    num[j] = (i, n, rate)
    pre = n

num.sort()

result = []
for i, n, rate in num:
    result.append(rate)

for r in result:
    print(r, end=' ')
