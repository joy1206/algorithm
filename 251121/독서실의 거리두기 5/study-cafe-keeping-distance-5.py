N = int(input())
seat = input()
ans = 0

for i in range(N):
    if seat[i] == '0':
        new_seat_list = list(seat)
        new_seat_list[i] = '1'
        new_seat = "".join(new_seat_list) # 다시 문자열로 합침

        # 1인 인덱스 찾기
        occupied_indices = []
        for idx in range(N):
            if new_seat[idx] == '1':
                occupied_indices.append(idx)

        current_min_dist = N + 1

        for k in range(len(occupied_indices)-1):
            dist = occupied_indices[k+1] - occupied_indices[k]
            current_min_dist = min(current_min_dist, dist)

        ans = max(ans, current_min_dist)

print(ans)
            
                
