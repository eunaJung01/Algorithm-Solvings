# DFS와 BFS

# # 왜 틀림?????
# import sys
# from collections import deque
#
# sys.setrecursionlimit(10000)
#
# N, M, V = map(int, sys.stdin.readline().split())
#
# connection = []
# for _ in range(M):
#     connection.append(list(map(int, sys.stdin.readline().split())))
#
# visited = [False for _ in range(N)]
# travel = []
#
#
# def DFS(node):
#     visited[node - 1] = True
#     travel.append(node)
#
#     nextList = []
#     for c in connection:
#         if c[0] == node and not visited[c[1] - 1]:
#             nextList.append(c[1])
#         elif c[1] == node and not visited[c[0] - 1]:
#             nextList.append(c[0])
#     nextList.sort()
#
#     for next in nextList:
#         if not visited[next - 1]:
#             DFS(next)
#
#     return travel
#
#
# def BFS(node):
#     visited = [False for _ in range(N)]
#     visited[node - 1] = True
#
#     q = deque([node])
#     travel = [node]
#
#     while q:
#         n = q.popleft()
#
#         nextList = []
#         for c in connection:
#             if c[0] == n and not visited[c[1] - 1]:
#                 nextList.append(c[1])
#             elif c[1] == n and not visited[c[0] - 1]:
#                 nextList.append(c[0])
#         nextList.sort()
#
#         for next in nextList:
#             visited[next - 1] = True
#             q.append(next)
#             travel.append(next)
#
#     return travel
#
#
# travel_DFS = DFS(V)
# travel_BFS = BFS(V)
#
# for t in travel_DFS:
#     print(t, end=' ')
# print()
# for t in travel_BFS:
#     print(t, end=' ')

# ---

import sys
from collections import deque

sys.setrecursionlimit(10000)

N, M, V = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    n1 -= 1
    n2 -= 1
    graph[n1][n2] = 1
    graph[n2][n1] = 1


def DFS(node):
    global visited
    global travel

    visited[node] = True
    travel.append(node)

    for j in range(N):
        if graph[node][j] == 1 and not visited[j]:
            DFS(j)

    return travel


def BFS(node):
    visited = [False for _ in range(N)]
    visited[node] = True

    q = deque([node])
    travel = [node]

    while q:
        n = q.popleft()

        for j in range(N):
            if graph[n][j] == 1 and not visited[j]:
                visited[j] = True
                q.append(j)
                travel.append(j)

    return travel


visited = [False for _ in range(N)]
travel = []
travel_DFS = DFS(V - 1)

travel_BFS = BFS(V - 1)

for t in travel_DFS:
    print(t + 1, end=' ')
print()
for t in travel_BFS:
    print(t + 1, end=' ')
