# 소-난다!

import sys
from math import sqrt

input = sys.stdin.readline

N, M = map(int, input().split())
cow = list(map(int, input().split()))

status = [False for _ in range(N)]
result = []


def check_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(sqrt(x) + 1)):
            if x % i == 0:
                return False
        return True


def func(idx, num):
    global status

    if num == M:
        x = 0
        for i in range(N):
            if status[i]:
                x += cow[i]
        if check_prime(x):
            result.append(x)
        return

    for i in range(idx, N):
        if not status[i]:
            status[i] = True
            func(i + 1, num + 1)
            status[i] = False


func(0, 0)

if len(result) == 0:
    print(-1)
else:
    result = list(set(result))
    result.sort()
    for r in result:
        print(r, end=' ')
