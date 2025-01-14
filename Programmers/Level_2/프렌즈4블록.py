dy = (0, 1, 1)
dx = (1, 1, 0)

BLANK = 'X'


def solution(m, n, board):
    for i, row in enumerate(board):
        board[i] = [s for s in row]

    answer = 0
    while True:
        q = set()

        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == BLANK:
                    continue

                pop_list = get_pop_list(board, i, j)
                if len(pop_list) == 4:
                    for p in pop_list:
                        q.add(p)

        if len(q) == 0:
            return answer
        answer += len(q)

        for y, x in q:
            board[y][x] = BLANK
        push_blocks_down(board, m, n)


def get_pop_list(board, i, j):
    target = board[i][j]
    cnt = 1
    temp = [(i, j)]
    for k in range(3):
        ny = i + dy[k]
        nx = j + dx[k]
        if board[ny][nx] == target:
            temp.append((ny, nx))
            cnt += 1
    return temp


def push_blocks_down(board, m, n):
    for j in range(n):
        y_string = ""
        for i in range(m):
            y_string += board[i][j]
        y_string = y_string.replace(BLANK, '')

        pos = 0
        for i in range(m):
            if i < m - len(y_string):
                board[i][j] = BLANK
                continue
            board[i][j] = y_string[pos]
            pos += 1
