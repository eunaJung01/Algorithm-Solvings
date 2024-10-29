def solution(operations):
    q = []

    for operation in operations:
        op, num = operation.split()

        if op == 'I':
            q.append(int(num))
            continue

        if len(q) == 0:
            continue

        if int(num) == 1:
            q.pop(q.index(max(q)))
            continue

        q.pop(q.index(min(q)))

    if len(q) == 0:
        return [0, 0]
    return [max(q), min(q)]
