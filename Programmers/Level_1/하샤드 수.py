def solution(x):
    t = sum(int(n) for n in str(x))
    if x % t == 0:
        return True
    return False
