n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# i번째 건너 뛰었을때는 i-1번째부터 i+1번째의 거리를 구하면 된다.

answer = 21e8


for i in range(1, n-1): # 건너뛸 체크포인트를 결정하는 변수
    dist = 0
    prev_idx = 0 
    for j in range(1, n): # 건너뛴 후의 총 거리를 계산하기 위해 모든 체크포인트를 순회하는 변수
        # 내부 for문에서 건너뛰어야 할 i번째 체크포인트를 제외하고 다음 체크포인트로 바로 넘어가
        if j == i:
            continue
        dist += abs(points[prev_idx][0] - points[j][0]) + abs(points[prev_idx][1] - points[j][1])
        prev_idx = j

    answer = min(answer, dist)

print(answer)



