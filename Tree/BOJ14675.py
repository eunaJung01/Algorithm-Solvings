# 단절점과 단절선

import sys

N = int(sys.stdin.readline().strip())

tree = [[] for _ in range(N + 1)]  # 인접하는 노드 저장
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

q = int(sys.stdin.readline().strip())

result = []
for _ in range(q):
    t, k = map(int, sys.stdin.readline().split())

    # leaf 노드가 아닌 정점은 모두 단절점
    if t == 1:  # leaf node = 인접하는 노드가 1개 이하인 경우
        if len(tree[k]) <= 1:
            result.append("no")
        else:
            result.append("yes")

    # 입력으로 주어지는 것은 항상 트리 -> 모든 간선은 단절선
    if t == 2:
        result.append("yes")

for r in result:
    print(r)
