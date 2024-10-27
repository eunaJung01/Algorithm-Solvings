# 숨바꼭질 2

import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
limit = 10 ** 5
INF = int(1e10)


def BFS():
    dp = [[INF, 0] for _ in range(limit + 1)]  # min_time, cnt
    dp[N][0] = 0
    heap = [(0, N)]
    heapq.heapify(heap)
    hasFound = False

    while heap:
        t, cur = heapq.heappop(heap)
        if cur == K:
            hasFound = True
            continue
        if hasFound and t > dp[K][0]:
            continue
        for i in range(3):
            if i == 0:
                next_pos = cur - 1
            elif i == 1:
                next_pos = cur + 1
            else:
                next_pos = cur * 2
            if 0 <= next_pos <= limit:
                if dp[next_pos][0] > dp[cur][0] + 1:
                    dp[next_pos][0] = dp[cur][0] + 1
                    dp[next_pos][1] = 1
                    heapq.heappush(heap, (dp[next_pos][0], next_pos))
                elif dp[next_pos][0] == dp[cur][0] + 1:
                    dp[next_pos][1] += 1
                    heapq.heappush(heap, (dp[next_pos][0], next_pos))
    return dp[K]


if N == K:
    time, cnt = 0, 1
else:
    time, cnt = BFS()
print(time)
print(cnt)
