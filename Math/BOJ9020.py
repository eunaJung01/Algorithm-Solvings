# 곮드바흐의 추축

import sys

input = sys.stdin.readline

N = 10000
prime = [True] * (N + 1)
prime[0], prime[1] = False, False
for i in range(2, int(pow(N, 0.5) + 1)):
    if prime[i]:
        for j in range(i * i, N + 1, i):
            prime[j] = False

T = int(input().strip())
for _ in range(T):
    num = int(input().strip())
    first, second = 0, num
    for i in range(1, num // 2 + 1):
        if prime[i] and prime[num - i]:
            if abs(first - second) > abs(i - (num - i)):
                first, second = i, num - i
    print(str(first) + " " + str(second))
