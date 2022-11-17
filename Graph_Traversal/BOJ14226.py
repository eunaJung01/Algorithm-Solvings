# 이모티콘

# 12퍼에서 시간 초과
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# S = int(input().strip())
#
# MAX_EMOJI = 1000
# INF = 2147000000
# min_cnt = [INF] * (MAX_EMOJI + 1)
#
#
# def BFS():
#     q = deque()
#     emoji, clipboard = 1, 0
#     q.append((emoji, clipboard, 0))
#
#     while q:
#         emoji, clipboard, cnt = q.popleft()
#         cnt += 1
#
#         for i in range(1, 4):
#             update_emoji = emoji
#
#             if i == 1:  # 1. 이모지 복사 -> 클립보드에 저장
#                 q.append((update_emoji, emoji, cnt))
#                 continue
#
#             elif i == 2:  # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
#                 if clipboard == 0:
#                     continue
#                 update_emoji += clipboard
#
#             elif i == 3:  # 3. 화면에 있는 이모티콘 중 하나를 삭제
#                 if emoji - 1 < 0:
#                     continue
#                 update_emoji -= 1
#
#             if update_emoji < 0 or update_emoji > S:  # 음.......
#                 continue
#             if update_emoji == S:
#                 return cnt
#
#             if min_cnt[update_emoji] >= cnt:
#                 min_cnt[update_emoji] = cnt
#                 q.append((update_emoji, clipboard, cnt))
#
# # 화면 개수 & 클립보드 수마다 경우가 다르니까......?
# print(BFS())

# ---

from collections import deque
import sys

input = sys.stdin.readline

S = int(input().strip())
dist = [[-1] * (S + 1) for _ in range(S + 1)]


def BFS():
    q = deque()
    q.append((1, 0))  # 화면 이모티콘 개수, 클립보드 이모티콘 개수

    dist[1][0] = 0

    while q:
        emoji, clipboard = q.popleft()

        if dist[emoji][emoji] == -1:
            dist[emoji][emoji] = dist[emoji][clipboard] + 1
            q.append((emoji, emoji))

        if emoji + clipboard <= S and dist[emoji + clipboard][clipboard] == -1:
            dist[emoji + clipboard][clipboard] = dist[emoji][clipboard] + 1
            q.append((emoji + clipboard, clipboard))

        if emoji - 1 >= 0 and dist[emoji - 1][clipboard] == -1:
            dist[emoji - 1][clipboard] = dist[emoji][clipboard] + 1
            q.append((emoji - 1, clipboard))

    result = -1

    for i in range(S + 1):
        if dist[S][i] != -1:
            if result == -1 or result > dist[S][i]:
                result = dist[S][i]
    return result


print(BFS())
