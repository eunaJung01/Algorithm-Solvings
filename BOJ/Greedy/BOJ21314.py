# 민겸 수

import sys

line = list(sys.stdin.readline().strip())

m = ''  # 최대 : 최소한의 파싱
n = ''  # 최소 : 최대한의 파싱

count = 0  # M이 나온 개수
for l in line:
    if l == 'M':
        count += 1

    elif l == 'K':
        if count == 0:
            m += '5'
            n += '5'
        else:
            m += str(5 * (10 ** count))
            n += str(10 ** (count - 1)) + '5'
        count = 0

if count != 0:
    m += '1' * count
    n += str(10 ** (count - 1))

print(m)
print(n)

"""
반례
MMM
111
100
"""
