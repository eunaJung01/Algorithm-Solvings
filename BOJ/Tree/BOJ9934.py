# 완전 이진 트리

import sys

K = int(sys.stdin.readline().strip())  # 깊이 K
pre = list(map(int, sys.stdin.readline().split()))  # 전위 순회 결과

tree = [[] for _ in range(K)]
d = 0


def get_tree(lst, d):
    global tree
    half = int(len(lst) / 2)

    if half == 0:
        tree[d].append(lst[half])
    else:
        tree[d].append(lst[half])
        get_tree(lst[:half], d + 1)
        get_tree(lst[half + 1:], d + 1)


get_tree(pre, d)

for t in tree:
    for node in t:
        print(node, end=' ')
    print()
