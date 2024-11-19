pair = {')': '(', ']': '[', '}': '{'}


def solution(s):
    n = len(s)

    answer = 0
    for base in range(n):
        if is_valid(s, n, base):
            answer += 1
    return answer


def is_valid(s, n, base):
    stack = []

    for offset in range(n):
        char = s[(base + offset) % n]

        if char in "([{":
            stack.append(char)
            continue

        if char in ")]}":
            if len(stack) == 0 or pair[char] != stack[-1]:
                return False
            stack.pop()

    if len(stack) > 0:
        return False
    return True
