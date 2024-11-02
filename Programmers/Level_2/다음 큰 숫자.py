def solution(n):
    n_one_cnt = bin(n)[2:].count('1')

    num = n + 1
    while True:
        num_one_cnt = bin(num)[2:].count('1')
        if num_one_cnt == n_one_cnt:
            return num
        num += 1
