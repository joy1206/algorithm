N, M, D, S = map(int, input().split())

# 먹은 기록 (eats): [[p, m, t], [p, m, t], ...]
eats = [list(map(int, input().split())) for _ in range(D)]
# 아픈 기록 (pains): [[p, t], [p, t], ...]
pains = [list(map(int, input().split())) for _ in range(S)]

max_sick_people = 0

# 상한 치즈가 맞는지 판별
def is_rotten(cheese_idx):
    for p_pain, t_pain in pains:
        has_eaten = False
        for p_eat, m_eat, t_eat in eats:
            if p_eat == p_pain and m_eat == cheese_idx and t_eat < t_pain:
                has_eaten = True
                break

    if not has_eaten: return False
    return True # 모든 아픈 사람이 이 치즈를 먹음

# i는 상한 치즈 번호
for i in range(1, M+1):
    if is_rotten(i) :
        sick_people = set()
        for p_eat, m_eat, t_eat in eats:
            if m_eat == i:
                sick_people.add(p_eat)

        max_sick_people = max(max_sick_people, len(sick_people))

print(max_sick_people)




