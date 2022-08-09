# Z

import sys

N, r, c = map(int, sys.stdin.readline().split())  # 2^N x 2^N 2차원 배열 -> (r, c)

square = 2 ** N  # 현재 보는 뭉탱이 크기

d = [(0, 0), (0, 1), (1, 0), (1, 1)]

# 뭉탱이 시작 주소 (start_y, start_x)
start_y = 0
start_x = 0

add = 2 + 2 * (N - 2)  # 2**add : 뭉탱이 숫자 덩어리
result = 0
while N > 1:
    n = square // 2  # 다음 뭉탱이 크기
    for i in range(4):
        # 다음 뭉탱이 시작 주소 (dy, dx)
        dy = start_y + d[i][0] * n
        dx = start_x + d[i][1] * n

        # (r, c)가 뭉탱이 끝값 안에 들어간다면 break
        if dy <= r <= dy + n - 1 and dx <= c <= dx + n - 1:
            start_y = dy
            start_x = dx
            result += 2 ** add * i
            break
    N -= 1
    add -= 2
    square = 2 ** N

for i in range(4):
    dy = start_y + d[i][0]
    dx = start_x + d[i][1]
    if r == dy and c == dx:
        break
    result += 1

print(result)
