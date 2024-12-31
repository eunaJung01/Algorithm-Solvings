from collections import deque


def solution(prices):
    temp = deque()
    for i, prices, in enumerate(prices):
        temp.append((prices, i))
    prices = temp

    n = len(prices)
    answer = [0 for _ in range(n)]
    stack = [prices.popleft()]

    while prices:
        while stack and stack[-1][0] > prices[0][0]:
            _, idx = stack.pop()
            answer[idx] = prices[0][1] - idx
        stack.append(prices.popleft())

    while stack:
        _, idx = stack.pop()
        answer[idx] = n - idx - 1

    return answer
