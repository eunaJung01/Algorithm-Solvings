# 배열 복원하기

import sys

input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(H + X)]

A = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i - X >= 0 and j - Y >= 0:
            A[i][j] = B[i][j] - A[i - X][j - Y]
        else:
            A[i][j] = B[i][j]

for row in A:
    for r in row:
        print(r, end=' ')
    print()
