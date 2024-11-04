def solution(s):
    stack = [s[0]]

    for char in s[1:]:
        if len(stack) == 0 or char != stack[-1]:
            stack.append(char)
            continue
        stack.pop()

    if len(stack) == 0:
        return 1
    return 0
