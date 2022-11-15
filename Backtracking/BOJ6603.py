# 로또

import sys

input = sys.stdin.readline
arr = []


def func(idx, N):
    global n, numbers, status

    if N == 6:
        for a in arr:
            print(a, end=' ')
        print()
        return

    for i in range(n):
        if not status[i] and idx <= i:
            status[i] = True
            arr.append(numbers[i])
            func(i, N + 1)
            arr.pop()
            status[i] = False


while True:
    line = list(map(int, input().split()))
    if line[0] == 0:
        break

    n = line[0]
    numbers = line[1:]
    status = [False] * n
    func(0, 0)
    print()
