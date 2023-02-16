# 강의실 배정

import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())
classes = [list(map(int, input().split())) for _ in range(N)]
classes.sort()

h = []
start, end = classes[0]
heapq.heappush(h, end)

for start, end in classes[1:]:
    if start < h[0]:  # 수업 시작 시간이 현재 수업의 종료 시간보다 빠른 경우
        heapq.heappush(h, end)  # 새 강의실 추가
    else:
        # 현재 수업의 종료 시간을 다음 수업의 종료 시간으로 교체
        heapq.heappop(h)
        heapq.heappush(h, end)

print(len(h))
