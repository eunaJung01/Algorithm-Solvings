# 수들의 합 2

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)

result = 0
start, end = 0, 0
s = 0  # 부분합

while end <= N:
    if s >= M:
        s -= arr[start]
        start += 1
    else:
        s += arr[end]
        end += 1

    if s == M:
        result += 1

print(result)
