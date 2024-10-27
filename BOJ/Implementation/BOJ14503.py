# 로봇 청소기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # 세로, 가로
robot_y, robot_x, d = map(int, input().split())  # 로봇 청소기가 있는 칸의 좌표, 방향
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

# 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}


def find(y, x, d):
    for _ in range(4):
        d = (d - 1) % 4  # 회전
        dy, dx = direction[d]
        ny, nx = y + dy, x + dx
        if room[ny][nx] == 1 or visited[ny][nx]:
            continue
        return True, ny, nx, d
    return False, y, x, d


clean = 0
while True:
    # TODO: 1. 현재 위치 청소
    if not visited[robot_y][robot_x]:
        clean += 1
    visited[robot_y][robot_x] = True

    # TODO: 2. 반시계 방향으로 탐색
    hasPlaceToClean, robot_y, robot_x, d = find(robot_y, robot_x, d)

    # TODO: (1) 청소할 공간이 있다면
    if hasPlaceToClean:
        continue
    # TODO: (2) 청소할 공간이 없다면
    else:
        dy, dx = direction[d]
        robot_y -= dy
        robot_x -= dx
        if room[robot_y][robot_x] == 1:
            break

print(clean)
