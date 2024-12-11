def solution(s):
    answer = 1
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if j - i + 1 <= answer:
                continue
            if is_palindrome(s[i:j + 1]):
                answer = max(answer, j - i + 1)
    return answer


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
