# 중복 빼고 정렬하기

import sys

input = sys.stdin.readline

N = int(input().strip())
line = list(map(int, input().split()))

line = set(line)
line = list(line)
line.sort()

for l in line:
    print(l, end=' ')
