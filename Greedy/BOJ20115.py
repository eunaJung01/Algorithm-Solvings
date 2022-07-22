# 에너지 드링크

import sys

N = int(sys.stdin.readline().strip())
drink = list(map(int, sys.stdin.readline().split()))
drink.sort(reverse=True)

result = drink[0]
for i in range(1, N):
    result += drink[i] / 2

print(result)
