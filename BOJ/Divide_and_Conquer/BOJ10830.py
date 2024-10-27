# 행렬 제곱

import sys

input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


def matrix_mul(a, b):
    mul_result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                mul_result[i][j] += a[i][k] * b[k][j]
            mul_result[i][j] %= 1000
    return mul_result


def cal(a, b):
    if b == 1:
        return a
    elif b == 2:
        return matrix_mul(a, a)
    else:
        half_mul = cal(a, b // 2)
        if b % 2 == 0:
            return matrix_mul(half_mul, half_mul)
        else:
            return matrix_mul(matrix_mul(half_mul, half_mul), A)


result = cal(A, B)
for i in range(N):
    for j in range(N):
        print(result[i][j] % 1000, end=' ')
    print()
