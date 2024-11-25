def solution(n, times):
    times.sort()
    min_time = times[0]
    max_time = times[0] * n

    while max_time != min_time + 1:
        mid_time = (max_time + min_time) // 2
        solved_people = calc(mid_time, times)
        if solved_people >= n:
            max_time = mid_time
        else:
            min_time = mid_time
    return max_time


def calc(deadline, times):
    solved_people = 0
    for t in times:
        solved_people += deadline // t
    return solved_people
