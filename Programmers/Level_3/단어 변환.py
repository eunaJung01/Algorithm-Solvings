from collections import deque

INF = int(1e10)


def able_to_go(word, next_word):
    wrong_cnt = 0

    for i in range(len(word)):
        if word[i] == next_word[i]:
            continue

        if wrong_cnt == 1:
            return False
        wrong_cnt += 1

    return True


def solution(begin, target, words):
    if target not in words:
        return 0

    visit_cnt = [INF] * len(words)
    q = deque([(begin, 0)])

    while q:
        word, cnt = q.popleft()

        for i in range(len(words)):
            if visit_cnt[i] <= cnt:
                continue

            t = words[i]
            if able_to_go(word, t):
                visit_cnt[i] = cnt + 1
                if t != target:
                    q.append((t, cnt + 1))

    return visit_cnt[words.index(target)]
