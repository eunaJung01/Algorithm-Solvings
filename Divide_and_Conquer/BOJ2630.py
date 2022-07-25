# 색종이 만들기

import sys

dy = (0, 1, 0, 1)
dx = (0, 0, 1, 1)


def check(r, c, num):
    global paper
    global white
    global blue

    color = paper[r][c]

    if num == 1:
        if color == 0:
            white += 1
        else:
            blue += 1
        return

    status = True
    for i in range(r, r + num):
        for j in range(c, c + num):
            if color != paper[i][j]:
                status = False

    if status:
        if color == 0:
            white += 1
        else:
            blue += 1
        return
    else:
        for d in range(4):
            check(r + dy[d] * (num // 2), c + dx[d] * (num // 2), num // 2)


N = int(sys.stdin.readline().strip())

paper = []
for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().split())))

white = 0
blue = 0

check(0, 0, N)
print(white)
print(blue)
