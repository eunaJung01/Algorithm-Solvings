# 나무 재테크

import sys
from math import trunc

input = sys.stdin.readline

N, M, K = map(int, input().split())  # 땅의 크기 N×N, 나무 개수 M개, K년

ground = [[5 for _ in range(N)] for _ in range(N)]  # 저장된 값은 양분
S2D2 = []  # 추가하는 양분
for y in range(N):
    S2D2.append(list(map(int, input().split())))

trees = [[[] for _ in range(N)] for _ in range(N)]  # 나무들
for _ in range(M):
    y, x, z = map(int, input().split())  # (y, x), 나무의 나이
    trees[y - 1][x - 1].append(z)

dy = (-1, -1, -1, 0, 0, 1, 1, 1)
dx = (-1, 0, 1, -1, 1, -1, 0, 1)

for _ in range(K):
    # TODO: 봄
    dead_trees = []
    for y in range(N):
        for x in range(N):
            if len(trees[y][x]) != 0:
                update = []
                for age in trees[y][x]:
                    if ground[y][x] >= age:
                        ground[y][x] -= age
                        update.append(age + 1)
                    else:
                        dead_trees.append((y, x, age))
                trees[y][x] = update

    # TODO: 여름
    for y, x, age in dead_trees:
        ground[y][x] += trunc(age / 2)

    # TODO: 가을
    update = [[[] for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if len(trees[y][x]) != 0:
                for age in trees[y][x]:
                    if age % 5 == 0:
                        for i in range(8):
                            ny = y + dy[i]
                            nx = x + dx[i]
                            if 0 <= ny < N and 0 <= nx < N:
                                update[ny][nx].append(1)
                    update[y][x].append(age)

    for y in range(N):
        for x in range(N):
            if len(update[y][x]) >= 2:
                update[y][x].sort()
    trees = update

    # TODO: 겨울
    for y in range(N):
        for x in range(N):
            ground[y][x] += S2D2[y][x]

tree_cnt = 0
for y in range(N):
    for x in range(N):
        tree_cnt += len(trees[y][x])
print(tree_cnt)
