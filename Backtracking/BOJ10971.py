# 외판원 순회 2

import sys

input = sys.stdin.readline

N = int(input().strip())
travel = [list(map(int, input().split())) for _ in range(N)]
result = 1e10


def func(start, j, cnt, total):
    global result, visited

    if total >= result:
        return

    if cnt == N:
        if travel[j][start] != 0:
            result = min(result, total + travel[j][start])
        return

    for k in range(N):
        if not visited[k] and travel[j][k] != 0:
            visited[k] = True
            func(start, k, cnt + 1, total + travel[j][k])
            visited[k] = False


for i in range(N):
    visited = [False for _ in range(N)]
    visited[i] = True
    func(i, i, 1, 0)

print(result)
