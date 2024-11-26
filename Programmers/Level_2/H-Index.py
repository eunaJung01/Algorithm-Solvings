def solution(citations):
    citations.sort()

    answer = len(citations)
    for c in citations:
        if c >= answer:
            break
        answer -= 1
    return answer
