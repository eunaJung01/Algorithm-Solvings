from copy import deepcopy

answer = []


def solution(tickets):
    n = len(tickets)

    for i in range(n):
        if tickets[i][0] == "ICN":
            visited = [False] * n
            dfs(n, tickets, visited, i, ["ICN"])

    if len(answer) == 1:
        return answer[0]
    answer.sort()
    return answer[0]


def dfs(n, tickets, visited, pos, route):
    visited[pos] = True
    b = tickets[pos][1]
    route.append(b)

    if len(route) == n + 1:
        answer.append(deepcopy(route))

    for i in range(n):
        if visited[i]:
            continue
        if tickets[i][0] == b:
            dfs(n, tickets, visited, i, route)

    route.pop()
    visited[pos] = False
