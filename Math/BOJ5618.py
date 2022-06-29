# 공약수

import sys
from math import gcd

n = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))

# 1. 최대 공약수 구하기
# if n == 2:
#     max_gcd = gcd(numList[0], numList[1])
# else:
#     max_gcd = gcd(numList[0], numList[1], numList[2])
# -> 런타임 에러 발생
max_gcd = gcd(numList[0], gcd(numList[1], numList[-1]))

# 2. 최대 공약수의 약수들 출력
for i in range(1, max_gcd // 2 + 1):
    if max_gcd % i == 0:
        print(i)
print(max_gcd)
