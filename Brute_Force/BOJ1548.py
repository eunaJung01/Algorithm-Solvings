# 부분 삼각 수열
# 가장 큰 수 k -> k<i+j

import sys

N = int(sys.stdin.readline().strip())
numList = list(map(int, sys.stdin.readline().split()))
numList.sort()  # 오름차순 정렬

result = 0
if len(numList) < 3:  # 숫자의 개수가 3 미만인 경우 -> 그냥 그 개수를 반환
    result = len(numList)
else:
    for i in range(len(numList) - 1):
        x = numList[i]
        y = numList[i + 1]
        for j in range(1, len(numList)):
            z = numList[-j]

            if x + y > z:
                result = max(result, len(numList) - j - i + 1)
            elif y == z:
                break

print(result)
