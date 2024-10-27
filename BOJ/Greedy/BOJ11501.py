# 주식

import sys

input = sys.stdin.readline

T = int(input().strip())

result = []
for _ in range(T):
    N = int(sys.stdin.readline())
    stocks = list(map(int, input().split()))
    max_stock, profit = 0, 0
    for i in range(N - 1, -1, -1):
        if stocks[i] < max_stock:
            profit += max_stock - stocks[i]
        else:
            max_stock = stocks[i]
    result.append(profit)

for r in result:
    print(r)
