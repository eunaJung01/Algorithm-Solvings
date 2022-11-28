# 근손실

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
visited = [False for _ in range(N)]
arr = []
result = 0


def func(cnt):
    global result

    if cnt == N:
        cur = 500
        for i in range(N):
            cur += A[arr[i]] - K
            if cur < 500:
                return
        result += 1
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            func(cnt + 1)
            arr.pop()
            visited[i] = False


func(0)
print(result)
