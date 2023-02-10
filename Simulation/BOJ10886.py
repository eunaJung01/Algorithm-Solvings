# 0 = not cute / 1 = cute

import sys

input = sys.stdin.readline

N = int(input().strip())
isCute, notCute = 0, 0

for _ in range(N):
    cute = int(input().strip())
    if cute == 0:
        notCute += 1
    else:
        isCute += 1

if isCute >= notCute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
