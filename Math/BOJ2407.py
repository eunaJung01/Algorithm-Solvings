# 조합

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
result = 1

if n != m:
    if m > n - m:
        m = n - m

    for i in range(m):
        result *= (n - i)
    for i in range(m):
        result //= (m - i)

print(result)
