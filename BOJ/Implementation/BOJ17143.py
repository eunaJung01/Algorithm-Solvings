# 낚시왕

import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())
pool = [[-1 for _ in range(C + 1)] for _ in range(R + 1)]
human_y, human_x = 0, 0

sharks = []
sharks_life = [True for _ in range(M)]
for i in range(M):
    # (r, c): 위치 / s: 속력 / d: 이동 방향 / z: 크기
    r, c, s, d, z = map(int, input().split())
    pool[r][c] = i
    sharks.append([r, c, s, d, z])

# 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
directions = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}


def move(y, x, dy, dx, s):
    global moveCnt
    while True:
        ny = y + dy
        nx = x + dx
        if moveCnt == s or (dy != 0 and (ny == 0 or ny == R + 1)) or (dx != 0 and (nx == 0 or nx == C + 1)):
            return y, x
        y, x = ny, nx
        moveCnt += 1


# 움직일 수 있는 범위 - 행: 1 ~ R, 열: 1 ~ C
def moveSharks():
    global moveCnt
    p = [[-1 for _ in range(C + 1)] for _ in range(R + 1)]

    for i in range(M):
        if not sharks_life[i]:
            continue

        y, x, s, d, z = sharks[i]
        first_dy, first_dx = directions[d]
        second_dy, second_dx = directions[d + 1 if d == 1 or d == 3 else d - 1]

        moveCnt, cnt = 0, 0
        while moveCnt != s:
            if cnt % 2 == 0:
                dy, dx = first_dy, first_dx
            else:
                dy, dx = second_dy, second_dx
            cnt += 1

            if (dy, dx) == (-1, 0) and y - 1 <= s - moveCnt:
                moveCnt += y - 1
                y, x = 1, x
                continue
            elif (dy, dx) == (1, 0) and R - y <= s - moveCnt:
                moveCnt += R - y
                y, x = R, x
                continue
            elif (dy, dx) == (0, -1) and x - 1 <= s - moveCnt:
                moveCnt += x - 1
                y, x = y, 1
                continue
            elif (dy, dx) == (0, 1) and C - x <= s - moveCnt:
                moveCnt += C - x
                y, x = y, C
                continue

            y, x = move(y, x, dy, dx, s)

        sharks[i][0], sharks[i][1] = y, x
        sharks[i][3] = d if cnt % 2 != 0 else (d + 1 if d == 1 or d == 3 else d - 1)

        if p[y][x] != -1:
            preSharkIdx = p[y][x]
            if sharks[preSharkIdx][-1] > z:
                sharks_life[i] = False
            else:
                sharks_life[preSharkIdx] = False
                p[y][x] = i
        else:
            p[y][x] = i

    return p


fishing, moveCnt = 0, 0
for _ in range(1, C + 1):
    # TODO: 낚시왕이 오른쪽으로 한 칸 이동
    human_x += 1

    # TODO: 낚시왕이 있는 열에 있는 상어 중, 땅과 제일 가까운 상어를 잡음
    for y in range(1, R + 1):
        sharkIdx = pool[y][human_x]
        if sharkIdx != -1 and sharks_life[sharkIdx]:
            fishing += sharks[sharkIdx][-1]
            sharks_life[sharkIdx] = False
            pool[y][human_x] = -1
            break

    # TODO: 상어 이동
    pool = moveSharks()

print(fishing)
