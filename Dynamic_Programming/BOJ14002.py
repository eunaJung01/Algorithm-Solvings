# 가장 긴 증가하는 부분 수열 4

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

max_seq_len = max(dp)
print(max_seq_len)

seq = deque()
for i in range(N - 1, -1, -1):
    if dp[i] == max_seq_len:
        seq.appendleft(A[i])
        max_seq_len -= 1

for s in seq:
    print(s, end=' ')
