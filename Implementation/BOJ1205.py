# 등수 구하기

import sys

input = sys.stdin.readline
N, NEW, P = map(int, input().split())

result = 1
if N != 0:
    score = list(map(int, input().split()))
    if N == P and score[-1] >= NEW:
        result = -1
    else:
        result = N + 1
        for i in range(N):
            if score[i] <= NEW:
                result = i + 1
                break
print(result)
