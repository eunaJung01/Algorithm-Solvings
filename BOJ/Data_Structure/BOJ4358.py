# 생태학

import sys

trees = []
trees_dic = {}
count = 0

while True:
    tree = sys.stdin.readline().strip()
    if not tree:
        break

    if tree in trees_dic:
        trees_dic[tree] += 1
    else:
        trees.append(tree)
        trees_dic[tree] = 1
    count += 1

trees.sort()

for t in trees:
    print("%s %.4f" % (t, trees_dic[t] / count * 100))
