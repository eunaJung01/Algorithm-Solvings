# 빗물

import sys

H, W = map(int, sys.stdin.readline().split())
world = list(map(int, sys.stdin.readline().split()))

well = 0  # 고인 물
next_i = 0
for i in range(len(world) - 1):
    h = world[i]
    if h != 0:
        for water_h in range(1, h + 1):
            for j in range(i + 1, len(world)):
                now_h = world[j]
                if now_h >= water_h:
                    well += j - i - 1
                    next_i = max(next_i, j)
                    break
    i = next_i

print(well)
