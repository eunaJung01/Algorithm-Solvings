# 테트로미노

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = 0


# ㅗ, ㅜ, ㅓ, ㅏ 모양 제외
def DFS(y, x, dsum, cnt):
    global result

    if cnt == 4:
        result = max(result, dsum)
        return

    # 상, 하, 좌, 우로 이동
    for n in range(4):
        ny = y + move[n][0]
        nx = x + move[n][1]
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True
            DFS(ny, nx, dsum + board[ny][nx], cnt + 1)
            visited[ny][nx] = False


# ㅗ, ㅜ, ㅓ, ㅏ 모양
def general4(i, j):
    global result
    for n in range(4):
        cur = board[i][j]
        for k in range(3):
            # move 배열의 요소를 3개씩 사용할 수 있도록 인덱스 계산
            # 012, 123, 230, 301
            t = (n + k) % 4
            ny = i + move[t][0]
            nx = j + move[t][1]

            if not (0 <= ny < N and 0 <= nx < M):
                cur = 0
                break
            cur += board[ny][nx]
        result = max(result, cur)


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i, j, board[i][j], 1)
        visited[i][j] = False
        general4(i, j)

print(result)
