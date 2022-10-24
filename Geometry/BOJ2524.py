# 희원이의 뉴욕 생활

import sys
import math

input = sys.stdin.readline

Ax, Ay, Bx, By, P, Q, R = map(float, input().split())


def broad_way(x):
    return -(P / Q) * x + (R / Q)


# 1. 브로드웨이 X
result = abs(Ax - Bx) + abs(Ay - By)

# 2. 브로드웨이 O

# 브로드웨이와 맞닿는 부분 후보
A = ((-Ay * (Q / P) + (R / P), Ay), (Ax, broad_way(Ax)))
B = ((-By * (Q / P) + (R / P), By), (Bx, broad_way(Bx)))

for i in range(2):
    for j in range(2):
        nx_A, ny_A = A[i][0], A[i][1]
        nx_B, ny_B = B[j][0], B[j][1]

        result = min(result, abs(Ax - nx_A) + abs(Ay - ny_A) + math.sqrt((nx_A - nx_B) ** 2 + (ny_A - ny_B) ** 2) + abs(
            Bx - nx_B) + abs(
            By - ny_B))

print(result)
