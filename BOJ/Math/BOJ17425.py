# 약수의 합

# DP로 해결 필요!!
import sys

input = sys.stdin.readline

T = int(input().strip())
N = [int(input().strip()) for _ in range(T)]

divResult = [0] * 1000001
for i in range(1, 1000001):
    divResult[i] = 1000000 // i

dp = [[] for _ in range(1000001)]
dp[0].append(1)

for i in range(1, 1000001):
    for j in range(1, divResult[i]):
        dp[i].append(i)
        dp[j].append(j)
        set1 = set(dp[i])
        set2 = set(dp[j])

        dp[i * j] = list(set1.union(set2))
        print(dp[i*j])

print(dp)
