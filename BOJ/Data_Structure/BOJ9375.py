# 패션왕 신해빈

import sys

input = sys.stdin.readline

T = int(input().strip())
result = []

for _ in range(T):
    n = int(input().strip())

    wears = {}
    for _ in range(n):
        name, type = input().split()
        if type in wears:
            wears[type] += 1
        else:
            wears[type] = 1

    ans = 1
    for k in wears:
        ans *= wears[k] + 1
    result.append(ans - 1)

for r in result:
    print(r)
