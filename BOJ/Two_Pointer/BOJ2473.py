# 세 용액

import sys

input = sys.stdin.readline

N = int(input().strip())
solutions = list(map(int, input().split()))
solutions.sort()


def solve():
    global s, ans_s, ans_p

    for p1 in range(N - 2):
        p2, p3 = p1 + 1, N - 1

        while p2 < p3:
            s = solutions[p1] + solutions[p2] + solutions[p3]
            if s == 0:
                ans_p = [p1, p2, p3]
                return
            if abs(s) < ans_s:
                ans_s = abs(s)
                ans_p = [p1, p2, p3]

            if s < 0:
                p2 += 1
            elif s > 0:
                p3 -= 1


s, ans_s, ans_p = 0, int(1e10), []
solve()
for p in ans_p:
    print(solutions[p], end=" ")
