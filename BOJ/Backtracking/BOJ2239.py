# 스도쿠

import sys

input = sys.stdin.readline

board = []
rowStats = [[False for _ in range(10)] for _ in range(9)]
colStats = [[False for _ in range(10)] for _ in range(9)]
boxStats = [[False for _ in range(10)] for _ in range(9)]

for y in range(9):
    line = input().strip()
    row = []
    for i, num in enumerate(line):
        num = int(num)
        if num != 0:
            rowStats[y][num] = True
            colStats[i][num] = True
        row.append(num)
    board.append(row)

cnt = 0
for y in range(0, 9, 3):
    for x in range(0, 9, 3):
        for i in range(3):
            for j in range(3):
                ny, nx = y + i, x + j
                num = board[ny][nx]
                if num != 0:
                    boxStats[cnt][num] = True
        cnt += 1


def findBoxIdx(y, x):
    i, j = y // 3, x // 3
    if i == 0 and j == 0:
        return 0
    elif i == 0 and j == 1:
        return 1
    elif i == 0 and j == 2:
        return 2
    elif i == 1 and j == 0:
        return 3
    elif i == 1 and j == 1:
        return 4
    elif i == 1 and j == 2:
        return 5
    elif i == 2 and j == 0:
        return 6
    elif i == 2 and j == 1:
        return 7
    elif i == 2 and j == 2:
        return 8


def backTracking(y, x, cnt):
    global result
    if cnt == 81:
        return True

    ny, nx = y, x + 1
    if nx == 9:
        ny += 1
        nx = 0

    if board[y][x] != 0:
        if backTracking(ny, nx, cnt + 1):
            return True
    else:
        for num in range(1, 10):
            if rowStats[y][num]:
                continue
            boxIdx = findBoxIdx(y, x)
            if not colStats[x][num] and not boxStats[boxIdx][num]:
                rowStats[y][num] = True
                colStats[x][num] = True
                boxStats[boxIdx][num] = True
                board[y][x] = num
                if backTracking(ny, nx, cnt + 1):
                    return True
                board[y][x] = 0
                boxStats[boxIdx][num] = False
                colStats[x][num] = False
                rowStats[y][num] = False


backTracking(0, 0, 0)
for row in board:
    for num in row:
        print(num, end="")
    print()
