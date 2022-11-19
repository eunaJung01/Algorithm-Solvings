# 보물

import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for _ in range(N):
    result += A.pop(A.index(min(A))) * B.pop(B.index(max(B)))
print(result)
