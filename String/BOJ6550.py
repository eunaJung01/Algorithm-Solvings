# 부분 문자열

import sys


def func(s, t):
    s_idx = 0
    for t_alpha in t:
        if t_alpha == s[s_idx]:
            s_idx += 1
            if s_idx == len(s):
                return "Yes"
    return "No"


while True:
    line = sys.stdin.readline()
    if not line:
        break
    s, t = line.split()

    print(func(s, t))
