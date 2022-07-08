# 마인크래프트

import sys

# NxM 집터 / 인벤토리 B개의 블록
N, M, B = map(int, sys.stdin.readline().split())

ground = []
max_h = -999
min_h = 999

for i in range(N):
    ground.append(list(map(int, sys.stdin.readline().split())))
    max_h = max(max_h, max(ground[i]))
    min_h = min(min_h, min(ground[i]))


def leveling(b, h):
    skip = 0
    time = 0

    for y in range(N):
        for x in range(M):
            g = ground[y][x]

            # h보다 높을 경우 → 블록 제거
            if g > h:
                num = g - h
                b += num  # 인벤토리 추가
                time += 2 * num

            # h보다 낮을 경우 → 블록 놓기
            elif g < h:
                num = h - g
                if b >= num:
                    b -= num  # 인벤토리 삭제
                    time += num
                else:
                    skip += num

            else:
                continue

    if skip != 0:
        if b >= skip:
            time += skip
        else:
            return 99999999

    return time


t = 99999999
h = 0

for i in range(min_h, max_h + 1):
    temp = leveling(B, i)
    if t >= temp:
        t = temp
        h = i

print(t, h)
