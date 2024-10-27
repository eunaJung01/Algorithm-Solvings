# 풍선 터뜨리기

import sys
from collections import deque

N = int(sys.stdin.readline().strip())
nums = [num for num in map(int, sys.stdin.readline().strip().split())]

balloons = deque()  # [풍선 번호, 번호] - 원형 큐
for num in range(1, N + 1):
    balloons.append([num, nums[num - 1]])

result = []

while len(balloons) != 0:
    now = balloons.popleft()
    result.append(now[0])
    nowNum = now[1]

    if len(balloons) == 0:
        break

    if nowNum > 0:  # 번호가 양수일 경우
        nowNum -= 1
        while nowNum != 0:
            balloons.append(balloons.popleft())
            nowNum -= 1

    else:  # 번호가 음수일 경우
        while nowNum != 0:
            balloons.appendleft(balloons.pop())
            nowNum += 1

for r in result:
    print(r, end=" ")
