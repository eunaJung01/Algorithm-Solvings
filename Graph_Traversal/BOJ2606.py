# 바이러스

import sys
from collections import deque

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

network = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    c1, c2 = map(int, sys.stdin.readline().split())
    c1 -= 1
    c2 -= 1
    network[c1][c2] = 1
    network[c2][c1] = 1

result = 0
visited = [False for _ in range(N)]
visited[0] = True

q = deque()
q.append(0)
while q:
    node = q.popleft()
    for i in range(N):
        if network[node][i] == 1 and not visited[i]:
            result += 1
            q.append(i)
            visited[i] = True

print(result)
