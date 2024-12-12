from collections import deque

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = True

    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx]:
                continue
            if maps[ny][nx] == 0:
                continue
            if ny == n - 1 and nx == m - 1:
                return cnt + 1
            visited[ny][nx] = True
            q.append((ny, nx, cnt + 1))
    return -1
