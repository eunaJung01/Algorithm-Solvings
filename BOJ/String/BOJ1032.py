# 명령 프롬프트

import sys

input = sys.stdin.readline
N = int(input().strip())
a = list(input().strip())

a_len = len(a)
for i in range(N - 1):
    b = list(input().strip())
    for j in range(a_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))
