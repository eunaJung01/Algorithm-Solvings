# 회장뽑기

import sys
from collections import defaultdict

input = sys.stdin.readline

studentNum = int(input().strip())
friendsDict = defaultdict(list)

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    friendsDict[a].append(b)
    friendsDict[b].append(a)


def DFS(studentId, level):
    global scores
    friends = friendsDict[studentId]
    for friendId in friends:
        if scores[friendId] > level:
            scores[friendId] = level
            DFS(friendId, level + 1)


INF = int(10e6)
min_score, result_list = sys.maxsize, list()
for studentId in range(1, studentNum + 1):
    scores = [INF for _ in range(studentNum + 1)]
    scores[studentId] = 0
    DFS(studentId, 1)

    score = max(scores[1:])
    if score < min_score:
        min_score = score
        result_list = [studentId]
    elif score == min_score:
        result_list.append(studentId)

print(min_score, len(result_list))
result_list.sort()
for result in result_list:
    print(result, end=' ')
