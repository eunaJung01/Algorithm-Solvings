from math import ceil
from collections import deque

max_time = 23 * 60 + 59


def solution(fees, records):
    default_time, default_fee, unit_time, unit_fee = fees

    cars = dict()
    for record in records:
        time_HH_MM, car_num, status = record.strip().split(" ")

        hour, minute = map(int, time_HH_MM.split(":"))
        time = hour * 60 + minute

        if car_num in cars:
            cars[car_num].append((time, status))
            continue
        cars[car_num] = [(time, status)]

    car_fee = []
    for car_num, car in cars.items():
        car.sort(key=lambda x: x[0])
        total_time = get_total_time(car)

        fee = default_fee
        if total_time > default_time:
            fee += ceil((total_time - default_time) / unit_time) * unit_fee
        car_fee.append((car_num, fee))
    car_fee.sort()

    answer = []
    for car, fee in car_fee:
        answer.append(fee)
    return answer


def get_total_time(car):
    car = deque(car)

    total_time = 0
    in_time = -1
    while car:
        time, _ = car.popleft()
        if in_time == -1:
            in_time = time
            continue
        total_time += time - in_time
        in_time = -1

    if in_time != -1:
        total_time += max_time - in_time
    return total_time
