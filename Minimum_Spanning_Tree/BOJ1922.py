# 네트워크 연결

import sys

input = sys.stdin.readline

N = int(input().strip())  # 컴퓨터의 수
M = int(input().strip())  # 연결할 수 있는 선의 수

parent = [i for i in range(N + 1)]

kruskal = []
for i in range(M):
    a, b, c = map(int, input().split())  # a 컴퓨터, b 컴퓨터, 비용 c
    kruskal.append((a, b, c))
kruskal.sort(key=lambda x: x[2])  # 가중치 기준 오름차순 정렬


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


weight_sum = 0
for a, b, w, in kruskal:
    if find(a) != find(b):
        a, b = find(a), find(b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
        weight_sum += w

print(weight_sum)
