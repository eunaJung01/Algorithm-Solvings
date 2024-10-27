# NM과 K (1)

import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
num = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

result = -1000000
visited = [[0 for _ in range(M)] for _ in range(N)]  # v = 0 : not visited / v > 0 : visited


def func(y, x, cnt, acc):
    global result

    if cnt == K:
        result = max(result, acc)
        return

    for i in range(y, N):
        for j in range(x if i == y else 0, M):
            if visited[i][j] == 0:

                no = []
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if 0 <= ny < N and 0 <= nx < M:
                        no.append((ny, nx))
                        visited[ny][nx] += 1

                visited[i][j] += 1
                func(i, j, cnt + 1, acc + num[i][j])
                visited[i][j] -= 1

                for ny, nx in no:
                    visited[ny][nx] -= 1


if K == 1:
    for i in range(N):
        for j in range(M):
            result = max(result, num[i][j])
else:
    func(0, 0, 0, 0)
print(result)
