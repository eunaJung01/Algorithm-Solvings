# 도시 분할 계획

import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # 집의 개수, 길의 개수
root = [i for i in range(N + 1)]

town = [list(map(int, input().split())) for _ in range(M)]  # A번 집, B번 집, 유지비 C
town.sort(key=lambda x: x[2])  # 가중치 기준 오름차순 정렬


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


result = 0
selected = []
for a, b, w in town:
    root_a, root_b = find(a), find(b)
    if root_a != root_b:
        if root_a > root_b:
            root[root_a] = root_b
        else:
            root[root_b] = root_a
        result += w
        selected.append(w)

result -= selected.pop()
print(result)
