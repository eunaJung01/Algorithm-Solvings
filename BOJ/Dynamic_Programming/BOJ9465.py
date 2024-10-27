# 스티커

import sys

T = int(sys.stdin.readline().strip())

result = []
for _ in range(T):
    n = int(sys.stdin.readline().strip())

    sticker = []
    for i in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    if n > 1:
        sticker[1][1] += sticker[0][0]
        sticker[0][1] += sticker[1][0]

    if n > 2:
        for i in range(2, n):
            sticker[0][i] += max(sticker[1][i - 2], sticker[1][i - 1])
            sticker[1][i] += max(sticker[0][i - 2], sticker[0][i - 1])

    result.append(max(sticker[0][n - 1], sticker[1][n - 1]))

for r in result:
    print(r)
