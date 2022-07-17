# 회의실 배정

import sys

N = int(sys.stdin.readline().strip())

meeting = []
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meeting.append((end, start))
meeting.sort()  # 회의가 가장 먼저 끝나는 순으로 정렬


result = 1
lastEnd = meeting[0][0]
for end, start in meeting[1:]:
    if lastEnd > start:
        continue
    lastEnd = end
    result += 1

print(result)
