# 별 찍기 - 11

import sys


def star(head_y, head_x, height):
    if height == 3:
        board[head_y][head_x] = "*"
        board[head_y + 1][head_x - 1] = "*"
        board[head_y + 1][head_x + 1] = "*"
        for i in range(5):
            board[head_y + 2][head_x - 2 + i] = "*"
        return

    new_height = height // 2
    new_bottom = new_height * 2 - 1
    star(head_y, head_x, new_height)
    star(head_y + new_height, head_x - new_bottom // 2 - 1, new_height)
    star(head_y + new_height, head_x + new_bottom // 2 + 1, new_height)


N = int(sys.stdin.readline().strip())
R, C = 2 * N - 1, N
board = [[" " for _ in range(R)] for _ in range(C)]

star(0, N - 1, N)
for row in board:
    print(''.join(row))
