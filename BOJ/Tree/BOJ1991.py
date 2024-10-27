# 트리 순회

import sys


class Node:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None


N = int(sys.stdin.readline().strip())

root = None


def insert_node(parent, n, left, right):
    if parent.n == n:
        parent.left = Node(left)
        parent.right = Node(right)
        return
    else:
        if parent.left is not None:
            insert_node(parent.left, n, left, right)
        if parent.right is not None:
            insert_node(parent.right, n, left, right)


for _ in range(N):
    line = list(sys.stdin.readline().split())

    n = line[0]
    left = line[1] if line[1] != '.' else None
    right = line[2] if line[2] != '.' else None

    if n == 'A':
        root = Node(n)

    insert_node(root, n, left, right)

result = [[] for _ in range(3)]


# 전위 순회 (루트, 왼쪽, 오른쪽)
def pre(node):
    global result

    if node.left is None and node.right is None:
        if node.n is not None:
            result[0].append(node.n)
        return

    result[0].append(node.n)
    if node.left is not None:
        pre(node.left)
    if node.right is not None:
        pre(node.right)


# 중위 순회 (왼쪽, 루트, 오른쪽)
def mid(node):
    if node.left is None and node.right is None:
        if node.n is not None:
            result[1].append(node.n)
        return

    if node.left is not None:
        mid(node.left)
    result[1].append(node.n)
    if node.right is not None:
        mid(node.right)


# 후위 순회 (왼쪽, 오른쪽, 루트)
def post(node):
    if node.left is None and node.right is None:
        if node.n is not None:
            result[2].append(node.n)
        return

    if node.left is not None:
        post(node.left)
    if node.right is not None:
        post(node.right)
    result[2].append(node.n)


pre(root)
mid(root)
post(root)

for r in result:
    print(''.join(r))
