# 도시 건설

# 시간 초과
# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# buildings = [list(map(int, input().split())) for _ in range(M)]  # 건물 a번, 건물 b번, 비용 c
# buildings.sort(key=lambda x: x[2])
# parent = [i for i in range(N + 1)]
#
#
# def find(x):
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]
#
#
# min_weight = 0
# for a, b, c in buildings:
#     root_a, root_b = find(a), find(b)
#
#     if root_a != root_b:
#         modified_root = -1
#         if root_a > root_b:
#             parent[root_a] = root_b
#             modified_root = root_a
#         else:
#             parent[root_b] = root_a
#             modified_root = root_b
#
#         for i, p in enumerate(parent):
#             if p == root_a:
#                 if modified_root == root_a:
#                     parent[i] = root_b
#             elif p == root_b:
#                 if modified_root == root_b:
#                     parent[i] = root_a
#         min_weight += c
#
#
# def print_result():
#     if sum(parent) != parent[1] * N:
#         print(-1)
#         return
#
#     total_weight = 0
#     for building in buildings:
#         total_weight += building[2]
#     print(total_weight - min_weight)
#
#
# print_result()

# ---

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

buildings, total_weight = [], 0
for _ in range(M):
    a, b, c = map(int, input().split())  # 건물 a번, 건물 b번, 비용 c
    total_weight += c
    buildings.append((a, b, c))
buildings.sort(key=lambda x: x[2])


def union(a, b):
    parent[max(a, b)] = min(a, b)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


min_weight, edge_cnt = 0, 0
for a, b, c in buildings:
    root_a, root_b = find(a), find(b)
    if root_a != root_b:
        union(root_a, root_b)
        min_weight += c
        edge_cnt += 1

# def isConnected():
#     count = 0
#     for i in range(1, N + 1):
#         if parent[i] == i:
#             count += 1
#             if count >= 2:
#                 return False
#     return True
#
#
# if isConnected():
#     print(total_weight - min_weight)
# else:
#     print(-1)

# isConnected()를 통해 부모 노드들을 하나하나 확인할 필요 없이, 간선의 개수만으로 확인 가능
if edge_cnt == N - 1:
    print(total_weight - min_weight)
else:
    print(-1)
