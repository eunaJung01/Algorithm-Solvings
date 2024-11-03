INF = 1e10


def solution(routes):
    routes.sort(key=lambda x: x[1])

    answer = 0
    camera_pos = -INF

    for start, end in routes:
        if start > camera_pos:
            answer += 1
            camera_pos = end

    return answer
