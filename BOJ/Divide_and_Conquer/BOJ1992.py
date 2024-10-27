# 쿼드트리

import sys

N = int(sys.stdin.readline().strip())

pic = []
for _ in range(N):
    pic.append(list(sys.stdin.readline().strip()))

dy = (0, 0, 1, 1)
dx = (0, 1, 0, 1)


def check4(r, c, num):
    global result

    count = 0
    temp = []
    for i in range(r, r + num):
        for j in range(c, c + num):
            count = count + 1 if pic[i][j] == '1' else count
            temp.append(pic[i][j])

    # 전부 0인 경우
    if count == 0:
        result.append('0')

    # 전부 1인 경우
    elif count == num * num:
        result.append('1')

    else:
        half = num // 2

        # 분할 가능할 경우
        if half != 1:
            result.append("(")
            for d in range(4):  # 4분할 -> 재귀
                check4(r + half * dy[d], c + half * dx[d], half)
            result.append(")")

        # 최대로 분할했던 것일 경우 -> 종료
        else:
            result.append("(")
            result.append(''.join(temp))
            result.append(")")
            return


result = []
check4(0, 0, N)
print(''.join(result))
