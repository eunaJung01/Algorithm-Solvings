# 나만 안되는 연애

import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # 학교의 수, 도로의 개수
parent = [i for i in range(N + 1)]

gender, men = list(map(str, input().split())), []
for i, g in enumerate(gender):
    if g == "M":
        men.append(i + 1)

colleges = []
for _ in range(M):
    u, v, d = map(int, input().split())
    if (u in men and v not in men) or (u not in men and v in men):
        colleges.append((u, v, d))
colleges.sort(key=lambda x: x[2])


def union(u, v):
    root_u, root_v = parent[u], parent[v],
    parent[max(root_u, root_v)] = min(root_u, root_v)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


result, edge = 0, 0
for u, v, d in colleges:
    if find(u) != find(v):
        result += d
        union(u, v)
        edge += 1

if edge == N - 1:
    print(result)
else:
    print(-1)
