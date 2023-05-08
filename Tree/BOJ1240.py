# 노드사이의 거리

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())
tree = defaultdict(list)
for _ in range(N - 1):
    a, b, w = map(int, input().split())
    tree[a].append((b, w))
    tree[b].append((a, w))


def BFS(start_node, end_node):
    visited = [False for _ in range(N + 1)]
    visited[start_node] = True

    q = deque()
    for next_node, next_w in tree[start_node]:
        q.append((next_node, next_w))
        visited[next_node] = True

    while q:
        node, w = q.popleft()
        if node == end_node:
            return w
        for next_node, next_w in tree[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append((next_node, w + next_w))


for _ in range(M):
    a, b = map(int, input().split())
    print(BFS(a, b))
