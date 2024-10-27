# 약수

import sys

input = sys.stdin.readline

real_num = int(input().strip())
real = list(map(int, input().split()))
real.sort()

print(max(real) * min(real))
