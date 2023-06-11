# 피보나치 수 6

import sys

input = sys.stdin.readline


# 행렬 제곱 (by. 분할 정복)
def power(a, n):
    if n == 1:
        return a
    if n % 2 == 1:  # n이 홀수일 경우
        return mul(power(a, n - 1), a)
    else:  # n이 짝수일 경우
        return power(mul(a, a), n // 2)


# 행렬 곱셈
def mul(a, b):
    ans = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            ans[i][j] = sum % 1000000007
    return ans


n = int(input().strip())
if n < 3:
    print(1)
else:
    f = [[1, 1], [1, 0]]
    start = [[1], [1]]
    print(mul(power(f, n - 2), start)[0][0])
