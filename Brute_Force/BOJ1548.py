# 부분 삼각 수열

# 가장 큰 수를 z라고 했을 때 x+y>z 만족 시 삼각 수열

import sys

N = int(sys.stdin.readline().strip())
numList = list(map(int, sys.stdin.readline().split()))

result = 0

if N < 3:  # 숫자의 개수가 3 미만인 경우 -> N 반환
    result = N

else:
    numList.sort()  # 오름차순 정렬

    for i in range(N - 1):
        x = numList[i]
        y = numList[i + 1]

        for j in range(1, N):
            z = numList[-j]

            if x + y > z:
                result = max(result, N - j - i + 1)
                break
            elif y == z:
                break

print(result)
