# 주사위 굴리기

import sys

input = sys.stdin.readline

N, M, dice_y, dice_x, K = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [0 for _ in range(7)]
move = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}  # 동: 1, 서: 2, 북: 3, 남: 4
result = []

for c in commands:
    # TODO: 주사위 이동
    dy, dx = move[c][0], move[c][1]
    if 0 <= dice_y + dy < N and 0 <= dice_x + dx < M:
        dice_y += dy
        dice_x += dx
        if c == 1:  # 동
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        elif c == 2:  # 서
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
        elif c == 3:  # 북
            dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
        else:  # 남
            dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    else:
        continue

    # TODO: 윗면 출력
    result.append(dice[6])

    # TODO: 지도에 따른 동작
    if ground[dice_y][dice_x] == 0:
        ground[dice_y][dice_x] = dice[1]
    else:
        dice[1] = ground[dice_y][dice_x]
        ground[dice_y][dice_x] = 0

for r in result:
    print(r)
