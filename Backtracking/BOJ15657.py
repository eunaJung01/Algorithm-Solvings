# N과 M (8)

from sys import stdin, stdout

input = stdin.readline
print = stdout.write

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
v = []


def solve(index, cnt):
    if cnt == m:
        print(' '.join(map(str, v)) + '\n')
        return
    for i in range(index, n):
        v.append(a[i])
        solve(i, cnt + 1)
        v.pop()


solve(0, 0)
