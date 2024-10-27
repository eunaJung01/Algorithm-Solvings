# 소수의 연속합

import sys

input = sys.stdin.readline


def getPrimes(N):
    flag = [True for _ in range(N + 1)]
    for i in range(2, N + 1):
        if not flag[i]:
            continue
        n = i * 2
        while n <= N:
            flag[n] = False
            n += i

    primes = []
    for i in range(2, N + 1):
        if flag[i]:
            primes.append(i)
    return primes


N = int(input().strip())
primes = getPrimes(N)

idx, s, cnt = 0, 0, 0
for i in range(len(primes)):
    while idx < len(primes) and s < N:
        s += primes[idx]
        idx += 1
    if s == N:
        cnt += 1
    s -= primes[i]

print(cnt)
