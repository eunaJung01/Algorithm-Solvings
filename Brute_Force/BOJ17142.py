# 연구소 3

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
lab = []
virus = []
blank_num = 0
ans = sys.maxsize

for y in range(N):
    row = list(map(int, input().split()))
    for x in range(N):
        if row[x] == 2:
            virus.append((y, x))
        elif row[x] == 0:
            blank_num += 1
    lab.append(row)

virus_num = len(virus)
isActive = [False for _ in range(virus_num)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


# 확산 : BFS
def spread_virus(blanks):
    global ans

    time = 0
    q = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]

    for id in range(virus_num):
        if isActive[id]:
            y, x = virus[id]
            q.append((y, x))

    while True:
        if blanks == 0:
            ans = min(ans, time)
            return
        if len(q) == 0:
            return

        time += 1
        if time >= ans:
            return

        for _ in range(len(q)):
            y, x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                # 빈 칸 또는 비활성 바이러스에게 전파
                if 0 <= ny < N and 0 <= nx < N \
                        and (lab[ny][nx] == 0 or lab[ny][nx] == 2) and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    if lab[ny][nx] == 0:
                        blanks -= 1


# 활성 바이러스 M개 선정 : DFS
def activate_virus(id, cnt):
    global isActive
    if cnt == M:
        spread_virus(blank_num)
        return

    for i in range(id, virus_num):
        if not isActive[i]:
            isActive[i] = True
            activate_virus(i, cnt + 1)
            isActive[i] = False


activate_virus(0, 0)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
