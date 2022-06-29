# 제곱수 찾기

import sys
import math

N, M = map(int, sys.stdin.readline().split())  # N : 행 / M : 열

arr = []
for _ in range(N):
    line = sys.stdin.readline().strip()
    arr.append([str(i) for i in line])

result = 0
hasResult = False
for i in range(N + 1):  # 행 읽기 시작하는 부분
    for j in range(M + 1):  # 열 읽기 시작하는 부분
        for n in range(-N, N):  # 행 등차값
            for m in range(-M, M):  # 열 등차값
                if n == 0 and m == 0:
                    continue
                row = i
                col = j
                num_str = []
                while row >= 0 and row < N and col >= 0 and col < M:
                    num_str.append(arr[row][col])

                    # 제곱수인지 확인
                    num = int(''.join(num_str))
                    num_sqrt = int(math.sqrt(float(num)))
                    if num_sqrt ** 2 == num:
                        result = max(num, result)
                        hasResult = True

                    row += n
                    col += m

if not hasResult:
    print(-1)
else:
    print(result)
