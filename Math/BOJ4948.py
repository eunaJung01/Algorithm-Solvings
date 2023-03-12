# 베르트랑 공준

import sys

input = sys.stdin.readline

N = 123456 * 2 + 1
prime = [False, False] + [True] * (2 * N - 1)
for i in range(2, int(pow(2 * N, 0.5) + 1)):
    if prime[i]:
        for j in range(i * i, 2 * N + 1, i):
            prime[j] = False

while True:
    num = int(input().strip())
    if num == 0:
        break

    cnt = 0
    for i in range(num + 1, 2 * num + 1):
        if prime[i]:
            cnt += 1
    print(cnt)
