# 연산자 끼워넣기

import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())  # +, -, *, /

result = [-1e11, 1e11]  # max, min


def func(cnt, sum, plus, minus, mul, div):
    if cnt == N:
        result[0] = max(result[0], sum)
        result[1] = min(result[1], sum)
        return

    if plus > 0:
        func(cnt + 1, sum + A[cnt], plus - 1, minus, mul, div)
    if minus > 0:
        func(cnt + 1, sum - A[cnt], plus, minus - 1, mul, div)
    if mul > 0:
        func(cnt + 1, sum * A[cnt], plus, minus, mul - 1, div)
    if div > 0:
        func(cnt + 1, int(sum / A[cnt]), plus, minus, mul, div - 1)


func(1, A[0], plus, minus, mul, div)
for r in result:
    print(r)
