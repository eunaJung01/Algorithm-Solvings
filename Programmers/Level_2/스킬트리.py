def solution(skill, skill_trees):
    skill = list(i for i in skill)
    answer = 0
    for tree in skill_trees:
        if is_able_skill_tree(skill, tree):
            answer += 1
    return answer


def is_able_skill_tree(skill, tree):
    order = []
    for t in tree:
        if t in skill:
            order.append(t)

    for i, o in enumerate(order):
        if o != skill[i]:
            return False
    return True
