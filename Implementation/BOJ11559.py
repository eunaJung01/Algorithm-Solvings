# Puyo Puyo

import sys
from collections import deque

input = sys.stdin.readline

N, M = 12, 6
field = [list(input().strip()) for _ in range(N)]


def drop_puyo():
    global field
    new_field = [["." for _ in range(M)] for _ in range(N)]

    for j in range(M):
        new_column = []
        for i in range(N - 1, -1, -1):
            if field[i][j] != ".":
                new_column.append(field[i][j])
        for i in range(len(new_column)):
            new_field[N - 1 - i][j] = new_column[i]

    return new_field


dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def explode(i, j, color):
    global field, visited

    # TODO: 1. 폭발 범위를 확인한다. (상하좌우)
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    byeList = [(i, j)]

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and field[ny][nx] == color:
                visited[ny][nx] = True
                byeList.append((ny, nx))
                q.append((ny, nx))

    # TODO: 2. 같은 색 뿌요가 4개 이상 연결되어 있을 경우 폭발한다.
    if len(byeList) >= 4:
        for y, x in byeList:
            field[y][x] = "."
        return True
    return False


def explode_puyo():
    global visited

    explodeCnt = 0
    for i in range(N - 1, -1, -1):
        for j in range(M):
            if field[i][j] != "." and not visited[i][j]:
                explodeCnt = explodeCnt + 1 if explode(i, j, field[i][j]) else explodeCnt

    if explodeCnt != 0:
        return True
    return False


result = 0
while True:
    # TODO: 1. 뿌요가 중력의 영향으로 떨어진다.
    field = drop_puyo()

    # TODO: 2. 뿌요 폭발 & 연쇄를 시작한다.
    visited = [[False for _ in range(M)] for _ in range(N)]
    hasExploded = explode_puyo()

    # TODO: 3. 연쇄가 일어나지 않았다면 게임을 멈춘다.
    if hasExploded:
        result += 1
        continue
    break

print(result)
