# 서강근육맨

import sys

N = int(sys.stdin.readline().strip())

t = list(map(int, sys.stdin.readline().split()))
t.sort()

if len(t) % 2 == 1:
    t.pop()

result = 0
for _ in range(len(t) // 2):
    result = max(result, t.pop() + t.pop(0))

print(result)
