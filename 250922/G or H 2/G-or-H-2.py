import sys

n = int(input())
people = []

for _ in range(n):
    pos, alpha = input().split()
    people.append((int(pos),alpha))

people.sort()
answer = 0

for i in range(n):
    for j in range(i, n):
        g_cnt = 0
        h_cnt = 0
        # i ~ j 구간에 있는 사람들 확인
        for k in range(i, j + 1):
            if people[k][1] == 'G':
                g_cnt += 1
            else:
                h_cnt += 1
        
        # 조건 체크
        if g_cnt == h_cnt or g_cnt == 0 or h_cnt == 0:
            current_len = people[j][0] - people[i][0]
            answer = max(answer, current_len)

print(answer)