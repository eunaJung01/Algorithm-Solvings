# 게으른 백곰

import sys

input = sys.stdin.readline

N, K = map(int, input().split())
ice_list = [tuple(map(int, input().split())) for _ in range(N)]
ice_list.sort(key=lambda x: (x[1], x[0]))

ice = [0 for _ in range(ice_list[-1][1] + 1)]
min_idx, result = sys.maxsize, -1
for i, idx in ice_list:
    ice[idx] = i
    min_idx = min(min_idx, idx)

end, curr = min_idx, 0
for start in range(min_idx, len(ice)):
    while end < len(ice) and end - start <= K * 2:
        if ice[end] == 0:
            end += 1
            continue
        curr += ice[end]
        end += 1
    result = max(result, curr)
    curr -= ice[start]

print(result)
