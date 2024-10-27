# 개구리

import sys

S = sys.stdin.readline().strip()

frog_K, frog_P = 0, 0
stack_K, stack_P = 0, 0

for i in range(len(S)):
    if S[i] == "K":
        if stack_P == 0:
            if stack_K >= frog_K:
                frog_K += 1
            stack_K += 1
        else:
            stack_P -= 1

    if S[i] == "P":
        if stack_K == 0:
            if stack_P >= frog_P:
                frog_P += 1
            stack_P += 1
        else:
            stack_K -= 1

print(frog_K + frog_P)
