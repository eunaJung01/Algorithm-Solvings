import math


def solution(n, stations, w):
    stations.sort()

    holes = [[1]]
    for station in stations:
        holes[-1].append(station - w - 1)
        holes.append([station + w + 1])
    holes[-1].append(n)

    answer = 0
    for start, end in holes:
        if start > end:
            continue

        if start == end:
            answer += 1
            continue
        answer += math.ceil((end - start + 1) / (w * 2 + 1))

    return answer
