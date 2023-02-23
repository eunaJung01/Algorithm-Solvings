# 크게 만들기

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
num = input().strip()

stack = []
cnt = K

for n in num:
    while stack and cnt > 0 and stack[-1] < n:
        stack.pop()
        cnt -= 1
    stack.append(n)

print("".join(stack[:N - K]))
