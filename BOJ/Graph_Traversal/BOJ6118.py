# 숨바꼭질

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

status = [False for _ in range(N + 1)]
status[1] = True


def BFS(x):
    q = deque()
    q.append(x)
    q.append(-1)

    d = 0
    arr1 = []
    arr2 = []

    while q:
        x = q.popleft()
        if x == -1:
            if len(q) == 0:
                break
            else:
                d += 1
                arr1 = arr2.copy()
                arr2 = []
                q.append(-1)
        else:
            for i in graph[x]:
                if not status[i]:
                    status[i] = True
                    arr2.append(i)
                    q.append(i)

    return [min(arr1), d, len(arr1)]


result = BFS(1)  # 가장 거리가 먼 헛간의 번호 / 거리 / 개수

for r in result:
    print(r, end=' ')
