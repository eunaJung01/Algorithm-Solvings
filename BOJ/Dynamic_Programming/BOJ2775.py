# 부녀회장이 될테야

import sys

input = sys.stdin.readline

apartment = [[0 for _ in range(15)] for _ in range(15)]
for room_num in range(1, 15):
    apartment[0][room_num] = room_num

for floor in range(1, 15):
    for room_num in range(1, 15):
        apartment[floor][room_num] = apartment[floor][room_num - 1] + apartment[floor - 1][room_num]

T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    n = int(input().strip())
    print(apartment[k][n])
