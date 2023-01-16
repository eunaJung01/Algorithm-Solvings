# 트리의 지름

# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input().strip())
# nodes = [[0, []] for _ in range(n + 1)]  # 부모, 자식들
#
# for _ in range(n - 1):
#     parent, child, w = map(int, input().split())
#     nodes[parent][1].append([child, w])
#     nodes[child][0] = [parent, w]
#
#
# def find_diameter(start, end):
#     visited = [False for _ in range(n + 1)]
#     visited[start] = True
#
#     q = deque()
#     q.append((start, 0))  # node, w
#     while q:
#         node, w = q.popleft()
#
#         parent_info, childs = nodes[node]
#         if parent_info != 0:
#             parent, parent_w = map(int, parent_info)
#             if not visited[parent]:
#                 if parent != end:
#                     q.append((parent, w + parent_w))
#                     visited[parent] = True
#                 else:
#                     return w + parent_w
#
#         for child, child_w in childs:
#             if not visited[child]:
#                 if child != end:
#                     q.append((child, w + child_w))
#                     visited[child] = True
#                 else:
#                     return w + child_w
#     return 0
#
#
# result = 0
# for i in range(1, n):
#     for j in range(2, n + 1):
#         result = max(result, find_diameter(i, j))
# print(result)

# ---

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def DFS(node, weight):
    for n, w, in tree[node]:
        if dist[n] == -1:
            dist[n] = weight + w
            DFS(n, weight + w)


n = int(input().strip())
tree = [[] for _ in range(n + 1)]  # 양방향 그래프로 구성
for _ in range(n - 1):
    parent, child, w = map(int, input().split())
    tree[parent].append([child, w])
    tree[child].append([parent, w])

dist = [-1 for _ in range(n + 1)]  # root 노드부터 각 노드까지의 가중치 합을 저장
dist[1] = 0
DFS(1, 0)

start = dist.index(max(dist))  # 가중치 합이 최대가 되는 노드 (leaf)
dist = [-1 for _ in range(n + 1)]
dist[start] = 0
DFS(start, 0)  # start를 기준으로 DFS를 한번 더 수행

print(max(dist))
