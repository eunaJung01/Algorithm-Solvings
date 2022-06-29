# 큐 2

# 시간 초과
# import sys
#
# N = int(sys.stdin.readline())
#
# queue = []
# for _ in range(N):
#     line = sys.stdin.readline().split()
#     inst = line[0]
#
#     if inst == "push":
#         queue.append(line[1])
#
#     elif inst == "pop":
#         if len(queue) != 0:
#             print(queue.pop(0))
#         else:
#             print(-1)
#
#     elif inst == "size":
#         print(len(queue))
#
#     elif inst == "empty":
#         if len(queue) != 0:
#             print(0)
#         else:
#             print(1)
#
#     elif inst == "front":
#         if len(queue) != 0:
#             print(queue[0])
#         else:
#             print(-1)
#
#     elif inst == "back":
#         if len(queue) != 0:
#             print(queue[-1])
#         else:
#             print(-1)
#
#     else:
#         break

# ---

import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque()
for _ in range(N):
    line = sys.stdin.readline().split()
    inst = line[0]

    if inst == "push":
        deq.append(line[1])

    elif inst == "pop":
        if len(deq) != 0:
            print(deq.popleft())
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