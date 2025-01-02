import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while len(scoville) > 1:
        least = heapq.heappop(scoville)
        if least >= K:
            break

        post_least = heapq.heappop(scoville)
        new_s = least + post_least * 2
        heapq.heappush(scoville, new_s)
        answer += 1

    if scoville[0] < K:
        return -1
    return answer
