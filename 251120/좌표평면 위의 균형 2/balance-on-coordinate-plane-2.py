n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans = 21e8

for i in range(0, 101, 2):
    for j in range(0, 101, 2):
        # 두 개의 직선 x = i, y =j
        dots = [0,0,0,0]
        for x,y in points:
            if x < i and y > j : dots[0] +=1
            elif x > i and y > j : dots[1] +=1
            elif x < i and y < j : dots[2] +=1
            elif x > i and y < j : dots[3] +=1
        ans = min(ans, max(dots))
print(ans)