def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2
        if not can_cross(stones, k, mid):
            right = mid - 1
            continue
        answer = mid
        left = mid + 1

    return answer


def can_cross(stones, k, mid):
    skip = 0
    for stone in stones:
        if stone >= mid:
            skip = 0
            continue
        skip += 1
        if skip >= k:
            return False
    return True
