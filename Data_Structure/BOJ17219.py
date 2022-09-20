# 비밀번호 찾기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

memo = {}
for _ in range(N):
    site, password = map(str, input().split())
    memo[site] = password

site = [input().strip() for _ in range(M)]

for s in site:
    print(memo[s])
