import sys
from collections import deque

input = sys.stdin.readline

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def bfs(start_y, start_x, islandId, hasVisited):
    q = deque()
    q.append((start_y, start_x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and _map[ny][nx] and not hasVisited[ny][nx]:
                _map[ny][nx] = islandId
                hasVisited[ny][nx] = True
                islands.append((ny, nx, islandId))
                q.append((ny, nx))


def find_islands():
    hasVisited = [[False for _ in range(m)] for _ in range(n)]
    islandId = 1
    for i in range(n):
        for j in range(m):
            if _map[i][j] and not hasVisited[i][j]:
                hasVisited[i][j] = True
                _map[i][j] = islandId
                islands.append((i, j, islandId))
                bfs(i, j, islandId, hasVisited)
                islandId += 1
    return islandId - 1


def make_bridges(start_y, start_x, islandId):
    q = deque()
    for i in range(4):
        hasVisited = [[False for _ in range(m)] for _ in range(n)]
        lengths = [[0 for _ in range(m)] for _ in range(n)]
        q.append((start_y, start_x))
        hasVisited[start_y][start_x] = True

        while q:
            y, x = q.popleft()
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and not hasVisited[ny][nx]:
                if _map[ny][nx] == 0:
                    lengths[ny][nx] = lengths[y][x] + 1
                    q.append((ny, nx))
                    continue

                if _map[ny][nx] != islandId and lengths[y][x] > 1:
                    bridges.append((lengths[y][x], islandId, _map[ny][nx]))


# union-find
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[a] = b


n, m = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]
islands, bridges = [], []

islandCnt = find_islands()
for y, x, islandId in islands:
    make_bridges(y, x, islandId)
bridges.sort()

# kruskal
parent = [i for i in range(islandCnt + 1)]
result, edgeCnt = 0, 0
for length, a, b in bridges:
    if find(a) != find(b):
        result += length
        edgeCnt += 1
        if edgeCnt == islandCnt - 1:
            break
        union(a, b)

if edgeCnt == islandCnt - 1:
    print(result)
else:
    print(-1)
