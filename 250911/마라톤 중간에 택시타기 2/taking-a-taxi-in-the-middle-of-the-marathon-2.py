n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 전체 거리 구하기
total_distance = 0
for i in range(n-1):
    dis = abs(points[i][0] - points[i+1][0]) + abs(points[i][1] - points[i+1][1])
    total_distance += dis

# 한 개씩 건너뛰는 모든 경우 
max_save_distance = 0
for i in range(1, n-1):
    # 안 건너 뛴 원래 거리
    dis = abs(points[i-1][0] - points[i][0]) + abs(points[i-1][1] - points[i][1]) + abs(points[i][0] - points[i+1][0]) + abs(points[i][1] - points[i+1][1])

    # 건너 뛴 거리
    skipped = abs(points[i-1][0] - points[i+1][0]) + abs(points[i-1][1] - points[i+1][1])

    # 단축량 dis - skipped
    saved = dis - skipped
    if max_save_distance < saved:
        max_save_distance = saved

answer = total_distance - max_save_distance
print(answer)
