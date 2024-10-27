# 집합 숫자 표기법

import sys

input = sys.stdin.readline

T = int(input().strip())
case = []
for _ in range(T):
    case.append((input().strip() for _ in range(2)))

result = []
dp = ["{}", "{{}}", "{{},{{}}}"]
for i in range(3, 16):
    d = "{" + dp[i - 1][1:-1] + "," + dp[i - 1] + "}"
    dp.append(d)

for x1, x2 in case:
    x1 = dp.index(x1)
    x2 = dp.index(x2)
    result.append(dp[x1 + x2])

for r in result:
    print(r)
