answer = set()


def solution(user_id, banned_id):
    visited = [False] * len(user_id)
    dfs(user_id, banned_id, visited, 0, [])
    return len(answer)


def dfs(user_id, banned_id, visited, n, lst):
    if n == len(banned_id):
        answer.add(tuple(sorted(lst)))
        return

    banned = banned_id[n]

    for i in range(len(user_id)):
        if visited[i]:
            continue

        user = user_id[i]
        if len(user) != len(banned):
            continue

        if not is_banned_user(user, banned):
            continue

        visited[i] = True
        dfs(user_id, banned_id, visited, n + 1, lst + [i])
        visited[i] = False


def is_banned_user(user, banned):
    for i, b in enumerate(banned):
        if b == "*":
            continue
        if user[i] != b:
            return False
    return True
