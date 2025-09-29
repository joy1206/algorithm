n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

answer = -21e8

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1 = points[i][0]
            x2 = points[j][0]
            x3 = points[k][0]
            y1 = points[i][1]
            y2 = points[j][1]
            y3 = points[k][1]

            # 평행 확인
            if ((x1 == x2) or (x2==x3) or (x1==x3)) and ((y1==y2) or (y2==y3)or (y1==y3)):
                xmin = min(x1, x2, x3)
                ymin = min(y1, y2, y3)
                xmax = max(x1, x2, x3)
                ymax = max(y1, y2, y3)

                temp = (xmax - xmin) * (ymax-ymin)
                answer = max(answer, temp)
print(answer)




            