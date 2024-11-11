def solution(n, words):
    word_set = set()
    word_set.add(words[0])
    cnt = 1

    for i in range(1, len(words)):
        cnt += 1
        if words[i][0] != words[i - 1][-1]:
            return wrong_person(n, cnt)
        if words[i] in word_set:
            return wrong_person(n, cnt)
        word_set.add(words[i])

    return [0, 0]


def wrong_person(n, cnt):
    first = cnt % n
    if first == 0:
        first = n
        return [first, cnt // n]
    return [first, cnt // n + 1]
