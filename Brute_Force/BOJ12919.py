# A와 B 2

import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()


def change1(x):  # A 제거
    x = x[:-1]
    return x


def change2(x):  # B 제거 -> 문자열 뒤집기
    x = x[1:][::-1]
    return x


def check(s, t):
    # 두 문자열이 같을 경우
    if s == t:
        return True

    # 'A__B'가 되는 경우는 없음 / 두 문자열의 길이가 같은데 다른 문자열인 경우
    elif (t[0] == 'A' and t[-1] == 'B') or len(s) >= len(t):
        return False

    elif t[0] == 'B' and check(s, change2(t)):
        return True

    elif t[-1] == 'A' and check(s, change1(t)):
        return True

    else:
        return False


status = check(s, t)
if status:
    print(1)
else:
    print(0)
