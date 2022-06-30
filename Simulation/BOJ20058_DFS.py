# 마법사 상어와 파이어스톰

import sys

sys.setrecursionlimit(10000)

N, Q = map(int, sys.stdin.readline().split())

grid = 2 ** N
ice = []  # 2^N X 2^N 격자
for _ in range(grid):
    ice.append(list(map(int, sys.stdin.readline().split())))

level = list(map(int, sys.stdin.readline().split()))  # 단계 L

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

for L in level:
    k = 2 ** L

    # 부분 격자 시작 좌표 (y, x)
    for y in range(0, grid, k):
        for x in range(0, grid, k):
            # 부분 격자 복사
            temp = [ice[i][x:x + k] for i in range(y, y + k)]

            # 회전
            for i in range(k):
                for j in range(k):
                    ice[y + j][x + k - 1 - i] = temp[i][j]

    # 녹아야 하는 얼음 찾기
    melt = []
    for y in range(grid):
        for x in range(grid):
            if ice[y][x] > 0:
                check = 0
                for i in range(4):
                    check_y = y + dy[i]
                    check_x = x + dx[i]
                    if 0 <= check_y < grid and 0 <= check_x < grid:
                        if ice[check_y][check_x] != 0:
                            check += 1
                if check < 3:
                    melt.append([y, x])

    # 얼음 융해
    for m_y, m_x in melt:
        ice[m_y][m_x] -= 1

visited = [[False for _ in range(grid)] for _ in range(grid)]


def DFS(y, x):
    visited[y][x] = True
    ans = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < grid and 0 <= nx < grid and ice[ny][nx] > 0 and not visited[ny][nx]:
            ans += DFS(ny, nx)

    return ans


left_ice = 0  # 남아있는 얼음의 합
mte = 0  # 가장 큰 얼음 뭉탱이
for y in range(grid):
    for x in range(grid):
        if ice[y][x] > 0:
            left_ice += ice[y][x]
            if not visited[y][x]:
                mte = max(mte, DFS(y, x))
print(left_ice)
print(mte)
