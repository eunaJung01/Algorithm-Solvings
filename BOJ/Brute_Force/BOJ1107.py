# 리모컨

import sys


def check(num):
    num = list(str(num))
    for i in num:
        if i in broken:
            return False
    return True


N = int(sys.stdin.readline())  # 이동하려는 채널 번호
M = int(sys.stdin.readline())  # 고장난 버튼의 개수
broken = list(sys.stdin.readline().strip())  # 고장난 버튼 list

result = abs(N - 100)

for i in range(1000001):
    if check(i):  # 버튼으로 이동 가능한지 확인
        result = min(result, len(str(i)) + abs(i - N))

print(result)
