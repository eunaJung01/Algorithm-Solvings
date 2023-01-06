# 미로만들기

import sys
import heapq

input = sys.stdin.readline

n = int(input().strip())
rooms = [input().strip() for _ in range(n)]

INF = 2147000000
dp = [[INF for _ in range(n)] for _ in range(n)]

dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)


def BFS():
    global rooms

    heap = []
    heapq.heappush(heap, (0, 0, 0))
    dp[0][0] = 0

    while heap:
        cnt, y, x = heapq.heappop(heap)
        if y == n - 1 and x == n - 1:
            return cnt

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                # 검은 방
                if rooms[ny][nx] == "0" and dp[ny][nx] > dp[y][x] + 1:
                    dp[ny][nx] = dp[y][x] + 1
                    heapq.heappush(heap, (dp[ny][nx], ny, nx))
                # 흰 방
                elif rooms[ny][nx] == "1" and dp[ny][nx] > dp[y][x]:
                    dp[ny][nx] = dp[y][x]
                    heapq.heappush(heap, (dp[ny][nx], ny, nx))


print(BFS())
