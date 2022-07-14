# 이진 검색 트리

import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, n):
        self.n = n
        self.left_child = None
        self.right_child = None


root = None


def insert_node(parent, child):
    if parent.left_child is None:
        if child.n < parent.n:
            parent.left_child = child
            return

    if parent.right_child is None:
        if child.n > parent.n:
            parent.right_child = child
            return

    if child.n < parent.n:
        insert_node(parent.left_child, child)
    elif child.n > parent.n:
        insert_node(parent.right_child, child)


while True:  # 입력(전위 순회 결과) 읽기
    n = sys.stdin.readline().strip()
    if not n:
        break

    else:
        node = Node(int(n))
        if root is None:
            root = node
        else:
            insert_node(root, node)


def print_post(node):  # 후위 순회
    # 자식 노드가 없을 경우 출력 -> return
    if node.left_child is None and node.right_child is None:
        print(node.n)
        return

    # 왼쪽, 오른쪽, 루트 순서로 방문
    if node.left_child is not None:
        print_post(node.left_child)
    if node.right_child is not None:
        print_post(node.right_child)
    print(node.n)


print_post(root)
