# 2048 (Easy)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
initial_board = [list(map(int, input().split())) for _ in range(N)]

result = 2


def move(direction, board):
    new_board = [[0 for _ in range(N)] for _ in range(N)]

    # 상
    if direction == 0:
        for j in range(N):  # 열
            col = []
            for i in range(N):  # 행
                col.append(board[i][j])

            col, new_col = deque(col), []
            prev_lower = 0

            while col:
                if prev_lower != 0:
                    upper = prev_lower
                else:
                    upper = col.popleft()
                    if upper == 0:
                        continue

                lower, prev_lower = 0, 0
                while lower == 0 and col:
                    lower = col.popleft()
                if lower == 0:
                    new_col.append(upper)
                    prev_lower = 0
                    continue

                if upper == lower:
                    new_col.append(upper + lower)
                    prev_lower = 0
                else:
                    new_col.append(upper)
                    prev_lower = lower

            if prev_lower != 0:
                new_col.append(prev_lower)

            for r, num in enumerate(new_col):
                new_board[r][j] = num

    # 하
    elif direction == 1:
        for j in range(N):  # 열
            col = []
            for i in range(N - 1, -1, -1):  # 행
                col.append(board[i][j])

            col, new_col = deque(col), []
            prev_upper = 0

            while col:
                if prev_upper != 0:
                    lower = prev_upper
                else:
                    lower = col.popleft()
                    if lower == 0:
                        continue

                upper, prev_upper = 0, 0
                while upper == 0 and col:
                    upper = col.popleft()
                if upper == 0:
                    new_col.append(lower)
                    continue

                if lower == upper:
                    new_col.append(lower + upper)
                    prev_upper = 0
                else:
                    new_col.append(lower)
                    prev_upper = upper

            if prev_upper != 0:
                new_col.append(prev_upper)

            for r, num in enumerate(new_col):
                new_board[N - r - 1][j] = num

    # 왼쪽
    elif direction == 2:
        for i in range(N):  # 행
            row, new_row = deque(board[i]), []
            prev_right = 0

            while row:
                if prev_right != 0:
                    left = prev_right
                else:
                    left = row.popleft()
                    if left == 0:
                        continue

                right, prev_right = 0, 0
                while right == 0 and row:
                    right = row.popleft()
                if right == 0:
                    new_row.append(left)
                    continue

                if left == right:
                    new_row.append(left + right)
                    prev_right = 0
                else:
                    new_row.append(left)
                    prev_right = right

            if prev_right != 0:
                new_row.append(prev_right)

            for c, num in enumerate(new_row):
                new_board[i][c] = num

    # 오른쪽
    elif direction == 3:
        for i in range(N):  # 행
            row = []
            for j in range(N - 1, -1, -1):
                row.append(board[i][j])

            row, new_row = deque(row), []
            prev_left = 0

            while row:
                if prev_left != 0:
                    right = prev_left
                else:
                    right = row.popleft()
                if right == 0:
                    continue

                left, prev_left = 0, 0
                while left == 0 and row:
                    left = row.popleft()
                if left == 0:
                    new_row.append(right)
                    continue

                if right == left:
                    new_row.append(right + left)
                    prev_left = 0
                else:
                    new_row.append(right)
                    prev_left = left

            if prev_left != 0:
                new_row.append(prev_left)

            for c, num in enumerate(new_row):
                new_board[i][N - c - 1] = num

    return new_board


def DFS(cnt, board):
    global result

    if cnt == 5:
        for row in board:
            result = max(result, max(row))
        return

    for i in range(4):
        DFS(cnt + 1, move(i, board))


DFS(0, initial_board)
print(result)
