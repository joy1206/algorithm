n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
answer = 0

# 겹치지 않는다 = x좌표가 서로 엇갈릴때

for i in range(n):
    is_intersecting = False
    for j in range(n):
        if i==j : continue
        x1i = lines[i][0]
        x2i = lines[i][1]
        x1j = lines[j][0]
        x2j = lines[j][1]

        if ((x1i < x1j) and (x2i > x2j)) or ((x1i > x1j) and (x2i < x2j)):
            #겹친다
            is_intersecting = True
            break

    if not is_intersecting : answer +=1
print(answer)