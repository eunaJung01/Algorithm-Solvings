# 1

import sys

input = sys.stdin.readline

n_list = []
while True:
    n = input().strip()
    if not n:
        break
    n_list.append(int(n))

result = []
for n in n_list:
    one = ['1' for _ in range(len(str(n)) + 1)]
    if int(''.join(one[1:])) == n:
        result.append(len(one) - 1)
        break

    while True:
        if int(''.join(one)) % n == 0:
            break
        else:
            one.append('1')

    result.append(len(one))

for r in result:
    print(r)
