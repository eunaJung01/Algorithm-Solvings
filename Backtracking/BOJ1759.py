# 암호 만들기

import sys

input = sys.stdin.readline

L, C = map(int, input().split())
alpha = list(map(str, input().split()))
alpha.sort()

# 암호 : 서로 다른 L개의 알파벳 소문자들로 구성
# 1. 최소 한 개의 모음 (a, e, i, o, u)
# 2. 최소 두 개의 자음

consonants = ['a', 'e', 'i', 'o', 'u']  # 자음

arr = []
status = [False for _ in range(C)]


def func(cnt, idx, consonantNum):
    global status

    if cnt == L:
        if 0 < consonantNum <= L - 2:
            for a in arr:
                print(a, end='')
            print()
        return

    for i in range(C):
        if not status[i] and i >= idx:
            status[i] = True

            a = alpha[i]
            arr.append(a)

            if a in consonants:
                func(cnt + 1, i, consonantNum + 1)
            else:
                func(cnt + 1, i, consonantNum)

            arr.pop()
            status[i] = False


func(0, 0, 0)
