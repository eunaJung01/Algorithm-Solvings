# 집합의 표현

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def union(a, b):
    root_a, root_b = find(a), find(b)
    parent[max(root_a, root_b)] = min(root_a, root_b)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


for _ in range(m):
    flag, a, b = map(int, input().split())
    if flag == 0:
        if a == b:
            continue
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
