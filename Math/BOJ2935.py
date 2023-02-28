# 소음

import sys

input = sys.stdin.readline

a = int(input().strip())
operation = input().strip()
b = int(input().strip())

if operation == '*':
    print(a * b)
else:
    print(a + b)
