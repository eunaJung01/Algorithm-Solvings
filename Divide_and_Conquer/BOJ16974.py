# 레벨 햄버거

import sys

input = sys.stdin.readline

N, X = map(int, input().split())

burger = [0] * (N + 1)  # 버거 층의 개수
patty = [0] * (N + 1)  # 패티의 개수
burger[0], patty[0] = 1, 1

for i in range(1, N + 1):
    burger[i] = burger[i - 1] * 2 + 3
    patty[i] = patty[i - 1] * 2 + 1


def cntPatty(level, h):
    if level == 0:
        if h == 0:
            return 0
        elif h == 1:
            return 1
    if h == 0:
        return 0

    # 중간 패티 위치보다 작은 경우
    if h <= burger[level - 1] + 1:
        return cntPatty(level - 1, h - 1)

    # 중간 패티 위치
    elif h == burger[level - 1] + 2:
        return patty[level - 1] + 1

    # 중간 패티 위치보다 큰 경우
    elif h <= burger[level - 1] * 2 + 2:
        return patty[level - 1] + 1 + cntPatty(level - 1, h - (burger[level - 1] + 2))

    # 현재 레벨의 층 수와 같은 경우
    else:
        return patty[level - 1] * 2 + 1


print(cntPatty(N, X))
