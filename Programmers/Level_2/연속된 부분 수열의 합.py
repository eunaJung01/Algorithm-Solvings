def solution(sequence, k):
    n = len(sequence)
    total = sequence[0]
    left = 0
    right = 0

    answer = [0, n - 1]
    while left < n and right < n:
        if total == k:
            if answer[1] - answer[0] > right - left:
                answer = [left, right]
            if right == n - 1:
                break
            right += 1
            total += sequence[right]
            continue

        if total < k:
            if right == n - 1:
                break
            right += 1
            total += sequence[right]
            continue

        if left < right:
            total -= sequence[left]
            left += 1
            continue

        if left == right == n - 1:
            break
        left += 1
        right += 1
        total = sequence[left]

    return answer
