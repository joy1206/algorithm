N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

answer = 0

for i in range(N):
    student = 0
    coupon = P[i] // 2
    temp_B = B - coupon
    for j in range(N):
        if i == j: continue
        tempB = B - P[j]
        if temp_B < 0:
            break
        else:
            student +=1
    answer = max(answer, student)

print(student)