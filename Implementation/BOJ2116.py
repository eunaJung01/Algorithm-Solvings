# 주사위 쌓기

import sys

input = sys.stdin.readline

dice_num = int(input().strip())
dices = []
for i in range(dice_num):
    dices.append(list(map(int, input().split())))
rotate = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

sum_result = []
for i in range(6):
    # 1층
    max_list = []
    dice = [1, 2, 3, 4, 5, 6]
    bottom = dices[0][i]
    top = dices[0][rotate[i]]
    dice.remove(bottom)
    dice.remove(top)
    max_list.append(max(dice))

    for j in range(1, dice_num):
        # 2~N층
        dice = [1, 2, 3, 4, 5, 6]
        bottom = top
        dice.remove(bottom)
        top = dices[j][rotate[dices[j].index(top)]]
        dice.remove(top)
        max_list.append(max(dice))
    sum_result.append(sum(max_list))

print(max(sum_result))
