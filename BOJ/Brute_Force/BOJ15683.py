# 감시

import copy
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
room, cctv_info = [], []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if 1 <= row[j] <= 5:
            cctv_info.append((i, j, row[j]))
    room.append(row)

cctv = {1: [[0], [1], [2], [3]],
        2: [[2, 3], [0, 1]],
        3: [[0, 3], [3, 1], [1, 2], [2, 0]],
        4: [[2, 0, 3], [0, 3, 1], [3, 1, 2], [1, 2, 0]],
        5: [[0, 1, 2, 3]]}
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def watch(room, cctv_y, cctv_x, direction):
    room_checked = copy.deepcopy(room)
    q = deque()
    for d in direction:
        q.append((cctv_y, cctv_x, d))

    while q:
        y, x, d = q.popleft()
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if room[ny][nx] == 0:
                room_checked[ny][nx] = -1
                q.append((ny, nx, d))
            elif room[ny][nx] == 6:
                continue
            else:  # CCTV 통과, -1
                q.append((ny, nx, d))
    return room_checked


def countBlindSpot(room):
    cnt = 0
    for i in range(N):
        cnt += room[i].count(0)
    return cnt


def DFS(room, depth):
    global answer
    if depth == len(cctv_info):
        answer = min(answer, countBlindSpot(room))
        return

    y, x, cctvNum = cctv_info[depth]
    for direction in cctv[cctvNum]:
        room_checked = watch(room, y, x, direction)
        DFS(room_checked, depth + 1)


answer = int(sys.maxsize)
DFS(room, 0)
print(answer)
