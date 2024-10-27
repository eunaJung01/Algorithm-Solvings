# N과 M (1)

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0 for _ in range(M + 1)]
status = [False for _ in range(N + 1)]


def func(k):  # 현재 k개까지의 수를 택했음
    if k == M:  # M개를 모두 택했으면 arr에 기록해둔 수를 출력
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, N + 1):  # 1부터 n까지의 수에 대해
        if not status[i]:  # 아직 i가 사용되지 않았으면
            arr[k] = i  # k번째 수를 i로 정함
            status[i] = True  # i를 사용되었다고 표시
            func(k + 1)  # 다음 수를 정하러 한 단계 더 들어감
            status[i] = False  # k번째 수를 i로 정한 모든 경우에 대해 다 확인했으므로 i를 이제 사용하지 않았다고 명시


func(0)
