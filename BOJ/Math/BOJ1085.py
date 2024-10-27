# 직사각형에서 탈출

import sys

input = sys.stdin.readline

a, b, c, d = list(map(int, input().split()))
print(min(a, b, c - a, d - b))
