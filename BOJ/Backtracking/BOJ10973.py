# 이전 순열

# 시간 초과
# import copy
# import sys
# sys.setrecursionlimit(10**6)
#
# input = sys.stdin.readline
#
# N = int(input().strip())
# line = list(map(int, input().split()))
#
# visited = [False] * N
# status = False
# arr = []
# result = []
#
#
# def func(cnt):
#     global status
#
#     if status:
#         return
#
#     if cnt == N:
#         temp = copy.deepcopy(arr)
#         result.append(temp)
#         if len(result) == 3:
#             result.pop(0)
#
#         for i in range(N):
#             if arr[i] != line[i]:
#                 return
#
#         if len(result) == 1:
#             print(-1)
#         else:
#             for r in result[0]:
#                 print(r, end=' ')
#         status = True
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             arr.append(i + 1)
#             func(cnt + 1)
#             arr.pop()
#             visited[i] = False
#
#
# func(0)

# ---

def prev_permutation(a):
    n = len(a) - 1
    i = n
    while i > 0 and a[i - 1] <= a[i]:
        i -= 1
    if i == 0:
        return False
    j = n
    while a[i - 1] <= a[j]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    j = n
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True


n = int(input())
a = list(map(int, input().split()))

if prev_permutation(a) is True:
    for i in a:
        print(i, end=' ')
    print()
else:
    print(-1)
