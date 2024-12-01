from collections import deque

INF = int(1e9)

# 방향 : 0, 1, 2, 3
dy = (0, 0, 1, -1)
dx = (1, -1, 0, 0)
pay = {"straight": 100, "corner": 500}


def solution(board):
    n = len(board)

    min_pay = [[[INF for _ in range(4)] for _ in range(n)] for _ in range(n)]
    for i in range(4):
        min_pay[0][0][i] = 0

    q = deque()

    if board[0][1] == 0:
        q.append((0, 1, 0))
        min_pay[0][1][0] = pay["straight"]

    if board[1][0] == 0:
        q.append((1, 0, 2))
        min_pay[1][0][2] = pay["straight"]

    while q:
        y, x, prev_d = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if board[ny][nx] == 1:
                continue

            new_pay = min_pay[y][x][prev_d] + pay["straight"]
            if get_road_type(prev_d, d) == "corner":
                new_pay += pay["corner"]

            if new_pay >= min_pay[ny][nx][d]:
                continue

            min_pay[ny][nx][d] = new_pay
            if ny == n - 1 and nx == n - 1:
                continue
            q.append((ny, nx, d))

    return min(min_pay[n - 1][n - 1])


def get_road_type(d1, d2):
    if d1 in (0, 1) and d2 in (0, 1):
        return "straight"
    if d1 in (2, 3) and d2 in (2, 3):
        return "straight"
    return "corner"
