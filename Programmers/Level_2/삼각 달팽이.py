def solution(n):
    if n == 1:
        return [1]

    arr = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    for i in range(n):
        arr[i][0] = num
        num += 1
    for i in range(1, n):
        arr[n - 1][i] = num
        num += 1

    y = n - 1
    x = n - 1
    while True:
        first_y = y
        first_x = x

        # reverse diagonal
        ny = y - 1
        nx = x - 1
        while 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 0:
            y = ny
            x = nx
            arr[y][x] = num
            num += 1
            ny = y - 1
            nx = x - 1

        # down
        ny = y + 1
        while 0 <= ny < n and arr[ny][x] == 0:
            y = ny
            arr[y][x] = num
            num += 1
            ny = y + 1

        # right
        nx = x + 1
        while 0 <= nx < n and arr[y][nx] == 0:
            x = nx
            arr[y][x] = num
            num += 1
            nx = x + 1

        if first_y == y and first_x == x:
            break

    answer = []
    for i, row in enumerate(arr):
        answer.extend(row[:i + 1])
    return answer
