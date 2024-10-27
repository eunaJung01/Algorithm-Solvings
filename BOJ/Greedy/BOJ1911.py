# 흙길 보수하기

import sys
import math

input = sys.stdin.readline

N, L = map(int, input().split())

pool = []
for _ in range(N):
    start, end = map(int, input().split())
    pool.append((start, end))
pool.sort()

result = 0
left = 0  # 남은 널빤지가 어디까지 가는가? (좌표)
pool_idx = 0
has_left = False

while True:
    if pool_idx == N:
        break

    start, end = pool[pool_idx]  # 웅덩이 시작, 끝

    if has_left:  # 앞에서 남은 널빤지가 존재한다면
        if left >= end:  # 웅덩이 끝을 넘어서는 경우
            pool_idx += 1
            continue
        elif left >= start:  # 웅덩이 앞 부분에 겹치는 경우
            start = left + 1
            has_left = False
        else:
            has_left = False

    cnt = math.ceil((end - start) / L)  # 웅덩이를 채우기 위한 널빤지 개수
    result += cnt
    left = start + L * cnt - 1  # 남은 널빤지가 어디까지 가는가? (좌표)
    if left != end:
        has_left = True
    else:
        has_left = False
    pool_idx += 1

print(result)
