# 텀 프로젝트

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def DFS(s):
    global visited, hasTeam, cycle

    visited[s] = True
    cycle.append(s)
    s_partner = partners[s]

    if visited[s_partner]:
        if s_partner in cycle:
            hasTeam += cycle[cycle.index(s_partner):]
        return
    DFS(s_partner)


T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    partners = [0] + list(map(int, input().split()))

    visited = [False for _ in range(n + 1)]
    hasTeam = []

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            DFS(i)

    print(n - len(hasTeam))
