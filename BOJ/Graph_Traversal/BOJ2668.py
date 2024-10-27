# 숫자고르기

# 시간 초과
# import sys
#
# input = sys.stdin.readline
#
# N = int(input().strip())
# second = [int(input().strip()) for _ in range(N)]
#
# result = 0
# visited = [False for _ in range(N)]
# firstList, secondList = [], []
#
#
# def DFS(max, cnt):
#     global result, firstList, secondList
#
#     if result != 0:
#         return
#
#     if cnt == max:
#         for f in firstList:
#             if f in secondList:
#                 continue
#             else:
#                 return
#         result = max
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             firstList.append(i + 1)
#             secondList.append(second[i])
#             DFS(max, cnt + 1)
#             if result != 0:
#                 return
#             secondList.pop()
#             firstList.pop()
#             visited[i] = False
#
#
# for i in range(N, 0, -1):
#     DFS(i, 0)
#     if result != 0:
#         break
#
# print(result)
# secondList.sort()
# for s in secondList:
#     print(s)

# ---

# ???
# import sys
#
# input = sys.stdin.readline
#
# N = int(input().strip())
# second = [int(input().strip()) for _ in range(N)]
#
# result = 0
# visited = [False for _ in range(N)]
# resultList = []
#
#
# def DFS(cur, start):
#     global result, resultList
#
#     if visited[cur]:
#         if cur == start:
#             resultList.append(cur)
#             result += 1
#     else:
#         visited[cur] = True
#         DFS(second[cur], start + 1)
#
#
# for i in range(N):
#     visited = [False for _ in range(N)]
#     DFS(i, i)
#
# print(len(resultList))
# for r in resultList:
#     print(r)

# ---

N = int(input())  # 입력
arr = [0]  # 두번째 줄 숫자 담을 리스트.
for _ in range(N):
    arr.append(int(input()))
answer = set()  # 결과 담을 set


# dfs 정의
def dfs(first, second, num):
    first.add(num)  # 첫번째 줄 집합에 num 추가
    second.add(arr[num])  # 두번째 줄 집합에 arr[num] 추가
    if arr[num] in first:  # arr[num]이 첫번째 줄 집합에 있을 때
        if first == second:  # 첫번째 줄 집합과 두번째 줄 집합이 같다면
            answer.update(first)  # 결과 업데이트
            return True
        return False
    return dfs(first, second, arr[num])  # 아니라면 다음 dfs 실행


# dfs 실행
for i in range(1, N + 1):
    if i not in answer:  # i가 결과 집합 안에 없는 경우만 실행
        dfs(set(), set(), i)

print(len(answer))
print(*sorted(list(answer)), sep='\n')
