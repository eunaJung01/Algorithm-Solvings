# 거짓말

import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # N : 사람의 수 / M : 파티의 수
truth = set(list(map(int, input().split()))[1:])
parties = [list(map(int, input().split()))[1:] for _ in range(M)]

truth_party = [0] * M

for _ in range(M):
    for idx, party in enumerate(parties):
        if truth.intersection(set(party)):  # 파티에 진실을 아는 사람이 존재할 경우 (교집합)
            truth_party[idx] = 1
            truth = truth.union(set(party))  # 합집합

print(truth_party.count(0))
