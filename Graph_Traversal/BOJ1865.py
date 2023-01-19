# 웜홀

import sys

input = sys.stdin.readline
INF = int(1e10)


def Bellman_Ford(start):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0

    for cnt in range(N):
        for edge in edges:
            cur, goal, weight = edge[0], edge[1], edge[2]
            if distance[goal] > distance[cur] + weight:
                distance[goal] = distance[cur] + weight
                if cnt == N - 1:  # 음의 사이클이 존재할 경우
                    return True
    return False


TC = int(input().strip())
result = []
for _ in range(TC):
    N, M, W = map(int, input().split())  # 지점의 수, 도로의 개수, 웜홀의 개수
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())  # 연결된 지점의 번호(S, E), 이 도로를 통해 이동 시 걸리는 시간
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())  # 연결된 지점의 번호(S, E), 이 도로를 통해 이동 시 줄어드는 시간
        edges.append((S, E, -T))

    hasNegativeCycle = Bellman_Ford(1)
    if hasNegativeCycle:
        result.append("YES")
    else:
        result.append("NO")

for r in result:
    print(r)
