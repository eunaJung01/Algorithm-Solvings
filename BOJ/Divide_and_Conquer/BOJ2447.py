# 별 찍기 - 10

import sys

input = sys.stdin.readline

N = int(input().strip())
board = [[' ' for _ in range(N)] for _ in range(N)]


def star(ay, ax, by, bx):
    if by - ay == 2:
        cnt = 0
        for dy in range(3):
            for dx in range(3):
                if cnt != 4:
                    board[ay + dy][ax + dx] = "*"
                cnt += 1
        return

    cnt = 0
    d = (by - ay + 1) // 3
    for y in range(ay, by, d):
        for x in range(ax, bx, d):
            if cnt != 4:
                star(y, x, y + d - 1, x + d - 1)
            cnt += 1


star(0, 0, N - 1, N - 1)
for row in board:
    print((''.join(row)))
