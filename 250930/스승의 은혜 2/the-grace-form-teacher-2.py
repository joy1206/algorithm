N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort()
answer = 0

for i in range(N):
    coupon = P[i] // 2
    temp_B = B - coupon

    if temp_B < 0:
        continue
    student = 1
    for j in range(N):
        if i == j: continue
        temp_B -= P[j]
        if temp_B < 0:
            break
        else:
            student +=1
    answer = max(answer, student)

print(answer)