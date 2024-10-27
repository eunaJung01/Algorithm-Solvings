# 랜선 자르기

import sys

K, N = map(int, sys.stdin.readline().split())

cable = []
for _ in range(K):
    cable.append(int(sys.stdin.readline().strip()))

left = 1
right = max(cable)
mid = (left + right) // 2

while left <= right:
    mid = (left + right) // 2

    count = 0
    for c in cable:
        count += c // mid

    if count >= N:
        left = mid + 1
    else:
        right = mid - 1

print(right)  # 최대 랜선 길이
