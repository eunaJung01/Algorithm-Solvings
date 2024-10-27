# 최소 스패닝 트리

import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split())  # 노드의 수, 간선의 수
visited = [False for _ in range(V + 1)]  # 노드 방문 정보

# 무방향 그래프 (가중치, 자기 자신, 연결된 노드)
graph = defaultdict(list)
for _ in range(E):
    A, B, C = map(int, input().split())  # A번 정점, B번 정점, 가중치 C
    graph[A].append((C, A, B))
    graph[B].append((C, B, A))


def prim(graph, start_node):
    visited[start_node] = True

    mst = []
    min_weight = 0

    # 우선순위 큐
    candidate_edge = graph[start_node]
    heapq.heapify(candidate_edge)

    while candidate_edge:
        w, a, b = heapq.heappop(candidate_edge)

        if not visited[b]:
            visited[b] = True
            mst.append((a, b))
            min_weight += w

            for edge in graph[b]:
                if not visited[edge[2]]:
                    heapq.heappush(candidate_edge, edge)

    return min_weight


print(prim(graph, 1))
