# 공유기 설치

import sys

input = sys.stdin.readline

N, C = map(int, input().split())
homes = [int(input().strip()) for _ in range(N)]
homes.sort()

left = 1
right = homes[-1]
answer = 0

while left <= right:
    min_distance = (left + right) // 2  # 공유기를 설치할 간격
    cur = homes[0]
    cnt = 1

    for i in range(1, N):
        if homes[i] - cur >= min_distance:
            cnt += 1
            cur = homes[i]

    if cnt >= C:
        answer = min_distance
        left = min_distance + 1  # 공유기를 설치할 간격을 늘림
    else:
        right = min_distance - 1  # 공유기를 설치할 간격을 줄임

print(answer)
