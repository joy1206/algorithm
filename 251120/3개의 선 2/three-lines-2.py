n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(11):
    for j in range(11):
        for k in range(11):
            success = True
            # x축에 평행한 직선 3개
            for x, y in points:
                if x == i or x == j or x == k:
                    continue
                success = False
            if success: ans = 1
            
            # x축 평행한 직선 2개, y축 평행한 직선 1개
            success = True
            for x, y in points:
                if x == i or x == j or y == k:
                    continue
                success = False
            if success : ans = 1

            # x축 평행한 직선 1개, y축 평행한 직선 2개
            success = True
            for x, y in points:
                if x == i or y == j or y == k:
                    continue
                success = False
            if success : ans = 1

            # y축 평행한 직선 3개
            success = True
            for x, y in points:
                if y == i or y == j or y == k:
                    continue
                success = False
            if success : ans = 1

print(ans)




