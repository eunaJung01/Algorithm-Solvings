# 경사로

import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]


def runway_is_able(lst):
    i = 1
    has_runway = [False for _ in range(len(lst))]

    while True:
        if i >= len(lst):
            return True
        if abs(lst[i - 1] - lst[i]) > 1:
            return False

        # 평지
        if lst[i - 1] == lst[i]:
            i += 1
            continue

        # 내리막길
        if lst[i - 1] > lst[i]:
            if i + L - 1 > len(lst) - 1:
                return False
            for j in range(L):
                if lst[i] != lst[i + j]:
                    return False
                has_runway[i + j] = True
            i += L
            continue

        # 오르막길
        if lst[i - 1] < lst[i]:
            if i - L < 0:
                return False
            for j in range(L):
                if has_runway[i - 1 - j]:
                    return False
                if lst[i - 1] != lst[i - 1 - j]:
                    return False
            i += 1


ans = 0
for y in range(N):  # 가로
    if runway_is_able(deque(ground[y])):
        ans += 1
for x in range(N):  # 세로
    target = []
    for i in range(N):
        target.append(ground[i][x])
    if runway_is_able(deque(target)):
        ans += 1
print(ans)
