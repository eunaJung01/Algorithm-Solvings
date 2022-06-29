# 덱

import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque()
for _ in range(N):
    line = sys.stdin.readline().split()
    inst = line[0]

    if inst == "push_front":
        deq.appendleft(line[1])

    elif inst == "push_back":
        deq.append(line[1])

    elif inst == "pop_front":
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)

    elif inst == "pop_back":
        if len(deq) != 0:
            print(deq.pop())
        else:
            print(-1)

    elif inst == "size":
        print(len(deq))

    elif inst == "empty":
        if len(deq) != 0:
            print(0)
        else:
            print(1)

    elif inst == "front":
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)

    elif inst == "back":
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)

    else:
        break
