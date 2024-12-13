from collections import deque

START_TIME = 9 * 60


def solution(n, t, m, timetable):
    times = []
    for time in timetable:
        hour, minute = map(int, time.strip().split(":"))
        times.append(hour * 60 + minute)
    times.sort()
    times = deque(times)

    last_shuttle = START_TIME + (n - 1) * t
    while times and times[-1] > last_shuttle:
        times.pop()

    if len(times) == 0:
        return get_HH_MM(last_shuttle)

    shuttle = START_TIME
    shuttle_cnt = 1
    while times and shuttle_cnt < n:
        people_cnt = 0
        while times and people_cnt < m and times[0] <= shuttle:
            people_cnt += 1
            times.popleft()
        shuttle += t
        shuttle_cnt += 1

    if len(times) == 0:
        return get_HH_MM(last_shuttle)

    if len(times) < m:
        return get_HH_MM(last_shuttle)
    return get_HH_MM(times[m - 1] - 1)


def get_HH_MM(minutes):
    hour = minutes // 60
    minute = minutes % 60
    return (str(hour).rjust(2, '0') +
            ":" +
            str(minute).rjust(2, '0'))
