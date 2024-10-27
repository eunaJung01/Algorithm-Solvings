# 단어 뒤집기

import sys

input = sys.stdin.readline
T = int(input().strip())

line = [input().split() for _ in range(T)]

for l in line:
    for word in l:
        print(word[::-1], end=" ")
    print()
