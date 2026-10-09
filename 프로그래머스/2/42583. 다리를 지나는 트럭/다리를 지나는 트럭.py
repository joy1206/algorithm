from collections import deque
def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)
    bridge = deque() #(트럭의 무게, 들어온 시간)
    time = 0
    bridge_weight = 0
    while waiting or bridge:
        time += 1
        
        # 다리를 다 건넌 트럭 빼기
        if bridge and time - bridge[0][1] == bridge_length:
            truck_weight, entered_time = bridge.popleft()
            bridge_weight -= truck_weight
            
        # 대기 트럭 확인하기
        if waiting:
            next_truck = waiting[0]
            if bridge_weight + next_truck <= weight:
                waiting.popleft()
                bridge.append((next_truck, time))
                bridge_weight += next_truck
        
    return time