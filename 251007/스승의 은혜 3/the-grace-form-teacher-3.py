N, B = map(int, input().split())
gifts = [tuple(map(int, input().split())) for _ in range(N)]
# 최대 명수
answer = 0
for i in range(N):
    current_cost = gifts[i][0] // 2 + gifts[i][1]
    if current_cost > B:
        continue
    # 남은 학생들의 선물 가격을 리스트에 저장
    remaining_gifts = []
    for j in range(N):
        if i==j: continue
        remaining_gifts.append(gifts[j][0] + gifts[j][1])

    remaining_gifts.sort()
    current_B = B - current_cost
    current_students = 1 # 쿠폰 사용 학생 포함

    for cost in remaining_gifts:
        if current_B >= cost:
            current_B -= cost
            current_students +=1
        else: break
    answer = max(answer, current_students)
print(answer)
         
