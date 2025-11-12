N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]
ans= 0

for temp in range(1001):
    current_work = 0
    
    # 2. 모든 N개 장비에 대해 작업량을 합산
    for ta, tb in ranges:
        # 3. 작업량 조건에 따라 계산
        
        # 1. Ta보다 낮은 온도: C
        if temp < ta:
            current_work += C
        
        # 2. Ta 이상 Tb 이하: G
        elif ta <= temp <= tb:
            current_work += G
            
        # 3. Tb보다 높은 온도: H
        elif temp > tb:
            current_work += H

    ans = max(ans, current_work)
print(ans)

    