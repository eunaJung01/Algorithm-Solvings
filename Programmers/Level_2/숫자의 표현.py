def solution(n):
    nums = list(range(1, n + 1))

    left = 0
    right = 1
    answer = 0

    while right <= n + 1:
        range_sum = sum(nums[left:right + 1])

        if range_sum == n:
            answer += 1
            left += 1
            continue

        if range_sum > n:
            left += 1
            continue
        right += 1

    return answer
