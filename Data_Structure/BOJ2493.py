# 탑

# 시간 초과
# ---
# import sys
#
# N = int(sys.stdin.readline().strip())
# line = list(map(int, sys.stdin.readline().split()))
#
# tower = []
# for i in range(1, N + 1):
#     tower.append([line[i - 1], i])
# tower = tower[::-1]  # [타워 높이][타워 번호]
# result = []
#
# max_h = max(line)
# max_h_list = []
#
# # [[4, 5], [7, 4], [5, 3], [9, 2], [6, 1]]
# for i in range(N):
#     t = tower[i]
#     h = t[0]  # 현재 보고있는 건물의 높이
#
#     if h == max_h:  # 가장 높이가 높은 건물 -> 일단 0
#         result.append(0)
#         max_h_list.append(t[1])
#     elif t[1] == 1:  # 가장 왼쪽 건물 -> 0
#         result.append(0)
#     else:
#         for j in range(N - t[1] + 1, N):
#             tower_now = tower[j]
#             if h <= tower_now[0]:
#                 result.append(tower_now[1])
#                 break
#
# if len(max_h_list) > 1:
#     idx = 1
#     while idx < len(max_h_list):
#         result[max_h_list[idx - 1] - N] = max_h_list[idx]
#         idx += 1
#
# result = result[::-1]
# for r in result:
#     print(r, end=' ')

# ---
import sys

N = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().split()))

tower = []  # [타워 높이][타워 번호]
for i in range(1, N + 1):
    tower.append([line[i - 1], i])
stack = [tower[0]]
result = [0]

for i in range(1, N):
    now_tower = tower[i]

    if stack[len(stack) - 1][0] >= now_tower[0]:  # stack top h >= 현재 보는 h
        result.append(stack[-1][1])
        stack.append(now_tower)

    else:  # stack top h < 현재 보는 h
        while stack[-1][0] < now_tower[0]:  # stack top h >= 현재 보는 h가 될 때까지
            stack.pop()
            if len(stack) == 0:
                break

        if len(stack) == 0:
            result.append(0)
        else:
            result.append(stack[-1][1])
        stack.append(now_tower)

for r in result:
    print(r, end=' ')
