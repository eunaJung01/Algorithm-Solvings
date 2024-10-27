def solution(s):
    arr = list(map(int, s.split()))
    arr.sort()

    return str(min(arr)) + " " + str(max(arr))
