# 상어 초등학교

import sys

input = sys.stdin.readline

scores = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

N = int(input().strip())
classroom = [[0 for _ in range(N)] for _ in range(N)]

lovers, lovers_dict = [], dict()
for _ in range(N ** 2):
    line = list(map(int, input().split()))
    student, student_lovers = line[0], line[1:]
    lovers.append((student, student_lovers))
    lovers_dict[student] = student_lovers


def conditions():
    available_seats = condition1()
    if len(available_seats) == 1:
        classroom[available_seats[0][0]][available_seats[0][1]] = student
        return

    most_empty_seats = condition2(available_seats)
    if len(most_empty_seats) == 1:
        classroom[most_empty_seats[0][0]][most_empty_seats[0][1]] = student
        return

    condition3(most_empty_seats)


def condition1():
    # TODO: 1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    lovers_cnt, available_seats = 0, []
    for y in range(N):
        for x in range(N):
            if classroom[y][x] == 0:
                cnt = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and classroom[ny][nx] in student_lovers:
                        cnt += 1
                if cnt > lovers_cnt:
                    lovers_cnt = cnt
                    available_seats = [(y, x)]
                elif cnt == lovers_cnt:
                    available_seats.append((y, x))
    return available_seats


def condition2(seats):
    # TODO: 2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    empty_cnt, most_empty_seats = 0, []
    for y, x in seats:
        cnt = 0
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and classroom[ny][nx] == 0:
                cnt += 1
        if cnt > empty_cnt:
            empty_cnt = cnt
            most_empty_seats = [(y, x)]
        elif cnt == empty_cnt:
            most_empty_seats.append((y, x))
    return most_empty_seats


def condition3(seats):
    # TODO: 3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.l
    for y in range(N):
        for x in range(N):
            if (y, x) in seats:
                classroom[y][x] = student
                return


for student, student_lovers in lovers:
    conditions()

result = 0
for y in range(N):
    for x in range(N):
        cnt = 0
        student_lovers = lovers_dict[classroom[y][x]]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and classroom[ny][nx] in student_lovers:
                cnt += 1
        result += scores[cnt]
print(result)
