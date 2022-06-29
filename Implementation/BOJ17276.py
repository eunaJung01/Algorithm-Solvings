# 배열 돌리기

import copy
import sys


def rotate(n, d, arr):
    global result

    # arr_rotated = arr[:]  # 얕은 복사
    arr_rotated = copy.deepcopy(arr)  # 깊은 복사

    half = int(n / 2)

    # 1. X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
    for i in range(n):
        arr_rotated[i][half] = arr[i][i]

    # 2. X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다.
    for i in range(n):
        arr_rotated[i][n - i - 1] = arr[i][half]

    # 3. X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
    for i in range(n):
        arr_rotated[half][n - i - 1] = arr[i][n - i - 1]

    # 4. X의 가운데 행을 X의 주 대각선으로 옮긴다.
    for i in range(n):
        arr_rotated[i][i] = arr[half][i]

    d -= 45
    if d == 0:
        result.append(arr_rotated)
        return
    else:
        rotate(n, d, arr_rotated)


T = int(sys.stdin.readline().strip())  # T : 테스트 케이스의 수

result = []
for _ in range(T):
    n, d = map(int, sys.stdin.readline().split())  # n : 배열의 크기 / d : 각도
    arr = []  # 크기가 n x n인 2차원 정수 배열
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    d %= 360  # d가 음수일 경우 & 양수일 경우를 나누지 않아도 됨!

    if d == 0:
        result.append(arr)
    else:
        rotate(n, d, arr)

for arr in result:
    for row in arr:
        for i in row:
            print(i, end=' ')
        print()
