# 파티

import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())  # 학생 수, 도로의 개수, 파티를 하는 마을 번호

roads = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, T = map(int, input().split())  # 시작점, 끝점, 소요 시간
    roads[start].append([end, T])


def dijkstra_come(start_node):
    dp = [INF for _ in range(N + 1)]
    dp[start_node] = 0
    q = [(0, start_node)]
    heapq.heapify(q)

    while q:
        time, node = heapq.heappop(q)
        if node == X:
            return time
        for next_node, t in roads[node]:
            if dp[next_node] > time + t:
                dp[next_node] = time + t
                heapq.heappush(q, (time + t, next_node))


def dijkstra_go_back():
    q = []
    for next_node, t in roads[X]:
        q.append((t, next_node))
        go_back[next_node] = t
    heapq.heapify(q)

    while q:
        time, node = heapq.heappop(q)
        for next_node, t in roads[node]:
            if go_back[next_node] > time + t:
                go_back[next_node] = time + t
                heapq.heappush(q, (time + t, next_node))


INF = int(1e10)
come, go_back = [INF for _ in range(N + 1)], [INF for _ in range(N + 1)]
come[X], go_back[X] = 0, 0

for i in range(1, N + 1):
    if i != X:
        come[i] = dijkstra_come(i)
dijkstra_go_back()

result = 0
for i in range(1, N + 1):
    result = max(result, come[i] + go_back[i])
print(result)
