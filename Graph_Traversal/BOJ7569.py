# 토마토

import sys
from collections import deque

dz = (1, -1, 0, 0, 0, 0)
dy = (0, 0, -1, 0, 1, 0)
dx = (0, 0, 0, -1, 0, 1)


def BFS():
    global q
    ans = 0

    q.append(-1)  # -1 : 하루동안 익은 토마토의 범위를 표시하기 위함
    while q:
        temp = q.popleft()

        if temp == -1:  # 전날 익은 토마토에 대하여 전부 탐색했을 때
            if len(q) != 0:  # 새로 익은 토마토가 있는 경우
                q.append(-1)
                ans += 1
            else:  # 새로 익은 토마토가 없는 경우
                break

        else:
            z, y, x = temp[0], temp[1], temp[2]
            for i in range(6):
                nz = z + dz[i]
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomato[nz][ny][nx] == 0:
                    tomato[nz][ny][nx] = 1
                    q.append((nz, ny, nx))

    return ans


M, N, H = map(int, sys.stdin.readline().split())  # M : 가로 / N : 세로 / H : 높이

result = 0  # 출력값 (저장될 때부터 모든 토마토 익음 : 0 / 토마토가 모두 익지는 못함 : -1 / 최소 일수)
status = False

tomato = []  # 1 : 익음 / 0 : 익지 않음 / -1 : 없음
q = deque()  # 익은 토마토의 위치 (h, n, m)

for h in range(H):  # 밑 상자 ~ 윗 상자
    tomato.append([])
    for n in range(N):
        line = list(map(int, sys.stdin.readline().split()))

        for m in range(M):
            if line[m] == 1:  # 익은 토마토 -> 큐에 삽입
                q.append((h, n, m))
            if line[m] == 0:
                status = True

        tomato[h].append(line)

# 익지 않은 토마토가 있는 경우
if status:
    result = BFS()  # 너비 우선 탐색

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == 0:  # 익지 못하는 토마토가 있는 경우
                    result = -1

print(result)
