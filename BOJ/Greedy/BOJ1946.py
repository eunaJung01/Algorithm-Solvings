# 신입 사원

import sys

input = sys.stdin.readline

T = int(input().strip())
results = []

for _ in range(T):
    N = int(input().strip())

    score = []
    for _ in range(N):
        score.append(list(map(int, input().split())))

    score.sort()  # 서류 기준 오름차순 정렬
    result = 1
    interview = score[0][1]
    for i in range(1, N):
        if score[i][1] < interview:
            result += 1
            interview = score[i][1]
    results.append(result)

for result in results:
    print(result)
