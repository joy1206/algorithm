n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
min_length = 21e8
for i in range(n):
    min_x = 101
    max_x = 0
    for j in range(n):
        if i == j: continue
        current_min = segments[j][0]
        current_max = segments[j][1]
        min_x = min(min_x, current_min)
        max_x = max(max_x, current_max)
    min_length = min(min_length, max_x - min_x)
print(min_length)

        
