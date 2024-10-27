# 막대기

import sys

input = sys.stdin.readline

X = int(input().strip())
stick = [64]

while sum(stick) != X:
    stick.sort(reverse=True)
    m = stick.pop()

    if sum(stick) + m / 2 < X:
        stick.append(m / 2)
    stick.append(m / 2)

print(len(stick))
