from collections import deque

INF = int(1e9)


def solution(n, roads, sources, destination):
    paths = [[] for _ in range(n + 1)]
    for a, b in roads:
        paths[a].append(b)
        paths[b].append(a)

    answers = [-1 for _ in range(n + 1)]
    answers[destination] = 0

    q = deque()
    q.append(destination)

    while q:
        s = q.popleft()
        cnt = answers[s] + 1

        for d in paths[s]:
            if answers[d] != -1:
                continue
            answers[d] = cnt
            q.append(d)

    answer = []
    for i in sources:
        answer.append(answers[i])
    return answer


print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))
