n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

answer = 21e8

# 가장 가까운 두 점 사리의 거리에 제곱을 한 값

# 두 점 i와 j
for i in range(n):
    for j in range(i+1, n):
        x1 = points[i][0]
        x2 = points[j][0]
        y1 = points[i][1]
        y2 = points[j][1]

        temp = (x1-x2)**2 + (y1-y2)**2
    answer = min(answer, temp)

print(answer)