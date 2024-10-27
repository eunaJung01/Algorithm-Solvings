# 구슬 탈출 2

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
red_y, red_x, blue_y, blue_x, hole_y, hole_x = 0, 0, 0, 0, 0, 0

for y in range(N):
    line = input().strip()

    grid_row = []
    for x in range(M):
        if line[x] == "#":
            grid_row.append(line[x])
            continue

        if line[x] == "R":
            red_y, red_x = y, x
        if line[x] == "B":
            blue_y, blue_x = y, x
        if line[x] == "O":
            hole_y, hole_x = y, x
        grid_row.append([])

    grid.append(grid_row)

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def moveMarbles(i, y, x, board):
    flag = False
    ny, nx = y, x
    while True:
        if hole_y == ny and hole_x == nx:
            flag = True
        temp_y = ny + dy[i]
        temp_x = nx + dx[i]
        if board[temp_y][temp_x] == "#":
            return flag, ny, nx
        ny = temp_y
        nx = temp_x


def tiltBoard(i, ry, rx, by, bx, board):
    global flag
    rFlag, rny, rnx = moveMarbles(i, ry, rx, board)
    bFlag, bny, bnx = moveMarbles(i, by, bx, board)

    # 두 구슬이 같은 위치로 이동할 경우
    if rny == bny and rnx == bnx:
        # 윗쪽 : 아랫쪽 구슬 y += 1
        if i == 0:
            if ry < by:
                bny += 1
            else:
                rny += 1
        # 아랫쪽 : 윗쪽 구슬 y -= 1
        elif i == 1:
            if ry > by:
                bny -= 1
            else:
                rny -= 1
        # 왼쪽 : 오른쪽 구슬 x += 1
        elif i == 2:
            if rx < bx:
                bnx += 1
            else:
                rnx += 1
        # 오른쪽 : 왼쪽 구슬 x -= 1
        elif i == 3:
            if rx > bx:
                bnx -= 1
            else:
                rnx -= 1

    if bFlag:
        return ry, rx, by, bx
    if rFlag:
        flag = True
    return rny, rnx, bny, bnx


def BFS():
    global grid
    grid[red_y][red_x].append((red_y, red_x, blue_y, blue_x))
    grid[blue_y][blue_x].append((red_y, red_x, blue_y, blue_x))
    q = deque([(red_y, red_x, blue_y, blue_x, grid, 0)])

    while q:
        ry, rx, by, bx, board, cnt = q.popleft()

        # TODO: 종료 조건
        if ry == hole_y and rx == hole_x:
            if by == hole_y and by == hole_y:  # 구멍에 동시에 빠질 경우 실패
                continue
            else:
                return cnt
        if cnt >= 10:  # 움직임 10번 이상
            return -1

        # TODO: 보드 기울이기
        for i in range(4):
            rny, rnx, bny, bnx = tiltBoard(i, ry, rx, by, bx, board)
            if flag:
                return cnt + 1
            if board[rny][rnx] and ((rny, rnx, bny, bnx) in board[rny][rnx]):
                continue
            elif board[bny][bnx] and ((rny, rnx, bny, bnx) in board[bny][bnx]):
                continue
            else:
                board[rny][rnx].append((rny, rnx, bny, bnx))
                board[bny][bnx].append((rny, rnx, bny, bnx))
                q.append((rny, rnx, bny, bnx, board, cnt + 1))
    return -1


flag = False
print(BFS())
