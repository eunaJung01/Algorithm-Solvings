def solution(n, costs):
    sorted_by_edges = sorted(costs, key=lambda x: x[2])

    parent = [i for i in range(n)]
    answer = 0

    for n1, n2, w in sorted_by_edges:
        parent_n1 = find(parent, n1)
        parent_n2 = find(parent, n2)

        if parent_n1 != parent_n2:
            answer += w
            union(parent, parent_n1, parent_n2)

    return answer


def find(parent, n):
    while n != parent[n]:
        n = parent[n]
    return n


def union(parent, n1, n2):
    parent[max(n1, n2)] = min(n1, n2)
