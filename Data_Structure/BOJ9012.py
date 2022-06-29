# 괄호

import sys


def check_VPS(line):
    stack = []
    for l in line:
        if l == "(":
            stack.append(True)
        elif l == ")":  # ")"
            if len(stack) == 0:
                return False
            else:
                stack.pop(0)
        else:
            continue
    if len(stack) == 0:
        return True
    else:
        return False


T = int(sys.stdin.readline())

for _ in range(T):
    line = sys.stdin.readline()
    if check_VPS(line):
        print("YES")
    else:
        print("NO")
