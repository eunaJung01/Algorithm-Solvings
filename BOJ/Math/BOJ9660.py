# 돌 게임 7

import sys

input = sys.stdin.readline

N = int(input().strip())
if N % 5 == 0 or N % 5 == 2:
    print("CY")
else:
    print("SK")
