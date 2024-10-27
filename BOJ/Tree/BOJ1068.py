# 트리

# # ??? 왜틀림 ???
# import sys
#
# N = int(sys.stdin.readline().strip())
#
# line = list(map(int, sys.stdin.readline().split()))
# parent = []  # (부모 노드, 노드 번호)
# for n, p in enumerate(line):
#     parent.append((p, n))
# parent.sort()
#
# d_node = int(sys.stdin.readline().strip())
#
# count = 0
# d = [d_node]  # 삭제되는 노드들
#
# if d_node != parent[0][1]:  # root가 아닐 경우
#     dic = {}
#
#     for p, n in parent:  # root 노드 제외
#         if p in d:
#             d.append(n)
#             continue
#         elif n in d:
#             continue
#         else:
#             if n not in dic:
#                 dic[n] = 0
#             if p not in dic:
#                 dic[p] = 1
#             else:
#                 dic[p] += 1
#
#     for v in dic.values():
#         if v == 0:
#             count += 1
#
# print(count)

# ---

import sys

N = int(sys.stdin.readline().strip())
parent = list(map(int, sys.stdin.readline().split()))
d_node = int(sys.stdin.readline().strip())

tree = [[] for _ in range(N)]  # child list
root = 0


def DFS(x):
    global result

    # 자식이 없는 경우
    if not tree[x]:
        result += 1
        return

    # 자식이 있는 경우
    for n in tree[x]:
        DFS(n)


for i in range(N):
    if parent[i] == -1:
        root = i
        continue

    if i == d_node:
        continue

    tree[parent[i]].append(i)

result = 0
if root != d_node:
    DFS(root)
print(result)
