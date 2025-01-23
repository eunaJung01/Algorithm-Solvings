def solution(arr):
    answer = []
    compress(arr, answer, 0, 0, len(arr))

    zeros = 0
    ones = 0
    for num in answer:
        if num == 0:
            zeros += 1
        elif num == 1:
            ones += 1
    return [zeros, ones]


def compress(arr, answer, y, x, n):
    if n == 1:
        answer.append(arr[y][x])
        return

    num = arr[y][x]
    for ny in range(y, y + n):
        for nx in range(x, x + n):
            if arr[ny][nx] == num:
                continue

            if arr[ny][nx] != num:
                compress(arr, answer, y, x, n // 2)
                compress(arr, answer, y + n // 2, x, n // 2)
                compress(arr, answer, y, x + n // 2, n // 2)
                compress(arr, answer, y + n // 2, x + n // 2, n // 2)
                return

    answer.append(num)
