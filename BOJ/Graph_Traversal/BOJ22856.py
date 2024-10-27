# 트리 순회

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

N = int(input().strip())
tree = [0 for _ in range(N + 1)]


class Node:
    def __init__(self, num, left, right):
        self.num = num
        self.leftChild = left
        self.rightChild = right


for _ in range(N):
    num, left, right = map(int, input().split())
    tree[num] = Node(num, left, right)


def findEndNode(num):
    global end, cnt_end
    visited[num] = True
    node = tree[num]
    right = node.rightChild

    if not visited[right] and right != -1:
        findEndNode(right)
        cnt_end += 1


root = 1
cnt_end = 0
visited = [False for _ in range(N + 1)]
if N != 2:
    findEndNode(root)

print((N - 1) * 2 - cnt_end)
