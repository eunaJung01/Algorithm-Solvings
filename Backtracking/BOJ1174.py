# 줄어드는 수

import sys

N = int(sys.stdin.readline().strip())
m = 9876543210


def func(N):
    q = [i for i in range(10)]

    if N <= 10:
        return N - 1

    idx = 1
    while True:
        for i in range(10):
            if q[idx] % 10 > i:
                temp = list(str(q[idx]))
                temp.append(str(i))
                q.append(int("".join(temp)))

            if len(q) == N:
                return q[-1]
            if q[-1] >= m:
                return -1
        idx += 1


print(func(N))
