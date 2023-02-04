# 연구소

import copy
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def spreadViruses():
    q = deque()
    viruses = copy.deepcopy(lab)
    for y in range(N):
        for x in range(M):
            if viruses[y][x] == 2:
                q.append((y, x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and viruses[ny][nx] == 0:
                viruses[ny][nx] = 2
                q.append((ny, nx))
    return viruses


def countSafeAreas():
    viruses = spreadViruses()
    safeAreas = 0
    for y in range(N):
        safeAreas += viruses[y].count(0)
    return safeAreas


def makeWalls(cnt):
    global result
    if cnt == 3:
        result = max(result, countSafeAreas())
        return
    for y in range(N):
        for x in range(M):
            if lab[y][x] == 0:
                lab[y][x] = 1
                makeWalls(cnt + 1)
                lab[y][x] = 0


result = -1
makeWalls(0)
print(result)
