# 팩토링얼 0의 개수

import sys

N = int(sys.stdin.readline())

result = N // 5 + N // 25 + N // 125
print(result)
