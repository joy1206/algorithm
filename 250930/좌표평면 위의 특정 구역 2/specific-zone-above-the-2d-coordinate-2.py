n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
answer = 21e8
for i in range(n):
    max_x, max_y = -21e8, -21e8
    min_x, min_y = 21e8, 21e8

    for j in range(n):
        if i == j : continue

        min_x = min(min_x, points[j][0])
        max_x = max(max_x, points[j][0])
        min_y = min(min_y, points[j][1])
        max_y = max(max_y, points[j][1])
    
    square = (max_x - min_x) * (max_y - min_y)
    answer = min(answer, square)
print(answer)

