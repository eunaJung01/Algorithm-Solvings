# 장난감 조립

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input().strip())  # 완제품의 번호
M = int(input().strip())

nextParts = defaultdict(list)
inDegrees = [0 for _ in range(N + 1)]

for _ in range(M):
    X, Y, K = map(int, input().split())  # X를 만드는데 부품 Y가 K개 필요하다
    nextParts[Y].append((X, K))
    inDegrees[X] += 1

q = deque()
for i in range(1, N + 1):
    if inDegrees[i] == 0:
        q.append(i)

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]  # 부품 × 필요한 부품들의 개수

while q:
    part = q.popleft()

    for nextPart, num in nextParts[part]:
        # part : 기본 부품일 경우
        if dp[part].count(0) == N + 1:
            dp[nextPart][part] += num

        # part : 중간 부품일 경우
        else:
            for i in range(1, N + 1):
                dp[nextPart][i] += dp[part][i] * num

        inDegrees[nextPart] -= 1
        if inDegrees[nextPart] == 0:
            q.append(nextPart)

for part, cnt in enumerate(dp[N]):
    if cnt > 0:
        print(part, cnt)
