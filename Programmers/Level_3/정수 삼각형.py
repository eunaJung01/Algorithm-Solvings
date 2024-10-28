def solution(triangle):
    height = len(triangle)

    dp = [[0 for _ in range(height)] for _ in range(height)]
    dp[0][0] = triangle[0][0]

    for row in range(1, height):
        for col in range(0, row + 1):
            if col == 0:
                dp[row][col] = dp[row - 1][col] + triangle[row][col]
            elif row == col:
                dp[row][col] = dp[row - 1][col - 1] + triangle[row][col]
            else:
                dp[row][col] = (max(dp[row - 1][col - 1], dp[row - 1][col]) +
                                triangle[row][col])

    return max(dp[height - 1])
