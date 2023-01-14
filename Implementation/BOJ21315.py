# 카드 섞기

import sys

input = sys.stdin.readline

N = int(input().strip())
initial_cards = [i for i in range(1, N + 1)]
result_cards = list(map(int, input().split()))


def get_max_K(N):
    K = 1
    while 2 ** K < N:
        K += 1
    return K - 1


def shuffle_cards(K, cards):
    shuffle, result = cards[N - 2 ** K:], cards[:N - 2 ** K]
    for i in range(2, K + 1):
        result = shuffle[:len(shuffle) - 2 ** (K - i + 1)] + result
        shuffle = shuffle[len(shuffle) - 2 ** (K - i + 1):]
    result = shuffle[::-1] + result
    return result


def getFirstShuffleResult():
    results = []
    for i in range(1, max_K + 1):
        results.append(([i], shuffle_cards(i, initial_cards)))
    return results


def isResult(shuffled_cards):
    for i in range(N):
        if shuffled_cards[i] != result_cards[i]:
            return False
    return True


def getResult():
    for K_list, first_shuffled_cards in first_shuffle_results:
        for i in range(1, max_K + 1):
            if isResult(shuffle_cards(i, first_shuffled_cards)):
                return K_list + [i]


max_K = get_max_K(N)
first_shuffle_results = getFirstShuffleResult()
result = getResult()
for r in result:
    print(r, end=' ')
