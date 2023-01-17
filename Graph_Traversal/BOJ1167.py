# 트리의 지름

# 524 ms, 67672 KB

import sys

input = sys.stdin.readline

V = int(input().strip())
tree = [[] for _ in range(V + 1)]

for _ in range(1, V + 1):
    line = list(map(int, input().split()))
    key = line[0]
    for j in range(1, len(line) - 2, 2):
        tree[key].append((line[j], line[j + 1]))  # 간선, 거리


def DFS(node, weight):
    global result, max_dist
    if result < weight:
        result = weight
        max_dist = node

    visited[node] = True
    for n, w in tree[node]:
        if not visited[n]:
            DFS(n, weight + w)


max_dist, result = 0, 0
visited = [False for _ in range(V + 1)]
DFS(1, 0)

visited = [False for _ in range(V + 1)]
DFS(max_dist, 0)
print(result)

# ---

# 기존 풀이
# 612 ms, 70744 KB

# import sys
#
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)
#
# V = int(input().strip())
# tree = [[] for _ in range(V + 1)]
#
# for i in range(1, V + 1):
#     line = list(map(int, input().split()))
#     key = line[0]
#     for j in range(1, len(line) - 2, 2):
#         tree[key].append((line[j], line[j + 1]))  # 간선, 거리
#
#
# def DFS(node, weight):
#     for n, w in tree[node]:
#         if dist[n] == -1:
#             dist[n] = weight + w
#             DFS(n, weight + w)
#
#
# dist = [-1 for _ in range(V + 1)]
# DFS(1, 0)
# max_dist = dist.index(max(dist))
#
# dist = [-1 for _ in range(V + 1)]
# dist[max_dist] = 0
# DFS(max_dist, 0)
# print(max(dist))
