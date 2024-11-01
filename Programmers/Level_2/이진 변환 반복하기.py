def solution(s):
    convert_cnt = 0
    zero_cnt = 0

    while s != "1":
        one_cnt = s.count("1")
        zero_cnt += (len(s) - one_cnt)

        s = bin(one_cnt)[2:]
        convert_cnt += 1

    return [convert_cnt, zero_cnt]
