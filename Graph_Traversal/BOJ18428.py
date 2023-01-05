# 감시 피하기

# 틀렸습니다
# import sys
#
# input = sys.stdin.readline
#
# N = int(input().strip())
#
# m = []  # X : 빈 공간 / S : 학생 / T : 선생 / O : 장애물 (3개 설치 가능)
# student = []
# result = "NO"
#
# for i in range(N):
#     line = list(map(str, input().split()))
#     for j in range(N):
#         if line[j] == "S":
#             student.append((i, j))
#     m.append(line)
#
# pos = []  # 장애물을 놓을 수 있는 위치 후보
#
# status = False
# for sy, sx in student:
#     if status:
#         break
#     for i in range(N):
#         if ((i == sy - 1 or i == sy + 1) and m[i][sx] == "T") or ((i == sx - 1 or i == sx + 1) and m[sy][i] == "T"):
#             status = True
#             break
#         if m[sy][i] == "X":
#             pos.append((sy, i))
#         if m[i][sx] == "X":
#             pos.append((i, sx))
#
#
# def func(cnt):
#     global m, pos_status, status
#
#     if status:
#         return
#
#     if cnt == 3:
#         for sy, sx in student:
#             for i in range(sy, -1, -1):  # 상
#                 if m[i][sx] == "O":
#                     break
#                 if m[i][sx] == "T":
#                     return
#             for i in range(sy + 1, N):  # 하
#                 if m[i][sx] == "O":
#                     break
#                 if m[i][sx] == "T":
#                     return
#             for i in range(sx, -1, -1):  # 좌
#                 if m[sy][i] == "O":
#                     break
#                 if m[sy][i] == "T":
#                     return
#             for i in range(sx + 1, N):  # 우
#                 if m[sy][i] == "O":
#                     break
#                 if m[sy][i] == "T":
#                     return
#
#         status = True
#         return
#
#     for i in range(len(pos)):
#         if not pos_status[i]:
#             y = pos[i][0]
#             x = pos[i][1]
#
#             m[y][x] = "O"
#             pos_status[i] = True
#             func(cnt + 1)
#             pos_status[i] = False
#             m[y][x] = "X"
#
#
# if not status:
#     pos_status = [False for _ in range(len(pos))]
#     func(0)
#     if status:
#         result = "YES"
#
# print(result)

# ---

import sys

input = sys.stdin.readline

N = int(input().strip())

data, teacher = [], []
result = "NO"

for i in range(N):
    data.append(list(map(str, input().split())))
    for j in range(N):
        if data[i][j] == "T":
            teacher.append((i, j))

# 상하좌우
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def hasAvoidedTeacher():
    global data, teacher

    for y, x in teacher:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            while 0 <= ny < N and 0 <= nx < N:
                if data[ny][nx] == "O":
                    break
                elif data[ny][nx] == "S":
                    return False
                ny += dy[i]
                nx += dx[i]
    return True


def DFS(cnt):
    global data, result

    if cnt > 3:
        return

    if cnt == 3:
        if hasAvoidedTeacher():
            result = "YES"
            return
        else:
            result = "NO"

    for i in range(N):
        for j in range(N):
            if data[i][j] == "X":
                data[i][j] = "O"
                DFS(cnt + 1)
                if result == "YES":
                    return
                data[i][j] = "X"


DFS(0)
print(result)
