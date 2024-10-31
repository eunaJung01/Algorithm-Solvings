def solution(s):
    answer = s[0].upper()

    capitalize_flag = False
    for i in range(1, len(s)):
        if s[i] == ' ':
            capitalize_flag = True
            answer += s[i]
            continue

        if capitalize_flag:
            answer += s[i].upper()
            capitalize_flag = False
            continue

        answer += s[i].lower()

    return answer
