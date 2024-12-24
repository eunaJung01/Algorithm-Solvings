def solution(n, t, m, p):
    arr = "00"
    i = 0
    while len(arr) < t * m:
        i += 1
        arr += str(convert_notation_to_n(n, i))

    answer = ""
    for i in range(t):
        answer += arr[m * i + p]
    return answer


def convert_notation_to_n(n, num):
    s = ""
    while num:
        s += get_value(num % n)
        num //= n
    return s[::-1]


def get_value(num):
    if num < 10:
        return str(num)
    return chr(55 + num)
