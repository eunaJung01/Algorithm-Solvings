# 뱀

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())  # 보드의 크기
K = int(input().strip())  # 사과의 개수
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input().strip())  # 방향 변환 횟수
moves = deque()
for _ in range(L):
    X, C = map(str, input().split())  # X초가 끝난 뒤, 왼쪽(L) 또는 오른쪽(D)로 90도 방향을 회전
    moves.append((int(X), C))

# TODO: 방향 정의 (0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽)
direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

# TODO: 뱀 정의
head_y, head_x = 0, 0  # 머리 위치
d = 1  # 향하는 방향 : 오른쪽
snake = deque()  # (y좌표, x좌표)
snake.append((head_y, head_x))

# TODO: 보드 생성 (-1: 뱀, 0: 공백, 1: 사과)
board = [[0 for _ in range(N)] for _ in range(N)]
board[0][0] = -1  # 뱀
for apple_y, apple_x in apples:  # 사과
    board[apple_y - 1][apple_x - 1] = 1


def get_d(alpha):
    if alpha == "L":  # L: 왼쪽으로 회전
        return (d - 1) % 4
    return (d + 1) % 4  # D: 오른쪽으로 회전


time = 0
while True:
    time += 1

    # TODO: 이동
    # (1) 머리 다음 칸에 위치
    head_y += direction[d][0]
    head_x += direction[d][1]
    snake.append((head_y, head_x))

    if 0 <= head_y < N and 0 <= head_x < N:
        # TODO: 이동한 칸에 뱀이 있다면 종료
        if board[head_y][head_x] == -1:
            break

        # (2) 이동한 칸에 사과가 있다면
        if board[head_y][head_x] == 1:
            pass

        # (3) 이동한 칸에 사과가 없다면
        if board[head_y][head_x] == 0:
            tail_y, tail_x = snake.popleft()
            board[tail_y][tail_x] = 0

        # 뱀 머리 이동 표시
        board[head_y][head_x] = -1

        # TODO: 뱡향 전환
        if moves and time == moves[0][0]:
            d = get_d(moves[0][1])
            moves.popleft()

    # TODO: 이동한 칸에 벽이 있다면 종료
    else:
        break

print(time)
