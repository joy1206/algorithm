from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    waiting = deque(truck_weights)
    bridge = deque()
    bridge_weight = 0
    while waiting or bridge :
        time += 1
        if bridge and time - bridge[0][1] == bridge_length :
            truck_weight, entered_time = bridge.popleft()
            bridge_weight -= truck_weight
        if waiting and bridge_weight + waiting[0] <= weight :
            current_turck_weight = waiting.popleft()
            bridge.append((current_turck_weight, time))
            bridge_weight += current_turck_weight
    
    return time