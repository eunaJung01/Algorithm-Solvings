# 사이클 게임

import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 점의 개수, 진행된 차례의 수
trials = [list(map(int, input().split())) for _ in range(m)]


def union(a, b):
    root_a, root_b = find(a), find(b)
    parent[max(root_a, root_b)] = min(root_a, root_b)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def playCycleGame():
    for i in range(m):
        dot1, dot2 = trials[i]
        if find(dot1) == find(dot2):
            return i + 1
        union(dot1, dot2)
    return 0


parent = [i for i in range(n)]
print(playCycleGame())
