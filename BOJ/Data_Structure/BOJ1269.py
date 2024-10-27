# 대칭 차집합

import sys

input = sys.stdin.readline

A_num, B_num = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A - B) + len(B - A))
