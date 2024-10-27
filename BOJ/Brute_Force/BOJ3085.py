# 사탕 게임

import sys

input = sys.stdin.readline

N = int(input().strip())
board = [list(input().strip()) for _ in range(N)]


def eat():
    answer = 0

    for y in range(N):
        cnt, pre_candy = 1, board[y][0]
        for x in range(1, N):
            if pre_candy == board[y][x]:
                cnt += 1
            else:
                pre_candy = board[y][x]
                cnt = 1
            answer = max(answer, cnt)

    for x in range(N):
        cnt, pre_candy = 1, board[0][x]
        for y in range(1, N):
            if pre_candy == board[y][x]:
                cnt += 1
            else:
                pre_candy = board[y][x]
                cnt = 1
            answer = max(answer, cnt)

    return answer


dy = (1, 0)
dx = (0, 1)

result = 0
for y in range(N):
    for x in range(N):
        for i in range(2):
            target_y = y + dy[i]
            target_x = x + dx[i]
            if 0 <= target_y < N and 0 <= target_x < N:
                cur_color, target_color = board[y][x], board[target_y][target_x]
                board[y][x] = target_color
                board[target_y][target_x] = cur_color
                result = max(result, eat())
                board[target_y][target_x] = target_color
                board[y][x] = cur_color
print(result)
