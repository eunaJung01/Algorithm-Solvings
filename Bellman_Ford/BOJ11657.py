# 타임머신

import sys

input = sys.stdin.readline


def Bellman_Ford(start):
    time[start] = 0
    for cnt in range(N):
        for bus in buses:
            cur_node, next_node, weight = map(int, bus)
            if time[cur_node] != INF and time[next_node] > time[cur_node] + weight:
                time[next_node] = time[cur_node] + weight
                if cnt == N - 1:
                    return True
    return False


N, M = map(int, input().split())  # 도시의 개수, 버스 노선의 개수
buses = []
for _ in range(M):
    A, B, C = map(int, input().split())  # 시작 도시, 도착 도시, 이동하는데 걸리는 시간
    buses.append((A, B, C))

INF = int(1e10)
time = [INF for _ in range(N + 1)]
hasLoop = Bellman_Ford(1)

if hasLoop:
    print(-1)
else:
    for t in range(2, N + 1):
        if time[t] == INF:
            print(-1)
        else:
            print(time[t])
