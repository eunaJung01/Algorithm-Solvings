# 개똥벌레

import sys

input = sys.stdin.readline

N, H = map(int, input().split())

upper, lower = [], []
for _ in range(N // 2):
    upper.append(int(input().strip()))
    lower.append(int(input().strip()))
upper.sort()
lower.sort()


def check(height, cave):
    l, r = 0, len(cave) - 1
    while l <= r:
        mid = (l + r) // 2
        if cave[mid] <= height:
            l = mid + 1
        else:
            r = mid - 1

    return len(cave) - (r + 1)


min_obstacleNum, cnt = sys.maxsize, 0
for i in range(1, H + 1):
    upper_cnt = check(i - 1, upper)
    lower_cnt = check(H - i, lower)
    cur_cnt = upper_cnt + lower_cnt

    if cur_cnt < min_obstacleNum:
        min_obstacleNum = cur_cnt
        cnt = 1
    elif cur_cnt == min_obstacleNum:
        cnt += 1

print(min_obstacleNum, cnt)
