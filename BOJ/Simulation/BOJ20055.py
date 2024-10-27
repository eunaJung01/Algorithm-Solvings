# 컨베이어 벨트 위의 로봇

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

robot = deque([False for _ in range(N)])  # 로봇 유무
A = deque(list(map(int, sys.stdin.readline().split())))  # 내구도

level = 0  # 단계

while True:
    level += 1

    # 1. 벨트 회전
    robot.appendleft(robot.pop())
    A.appendleft(A.pop())

    # 내리는 위치 : N-1
    if robot[N - 1]:
        robot[N - 1] = False

    # 2. 로봇 이동
    for i in range(N - 2, -1, -1):
        next = i + 1
        if robot[i] and not robot[next] and A[next] > 0:
            robot[i] = False
            if next != N - 1:  # 내리는 위치일 경우 로봇은 바로 내림
                robot[next] = True
            A[next] -= 1

    # 3. 올리는 위치 : 0
    if not robot[0] and A[0] > 0:
        robot[0] = True
        A[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 종료
    count = 0
    for i in range(2 * N):
        if A[i] == 0:
            count += 1
    if count >= K:
        break

print(level)
