# 주유소

import sys

N = int(sys.stdin.readline().strip())
d = list(map(int, sys.stdin.readline().split()))  # 도로의 길이
money = list(map(int, sys.stdin.readline().split()))[:-1]  # 주유소의 리터당 가격

result = 0
minimum = money[0]
for i in range(N - 1):
    if money[i] < minimum:
        minimum = money[i]
    result += minimum * d[i]

print(result)
