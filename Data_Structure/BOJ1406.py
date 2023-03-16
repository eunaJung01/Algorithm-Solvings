# 에디터

# 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# line = deque(list(input().strip()))
# M = int(input().strip())
#
# cur = len(line)
# for _ in range(M):
#     inst = list(map(str, input().split()))
#     if len(inst) == 1:
#         if inst[0] == "L" and cur > 0:
#             cur -= 1
#         elif inst[0] == "D" and cur < len(line):
#             cur += 1
#         elif inst[0] == "B" and cur > 0:
#             line.remove(line[cur - 1])
#     else:
#         line.insert(cur, inst[1])
#         cur += 1
#
# print(''.join(line))

# ---

import sys

input = sys.stdin.readline

stack1 = list(input().strip())
stack2 = []
M = int(input().strip())

for _ in range(M):
    inst = list(map(str, input().split()))
    if inst[0] == "L":
        if stack1:
            stack2.append(stack1.pop())
    elif inst[0] == "D":
        if stack2:
            stack1.append(stack2.pop())
    elif inst[0] == "B":
        if stack1:
            stack1.pop()
    else:
        stack1.append(inst[1])

stack1.extend(reversed(stack2))
print(''.join(stack1))
