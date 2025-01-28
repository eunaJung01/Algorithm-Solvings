from itertools import permutations
from math import sqrt


def solution(numbers):
    numbers = [str(i) for i in numbers]
    combinations = get_combinations(numbers)

    answer = 0
    for n in combinations:
        if is_prime_number(n):
            answer += 1
    return answer


def get_combinations(numbers):
    combinations = set()
    for i in range(1, len(numbers) + 1):
        num_list = list(permutations(numbers, i))
        for num in num_list:
            combinations.add(int(''.join(num)))
    return combinations


def is_prime_number(n):
    if n == 0 or n == 1:
        return False

    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
