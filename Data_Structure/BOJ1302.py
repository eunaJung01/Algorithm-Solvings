# 베스트셀러

import sys

input = sys.stdin.readline

N = int(input().strip())

book = {}
for _ in range(N):
    title = input().strip()
    if title in book:
        book[title] += 1
    else:
        book[title] = 1

s = list(sorted(book.items(), key=lambda item: item[1], reverse=True))
l = []
for title, num in s:
    if num == s[0][1]:
        l.append(title)
l.sort()
print(l[0])
