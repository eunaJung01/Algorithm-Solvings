# 톱니바퀴

import sys
from collections import deque

input = sys.stdin.readline

gears = []  # 오른쪽 : 2, 왼쪽 : 6
for _ in range(4):
    gear = []
    line = input().strip()
    for l in line:
        gear.append(int(l))
    gears.append(gear)

K = int(input().strip())
move = []  # 톱니바퀴 번호, 방향
for _ in range(K):
    gearNum, direction = map(int, input().split())
    move.append((gearNum - 1, direction))


def getDirections(gearNum):
    leftGearNum, rightGearNum = gearNum - 1, gearNum + 1
    if 0 <= leftGearNum < 4 and not visited[leftGearNum]:  # 왼쪽
        visited[leftGearNum] = True
        if gears[leftGearNum][2] != gears[gearNum][6]:  # 극이 다른 경우
            gearDirections[leftGearNum] = gearDirections[gearNum] * -1  # 반대 방향으로 회전
            getDirections(leftGearNum)
    if 0 <= rightGearNum < 4 and not visited[rightGearNum]:  # 오른쪽
        visited[rightGearNum] = True
        if gears[gearNum][2] != gears[rightGearNum][6]:  # 극이 다른 경우
            gearDirections[rightGearNum] = gearDirections[gearNum] * -1  # 반대 방향으로 회전
            getDirections(rightGearNum)


def rotate(gear, direction):
    if direction == 1:  # 시계 방향
        gear.appendleft(gear.pop())
    elif direction == -1:  # 반시계 방향
        gear.append(gear.popleft())
    return list(gear)


# 방향 0 : 회전하지 않음, 1 : 시계 방향(pop->pushLeft), -1 : 반시계 방향 (popLeft->push)
for gearNum, direction in move:
    # TODO: 각 톱니바퀴들 회전 방향 계산
    gearDirections, visited = [0 for _ in range(4)], [False for _ in range(4)]
    gearDirections[gearNum], visited[gearNum] = direction, True
    getDirections(gearNum)

    # TODO: 회전
    for gearNum, direction in enumerate(gearDirections):
        gears[gearNum] = rotate(deque(gears[gearNum]), direction)

gearScores = (1, 2, 4, 8)
score = 0
for gearNum, gear in enumerate(gears):
    score += gear[0] * gearScores[gearNum]
print(score)
