answer = 0


def solution(k, dungeons):
    for i in range(len(dungeons)):
        if dungeons[i][0] > k:
            continue
        visited = [False for _ in range(len(dungeons))]
        visited[i] = True
        dfs(k - dungeons[i][1], dungeons, visited, 1)
    return answer


def dfs(tiredness, dungeons, visited, visited_cnt):
    global answer

    for i in range(len(dungeons)):
        if visited[i]:
            continue

        if dungeons[i][0] <= tiredness:
            visited[i] = True
            visited_cnt += 1
            tiredness -= dungeons[i][1]
            dfs(tiredness, dungeons, visited, visited_cnt)
            tiredness += dungeons[i][1]
            visited_cnt -= 1
            visited[i] = False
            continue

    answer = max(answer, visited_cnt)
