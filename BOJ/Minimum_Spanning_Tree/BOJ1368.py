# 물대기

import sys

input = sys.stdin.readline

N = int(input().strip())
well = [int(input().strip()) for _ in range(N)]  # 우물을 팔 때 드는 비용
parent = [i for i in range(N + 1)]
paddy = []

# 연결 비용
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(i + 1, N):
        paddy.append((i, j, row[j]))  # i번째 논, j번째 논, 비용

# 가상의 N번째 노드를 추가하여 우물 파는 비용을 그래프에 함께 표현
for i, w in enumerate(well):
    paddy.append((i, N, w))

# 정렬
paddy.sort(key=lambda x: x[2])


def union(a, b):
    root_a, root_b = find(a), find(b)
    parent[max(root_a, root_b)] = min(root_a, root_b)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


result = 0
for i, j, w in paddy:
    if find(i) != find(j):
        result += w
        union(i, j)
print(result)
