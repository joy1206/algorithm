from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_weight = 0
    bridge = deque()
    waiting = deque(truck_weights)
    
    while waiting or bridge:
        time += 1
        if bridge and time - bridge[0][1] == bridge_length:
            truck_weight, entered_time = bridge.popleft()
            bridge_weight -= truck_weight
        if waiting and bridge_weight + waiting[0] <= weight:
            truck_weight = waiting.popleft()
            bridge_weight += truck_weight
            bridge.append((truck_weight, time))
    return time