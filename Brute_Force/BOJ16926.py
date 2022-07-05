# 배열 돌리기 1

# 시간 초과
# import copy
# import sys
#
# N, M, R = map(int, sys.stdin.readline().split())  # N x M 배열 / R번 회전
#
# A = []
# for _ in range(N):
#     A.append(list(map(int, sys.stdin.readline().split())))
#
# r = []  # 각 구간 별 회전 수
# for i in range(min(N, M) // 2):
#     r_num = 2 * (M - 2 * i) + 2 * (N - 2 * (i + 1))
#     r.append(R % r_num)
#
#
# def rotate(num, r):
#     for i in range(r):
#         temp = copy.deepcopy(A)  # temp -> A
#         point = [(num, num), (N - num - 1, M - num - 1), (N - num - 1, num),
#                  (num, M - num - 1)]
#
#         for y in range(N - 2 * num - 1):
#             A[point[0][0] + y + 1][point[0][1]] = temp[point[0][0] + y][point[0][1]]
#             A[point[1][0] - y - 1][point[1][1]] = temp[point[1][0] - y][point[1][1]]
#
#         for x in range(M - 2 * num - 1):
#             A[point[2][0]][point[2][1] + x + 1] = temp[point[2][0]][point[2][1] + x]
#             A[point[3][0]][point[3][1] - x - 1] = temp[point[3][0]][point[3][1] - x]
#
#
# for i in range(min(N, M) // 2):
#     rotate(i, r[i])  # 구간 번호, 각 구간별 회전 수
#
# for row in A:
#     for r in row:
#         print(r, end=' ')
#     print()


import sys

N, M, R = map(int, sys.stdin.readline().split())  # N x M 배열 / R번 회전

A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

for _ in range(R):
    for i in range(min(N, M) // 2):
        y, x = i, i
        a = A[y][x]

        # 왼쪽
        for j in range(i + 1, N - i):
            y = j
            temp = A[y][x]
            A[y][x] = a
            a = temp

        # 아래
        for j in range(i + 1, M - i):
            x = j
            temp = A[y][x]
            A[y][x] = a
            a = temp

        # 오른쪽
        for j in range(i + 1, N - i):
            y = N - j - 1
            temp = A[y][x]
            A[y][x] = a
            a = temp

        # 위
        for j in range(i + 1, M - i):
            x = M - j - 1
            temp = A[y][x]
            A[y][x] = a
            a = temp

for row in A:
    for r in row:
        print(r, end=' ')
    print()
