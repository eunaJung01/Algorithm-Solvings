# N-Queen

import sys

input = sys.stdin.readline
N = int(input().strip())
result = 0

col = [False for _ in range(40)]  # y
diag1 = [False for _ in range(40)]  # x+y
diag2 = [False for _ in range(40)]  # x-y+n-1


def func(cnt):
    global result

    if cnt == N:
        result += 1
        return

    for i in range(N):
        if col[i] or diag1[cnt + i] or diag2[cnt - i + N - 1]:
            continue

        col[i] = True
        diag1[cnt + i] = True
        diag2[cnt - i + N - 1] = True
        func(cnt + 1)
        col[i] = False
        diag1[cnt + i] = False
        diag2[cnt - i + N - 1] = False


func(0)
print(result)
