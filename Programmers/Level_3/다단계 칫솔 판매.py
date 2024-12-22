def solution(enroll, referral, seller, amount):
    n = len(enroll)
    name_to_id = dict()
    for i, e_name in enumerate(enroll):
        name_to_id[e_name] = i

    parents = [-1 for _ in range(n)]
    for i, r_name in enumerate(referral):
        if r_name == "-":
            continue
        parents[i] = name_to_id[r_name]

    answer = [0 for _ in range(n)]
    for i in range(len(seller)):
        seller_id = name_to_id[seller[i]]
        money = amount[i] * 100
        while seller_id > -1:
            to_parent = money // 10
            answer[seller_id] += money - to_parent
            money = to_parent
            if money == 0:
                break
            seller_id = parents[seller_id]
    return answer
