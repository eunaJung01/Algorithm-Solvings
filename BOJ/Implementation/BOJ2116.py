# 주사위 쌓기

import sys

input = sys.stdin.readline

N = int(input().strip())
dices = [list(map(int, input().split())) for _ in range(N)]
facings = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

result = []
for first_bottomIdx in range(6):
    # 1층
    dice = [1, 2, 3, 4, 5, 6]
    bottom = dices[0][first_bottomIdx]
    top = dices[0][facings[first_bottomIdx]]
    dice.remove(bottom)
    dice.remove(top)
    maxSideNums = [max(dice)]

    # 2~N층
    for j in range(1, N):
        dice = [1, 2, 3, 4, 5, 6]
        bottom = top
        top = dices[j][facings[dices[j].index(top)]]
        dice.remove(bottom)
        dice.remove(top)
        maxSideNums.append(max(dice))

    result.append(sum(maxSideNums))

print(max(result))
