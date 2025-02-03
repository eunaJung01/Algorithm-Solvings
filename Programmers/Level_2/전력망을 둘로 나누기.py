INF = int(1e9)


def solution(n, wires):
    wire_map = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        wire_map[v1].append(v2)
        wire_map[v2].append(v1)

    linked_node_cnt = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # linked_node_cnt[a][b] == a-b 간선을 지우는 경우, b와 연결된 노드의 수
    visited = [False for _ in range(n + 1)]

    def dfs(node):
        visited[node] = True
        cnt = 0
        for next_node in wire_map[node]:
            if visited[next_node]:
                continue
            partial_cnt = dfs(next_node) + 1
            linked_node_cnt[node][next_node] = partial_cnt
            cnt += partial_cnt
        return cnt

    dfs(1)

    answer = INF
    for node in range(1, n + 1):
        for next_node in wire_map[node]:
            answer = min(abs(n - 2 * (linked_node_cnt[node][next_node])), answer)
    return answer
