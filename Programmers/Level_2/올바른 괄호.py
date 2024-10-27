def solution(s):
    stack = []

    for i in list(s):
        if i == '(':
            stack.append(i)
            continue

        if len(stack) == 0:
            return False
        stack.pop()

    if len(stack) == 0:
        return True
    return False
