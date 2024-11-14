from collections import defaultdict, deque


def solution(k, tangerine):
    t_cnt = defaultdict(int)
    for t in tangerine:
        t_cnt[t] += 1

    sorted_t_cnt = deque(sorted(t_cnt.items(), key=lambda x: x[1]))
    pop_cnt = len(tangerine) - k

    while True:
        if pop_cnt < sorted_t_cnt[0][1]:
            break
        pop_cnt -= sorted_t_cnt[0][1]
        sorted_t_cnt.popleft()

    return len(sorted_t_cnt)
