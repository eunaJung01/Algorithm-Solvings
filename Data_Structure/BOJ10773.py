# 제로

import sys

input = sys.stdin.readline

K = int(input().strip())
stack = []
for _ in range(K):
    num = int(input().strip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
