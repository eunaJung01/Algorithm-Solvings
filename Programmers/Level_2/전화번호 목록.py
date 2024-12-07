def solution(phone_book):
    for phone_num in set(phone_book):
        for i in range(len(phone_num)):
            prefix = phone_num[:i]
            if prefix in phone_book:
                return False
    return True
