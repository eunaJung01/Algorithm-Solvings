# 조각 케이크

import sys

input = sys.stdin.readline

N = int(input().strip())
cake = list(map(int, input().split()))
cake.sort()

status = [False for _ in range(N)]
result = 0


def func(idx, w):
    global result
    if 0.99 <= w <= 1.01:
        result += 1
        return
    elif w > 1.01:
        return

    for i in range(idx, N):
        if not status[i]:
            status[i] = True
            func(i + 1, w + 1 / cake[i])
            status[i] = False


func(0, 0)
print(result)
