# 경로 찾기

import sys

N = int(sys.stdin.readline().strip())

INF = int(1e9)
d = [[INF for _ in range(N)] for _ in range(N)]

for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if line[j] == 1:
            d[i][j] = 1

# 플로이드 워셜 알고리즘
for k in range(N):  # k : 거쳐가는 노드
    for i in range(N):  # i : 출발 노드
        for j in range(N):  # j : 도착 노드
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = 1

for row in d:
    for r in row:
        if r == INF:
            print(0, end=' ')
        else:
            print(r, end=' ')
    print()
