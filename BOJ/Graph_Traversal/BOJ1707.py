# 이분 그래프

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

RED, BLUE = 0, 1


def BFS(start_node):
    global graph, flags
    flags[start_node] = RED

    q = deque()
    q.append((start_node, RED))

    while q:
        pre_node, pre_flag = q.popleft()
        flag = BLUE if pre_flag == RED else RED

        nodes = graph[pre_node]
        for node in nodes:
            if flags[node] == -1:
                flags[node] = flag
                q.append((node, flag))
            else:
                if flags[node] != flag:
                    return False
    return True


def isBipartite():
    global flags
    for node in range(1, V + 1):
        if flags[node] == -1:
            if not BFS(node):
                return False
    return True


K = int(input().strip())
for _ in range(K):
    V, E = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(E):
        a, b, = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    flags = [-1 for _ in range(V + 1)]
    if isBipartite():
        print("YES")
    else:
        print("NO")
