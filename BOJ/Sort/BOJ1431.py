# 시리얼 번호

import sys

input = sys.stdin.readline


def sum_num(s):
    result = 0
    for x in s:
        if x.isdigit():
            result += int(x)
    return result


N = int(input().strip())

serials = [input().strip() for _ in range(N)]
serials.sort(key=lambda s: (len(s), sum_num(s), s))
for serial in serials:
    print(serial)
