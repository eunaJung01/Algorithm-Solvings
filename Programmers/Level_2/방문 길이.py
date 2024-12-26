directions = {
    "U": (1, 0),
    "D": (-1, 0),
    "R": (0, 1),
    "L": (0, -1)
}


def solution(dirs):
    visited = set()
    answer = 0
    y = 0
    x = 0

    n = 5
    for d in dirs:
        dy, dx = directions[d]
        ny = y + dy
        nx = x + dx
        if ny < -n or ny > n or nx < -n or nx > n:
            continue

        path = ((y, x), (ny, nx))
        reverse_path = ((ny, nx), (y, x))

        if path not in visited:
            answer += 1
            visited.add(path)
            visited.add(reverse_path)
        y = ny
        x = nx
    return answer
