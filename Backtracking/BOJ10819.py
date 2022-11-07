# 차이를 최대로

import sys

input = sys.stdin.readline

N = int(input().strip())
num = list(map(int, input().split()))

result = -1000
arr = []
visited = [False for _ in range(N)]


def func(cnt):
    global result

    if cnt == N:
        temp = 0
        for i in range(N - 1):
            temp += abs(num[arr[i]] - num[arr[i + 1]])
        result = max(result, temp)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            func(cnt + 1)
            arr.pop()
            visited[i] = False


func(0)
print(result)
