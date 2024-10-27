# ZOAC

import sys

str = list(sys.stdin.readline().strip())
check = [False for _ in range(len(str))]  # 출력 여부


def find(l, r):
    idx = -1
    min_str = 'zz'

    for i in range(l, r + 1, 1):
        # 범위 내에서 가장 작은 문자 찾기
        if not check[i] and min_str > str[i]:
            min_str = str[i]
            idx = i

    if min_str == 'zz':
        return

    check[idx] = True

    temp = []
    for i in range(len(str)):
        if check[i]:
            temp.append(str[i])
    print(''.join(temp))

    find(idx + 1, r)
    find(l, idx - 1)


find(0, len(str) - 1)
