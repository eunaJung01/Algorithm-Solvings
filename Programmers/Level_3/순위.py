def solution(n, results):
    table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for A, B in results:
        # win
        table[A][B] = 1
        # lose
        table[B][A] = -1

    for i in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if table[a][i] == 1 and table[i][b] == 1:
                    table[a][b] = 1
                if table[a][i] == -1 and table[i][b] == -1:
                    table[a][b] = -1

    answer = 0
    for i in range(1, n + 1):
        known_cnt = 0
        for j in range(1, n + 1):
            if table[i][j] != 0:
                known_cnt += 1
        if known_cnt == n - 1:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5, 6], [6, 7]]), 4)
print(solution(6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]), 6)
print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
print(solution(3, [[1, 2], [1, 3]]), 1)
print(solution(6, [[1, 6], [2, 6], [3, 6], [4, 6]]), 0)
print(solution(8, [[1, 2], [3, 4], [5, 6], [7, 8]]), 0)
print(solution(9, [[1, 2], [1, 3], [1, 4], [1, 5], [6, 1], [7, 1], [8, 1], [9, 1]]), 1)
print(solution(6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [2, 4], [2, 6]]), 6)
print(solution(4, [[4, 3], [4, 2], [3, 2], [3, 1], [4, 1], [2, 1]]), 4)
print(solution(3, [[3, 2], [3, 1]]), 1)
print(solution(4, [[1, 2], [1, 3], [3, 4]]), 1)
