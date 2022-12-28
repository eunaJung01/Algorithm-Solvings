# 행성 터널

import sys

input = sys.stdin.readline

N = int(input().strip())
planets = [(i, list(map(int, input().split()))) for i in range(N)]  # 행성 번호, [x좌표, y좌표, z좌표]
parent = [i for i in range(N)]


def calc_weight(planet1_loc, planet2_loc):
    return min(abs(planet1_loc[0] - planet2_loc[0]), abs(planet1_loc[1] - planet2_loc[1]),
               abs(planet1_loc[2] - planet2_loc[2]))


weight = []  # 행성1, 행성2, 가중치
for i in range(3):
    sorted_planets = sorted(planets, key=lambda x: x[1][i])
    for j in range(N - 1):
        planet1, planet2 = sorted_planets[j], sorted_planets[j + 1]
        w = calc_weight(planet1[1], planet2[1])
        weight.append((planet1[0], planet2[0], w))
weight.sort(key=lambda x: x[2])


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


result = 0
for p1, p2, w in weight:
    p1_parent, p2_parent = find(p1), find(p2),
    if p1_parent != p2_parent:
        if p1_parent > p2_parent:
            parent[p1_parent] = p2_parent
        else:
            parent[p2_parent] = p1_parent
        result += w
print(result)
