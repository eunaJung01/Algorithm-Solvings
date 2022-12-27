# 행성 연결

import sys

input = sys.stdin.readline

N = int(input().strip())
root = [i for i in range(N)]

planet = []
for i in range(N):
    row = list(map(int, input().split()))
    for j, w in enumerate(row):
        if i != j:
            planet.append((i, j, w))
planet.sort(key=lambda x: x[2])  # 가중치 기준 오름차순 정렬


def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]


result = 0
for i, j, w in planet:
    root_i, root_j = find(i), find(j)
    if root_i != root_j:
        if root_i > root_j:
            root[root_i] = root_j
        else:
            root[root_j] = root_i
        result += w
print(result)
