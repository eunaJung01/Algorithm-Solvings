# 문자열 폭발

# 시간 초과 (45%)

# import sys
#
# input = sys.stdin.readline
#
# line = list(input().strip())
# explodingLine = list(input().strip())
#
# while True:
#     cnt, idx = 0, 0
#     temp = []
#     while True:
#         if idx >= len(line) - len(explodingLine) + 1:
#             while idx != len(line):
#                 temp.append(line[idx])
#                 idx += 1
#             break
#         if line[idx:idx + len(explodingLine)] == explodingLine:
#             cnt += 1
#             idx += len(explodingLine)
#         else:
#             temp.append(line[idx])
#             idx += 1
#     if cnt == 0:
#         break
#     line = temp
#
# if not line:
#     print("FRULA")
# else:
#     print(''.join(line))

# ---

import sys

input = sys.stdin.readline

line = list(input().strip())
explodingLine = list(input().strip())

stack = []
for l in line:
    stack.append(l)
    if l == explodingLine[-1] and len(stack) >= len(explodingLine):
        if stack[len(stack) - len(explodingLine):] == explodingLine:
            for _ in range(len(explodingLine)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
