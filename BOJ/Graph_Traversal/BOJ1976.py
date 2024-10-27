# 여행 가자

import sys

input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

parent = [i for i in range(N + 1)]
graph = []

for i in range(N):
    graph.append([idx + 1
                  for idx, flag in enumerate(list(map(int, input().split())))
                  if flag == 1])

travel_cities = list(map(int, input().split()))


def union(a, b):
    parent_a, parent_b = find(a), find(b)
    parent[max(parent_a, parent_b)] = min(parent_a, parent_b)


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]


for i, cities in enumerate(graph):
    for city in cities:
        union(i + 1, city)

result = True
root = parent[travel_cities[0]]
for travel_city in travel_cities[1:]:
    if parent[travel_city] != root:
        result = False
        break

if result:
    print("YES")
else:
    print("NO")
