def solution(people, limit):
    people.sort()
    p1 = 0
    p2 = len(people) - 1

    answer = 0
    while p1 <= p2:
        if p1 == p2:
            answer += 1
            break

        if people[p1] + people[p2] <= limit:
            answer += 1
            p1 += 1
            p2 -= 1
            continue

        answer += 1
        p2 -= 1

    return answer
