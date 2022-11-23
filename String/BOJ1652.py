# 누울 자리를 찾아라

import sys

input = sys.stdin.readline
N = int(input().strip())

room_row = [list(input()) for _ in range(N)]
room_col = [[room_row[i][j] for i in range(N)] for j in range(N)]


def find(li):
    cnt = 0
    for i in range(N):
        temp = 0
        for j in range(N):
            if li[i][j] == 'X':
                if temp >= 2:
                    cnt += 1
                temp = 0
            else:
                temp += 1
        if temp >= 2:
            cnt += 1
    return cnt


print(find(room_row), find(room_col))
