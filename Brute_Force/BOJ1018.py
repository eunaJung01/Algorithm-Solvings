# 체스판 다시 칠하기

import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    board.append(list(sys.stdin.readline().strip()))

dic = {'W': 0, 'B': 1}


def paint(b):
    check1 = dic[b[0][0]]
    check2 = 0 if check1 == 1 else 1

    count1 = 0
    count2 = 0

    for y in range(8):
        for x in range(8):
            if dic[b[y][x]] != check1:
                count1 += 1
            else:
                count2 += 1
            check1 = 0 if check1 == 1 else 1
            check2 = 0 if check2 == 1 else 1
        check1 = 0 if check1 == 1 else 1
        check2 = 0 if check2 == 1 else 1
    return min(count1, count2)


result = 9999999
for start_y in range(N - 7):
    for start_x in range(M - 7):

        b = []
        for y in range(start_y, start_y + 8):
            b.append(board[y][start_x:start_x + 8])

        result = min(result, paint(b))

print(result)
