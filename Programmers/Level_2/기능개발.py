import math


def solution(progresses, speeds):
    n = len(progresses)

    answer = []
    day = math.ceil((100 - progresses[0]) / speeds[0])
    cnt = 1
    work_id = 1

    while work_id < n:
        work = progresses[work_id]
        speed = speeds[work_id]
        left_day = math.ceil((100 - work) / speed)

        if left_day <= day:
            cnt += 1
            work_id += 1
            continue

        answer.append(cnt)
        day = left_day
        cnt = 1
        work_id += 1

    if cnt > 0:
        answer.append(cnt)
    return answer
