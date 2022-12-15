# 검증수

import sys

line = list(map(int, sys.stdin.readline().split()))
s = 0
for num in line:
    s += num ** 2
print(s % 10)
