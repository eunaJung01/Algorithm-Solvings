# 부분합

import sys

input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

first, second = 0, 0
s, cnt = 0, 0
result = 100001

while True:
    if s >= S:
        result = min(result, cnt)
        s -= numbers[first]
        cnt -= 1

        first += 1
        if first == N:
            break

    else:
        if second == N:
            break

        s += numbers[second]
        cnt += 1
        second += 1

if result == 100001:
    print(0)
else:
    print(result)
