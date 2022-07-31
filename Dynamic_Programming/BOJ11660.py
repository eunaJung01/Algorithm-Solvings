# 구간 합 구하기 5

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, N + 1):
        arr[i][j] = temp[j - 1]

# 1. 행 별로 더하기
for i in range(1, N + 1):
    for j in range(1, N):
        arr[i][j + 1] += arr[i][j]

# 2. 열 별로 더하기
for j in range(1, N + 1):
    for i in range(1, N):
        arr[i + 1][j] += arr[i][j]

point = []  # [x1, y1, x2, y2]
for _ in range(M):
    point.append(list(map(int, sys.stdin.readline().split())))

for x1, y1, x2, y2 in point:
    print(arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1])
