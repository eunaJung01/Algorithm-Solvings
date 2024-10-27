# 인공지능 시계

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
d = int(input())

a = ((((c + d) // 60 + b) // 60) + a) % 24
print(a, ((c + d) // 60 + b) % 60, (c + d) % 60)
