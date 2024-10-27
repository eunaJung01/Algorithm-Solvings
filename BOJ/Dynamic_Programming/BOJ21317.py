# 징검다리 건너기

# 마지막 돌 틈 사이에 산삼 -> 마지막 돌은 반드시 밟아야 함

# 작은 점프 : 다음 돌로
# 큰 점프 : 1개 돌 건너뜀
# 매우 큰 점프 : 2개 돌 건너뜀 / 한번만 가능, K만큼의 에너지 소비

import sys

N = int(sys.stdin.readline().strip())

energy = [[0, 0]]
for _ in range(N - 1):
    energy.append(list(map(int, sys.stdin.readline().split())))  # [작은 점프, 큰 점프]

K = int(sys.stdin.readline().strip())  # 매우 큰 점프

result = 99999

if N == 1 or N == 2:
    result = energy[N - 1][0]
else:
    dp = [[99999 for _ in range(N + 1)] for _ in range(N - 2)]

    for i in range(0, N - 2):
        dp[i][2] = energy[1][0]
        dp[i][3] = min(dp[i][2] + energy[2][0], energy[1][1])

        for j in range(1, N + 1):
            dp[i][j] = min(dp[i][j - 1] + energy[j - 1][0], dp[i][j - 2] + energy[j - 2][1], dp[i][j])

            if i == j:
                if i == 1:
                    dp[1][4] = K
                else:
                    dp[i][j + 3] = dp[i][j] + K

    for i in range(0, N - 2):
        result = min(result, dp[i][-1])

print(result)
