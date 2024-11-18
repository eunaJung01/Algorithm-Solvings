from collections import defaultdict, deque

INF = int(1e9)


def solution(n, vertex):
    edges = defaultdict(list)
    for e1, e2 in vertex:
        edges[e1].append(e2)
        edges[e2].append(e1)

    min_distances = [INF] * (n + 1)
    min_distances[1] = 0

    q = deque()
    q.append((1, 1))

    while q:
        node, distance = q.popleft()
        for next_node in edges[node]:
            if distance >= min_distances[next_node]:
                continue
            min_distances[next_node] = distance
            q.append((next_node, distance + 1))

    max_distance = 0
    answer = 0
    for i in range(2, n + 1):
        if min_distances[i] == max_distance:
            answer += 1
            continue
        if min_distances[i] > max_distance:
            max_distance = min_distances[i]
            answer = 1
    return answer
