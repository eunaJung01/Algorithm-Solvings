# 오큰수

import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

nge = [-1 for _ in range(N)]
stack = [0]
idx = 1

while stack and idx < N:
    while stack and A[stack[-1]] < A[idx]:
        nge[stack[-1]] = A[idx]
        stack.pop()
    stack.append(idx)
    idx += 1

for n in nge:
    print(n, end=' ')
