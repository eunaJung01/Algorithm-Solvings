def solution(queue1, queue2):
    if sum(queue1) == sum(queue2):
        return 0

    if (sum(queue1) + sum(queue2)) % 2 != 0:
        return -1

    q = queue1 + queue2
    target_sum = sum(q) // 2

    q1_start = 0
    q1_end = len(queue1) - 1
    q1_sum = sum(queue1)
    cnt = 0

    while q1_end < len(q):
        if q1_sum == target_sum:
            return cnt

        if q1_sum < target_sum:
            q1_end += 1
            if q1_end < len(q):
                q1_sum += q[q1_end]
        else:
            q1_sum -= q[q1_start]
            q1_start += 1
        cnt += 1

    return -1
