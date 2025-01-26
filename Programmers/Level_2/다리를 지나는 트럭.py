from collections import deque


def solution(bridge_length, weight, truck_weights):
    n = len(truck_weights)
    truck_weights = deque(truck_weights)

    bridge = deque()
    for _ in range(bridge_length):
        bridge.append(0)
    complete_cnt = 0

    answer = 0
    total_weight = 0

    while True:
        if complete_cnt == n:
            break
        answer += 1

        w = bridge.popleft()
        if w != 0:
            total_weight -= w
            complete_cnt += 1

        while (len(truck_weights) > 0 and
               total_weight + truck_weights[0] <= weight and
               len(bridge) < bridge_length):
            total_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())

        while len(bridge) < bridge_length:
            bridge.append(0)

    return answer
