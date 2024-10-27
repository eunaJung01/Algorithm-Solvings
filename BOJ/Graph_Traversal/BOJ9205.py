# 맥주 마시면서 걸어가기

import sys
from collections import deque

input = sys.stdin.readline

t = int(input().strip())
road_limit = 50 * 20


def BFS():
    q = deque()
    q.append((home_y, home_x))
    visitedStores = [False for _ in range(n)]

    while q:
        y, x = q.popleft()
        if abs(y - festival_y) + abs(x - festival_x) <= road_limit:
            return "happy"
        for i in range(n):
            store_y, store_x = map(int, stores[i])
            if not visitedStores[i] and abs(y - store_y) + abs(x - store_x) <= road_limit:
                visitedStores[i] = True
                q.append((store_y, store_x))
    return "sad"


for _ in range(t):
    n = int(input().strip())
    home_y, home_x = map(int, input().split())
    stores = [list(map(int, input().split())) for _ in range(n)]
    festival_y, festival_x = map(int, input().split())
    print(BFS())
