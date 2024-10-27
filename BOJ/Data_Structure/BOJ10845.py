# 큐

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
q = deque()

for _ in range(N):
    line = list(map(str, input().split()))

    if len(line) == 1:
        command = line[0]

        if command == "pop":
            if len(q) == 0:
                print(-1)
            else:
                print(q.popleft())

        if command == "size":
            print(len(q))

        if command == "empty":
            if len(q) == 0:
                print(1)
            else:
                print(0)

        if command == "front":
            if len(q) == 0:
                print(-1)
            else:
                print(q[0])

        if command == "back":
            if len(q) == 0:
                print(-1)
            else:
                print(q[-1])

    else:
        command, num = line[0], int(line[1])
        if command == "push":
            q.append(num)
