# 빙산

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ices = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS_MTE(visited, start_y, start_x):
    visited[start_y][start_x] = True
    q = deque()
    q.append((start_y, start_x))
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and ices[ny][nx] > 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))


def findMTEs():
    mte, ice_num = 0, 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if ices[y][x] > 0:
                ice_num += 1
                if not visited[y][x]:
                    BFS_MTE(visited, y, x)
                    mte += 1
    return mte, ice_num


def melt():
    new_ices = [[0 for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            ice = ices[y][x]
            if ice > 0:
                ocean_count = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < M and ices[ny][nx] == 0:
                        ocean_count += 1
                if ice - ocean_count > 0:  # 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다!!!!!!!!
                    new_ices[y][x] = ice - ocean_count
    return new_ices


year = 0
while True:
    # TODO: 빙산 뭉탱이 개수 세기
    mte, ice_num = findMTEs()

    # TODO: 두 뭉탱이 이상으로 분리된 경우 종료
    if mte >= 2:
        break
    # TODO: 빙산이 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않을 경우 종료
    if mte == 0 and ice_num == 0:
        year = 0
        break

    # TODO: 빙산 녹음
    ices = melt()
    year += 1

print(year)

# ---

# 호수는 제외할 경우...

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# ices = [list(map(int, input().split())) for _ in range(N)]
#
# dy = (-1, 1, 0, 0)
# dx = (0, 0, -1, 1)
#
#
# def BFS_MTE(visited, start_y, start_x):
#     visited[start_y][start_x] = True
#     q = deque()
#     q.append((start_y, start_x))
#     while q:
#         y, x = q.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < N and 0 <= nx < M and ices[ny][nx] > 0 and not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 q.append((ny, nx))
#
#
# def findMTEs():
#     mte, ice_num = 0, 0
#     visited = [[False for _ in range(M)] for _ in range(N)]
#     for y in range(N):
#         for x in range(M):
#             if ices[y][x] > 0:
#                 ice_num += 1
#                 if not visited[y][x]:
#                     BFS_MTE(visited, y, x)
#                     mte += 1
#     return mte, ice_num
#
#
# def BFS_oceans(visited, start_y, start_x, oceans):
#     visited[start_y][start_x] = True
#     q = deque()
#     q.append((start_y, start_x))
#     temp = [(start_y, start_x)]
#     isOcean = False
#     while q:
#         y, x = q.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < N and 0 <= nx < M and ices[ny][nx] == 0 and not visited[ny][nx]:
#                 visited[ny][nx] = True
#                 temp.append((ny, nx))
#                 if (ny == 0 or ny == N - 1) or (nx == 0 or nx == M - 1):
#                     isOcean = True
#     if isOcean:
#         for y, x in temp:
#             oceans[y][x] = True
#
#
# def findOceans():
#     visited = [[False for _ in range(M)] for _ in range(N)]
#     oceans = [[False for _ in range(M)] for _ in range(N)]
#     for y in range(N):
#         for x in range(M):
#             if ices[y][x] == 0 and not visited[y][x]:
#                 BFS_oceans(visited, y, x, oceans)
#     return oceans
#
#
# def melt(oceans):
#     new_ices = [[0 for _ in range(M)] for _ in range(N)]
#     for y in range(N):
#         for x in range(M):
#             ice = ices[y][x]
#             if ice > 0:
#                 ocean_count = 0
#                 for i in range(4):
#                     ny = y + dy[i]
#                     nx = x + dx[i]
#                     if 0 <= ny < N and 0 <= nx < M and oceans[ny][nx]:
#                         ocean_count += 1
#                 if ice - ocean_count > 0:
#                     new_ices[y][x] = ice - ocean_count
#     return new_ices
#
#
# year = 0
# while True:
#     # TODO: 빙산 뭉탱이 개수 세기
#     mte, ice_num = findMTEs()
#     # TODO: 두 뭉탱이 이상으로 분리된 경우 종료
#     if mte >= 2:
#         break
#     else:
#         # TODO: 빙산이 전부 녹은 경우 종료
#         if ice_num == 0:
#             year = 0
#             break
#         # TODO: 바다인 부분 녹음
#         ices = melt(findOceans())
#         year += 1
#
# print(year)
