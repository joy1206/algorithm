import sys

N, M, D, S = map(int, input().split())
# 먹은 기록: [[사람, 치즈, 시간], ...]
eats = [list(map(int, input().split())) for _ in range(D)]
# 아픈 기록: [[사람, 시간], ...]
pains = [list(map(int, input().split())) for _ in range(S)]

ans = 0 

# 모든 치즈를 순회하며 상했다고 가정
for i in range(1, M + 1):
    is_rotten = True  # 현재 i번 치즈가 상했다고 가정

    # '이 치즈가 상했을까?' 판단
    # 아픈 기록에 있는 모든 사람이 아프기 전에 이 치즈를 먹었는지 확인
    for p_pain, t_pain in pains:
        did_eat_before_pain = False
        for p_eat, m_eat, t_eat in eats:
            # 아픈 사람과 먹은 기록의 사람이 같고,
            # 현재 가정하는 치즈와 먹은 치즈가 같으며,
            # 먹은 시간이 아픈 시간보다 이르다면 (아프기 전에 먹었다면)
            if p_eat == p_pain and m_eat == i and t_eat < t_pain:
                did_eat_before_pain = True
                break  # 이 사람에 대한 확인이 끝났으므로 다음 아픈 사람으로
        
        # 만약 한 명이라도 아프기 전에 이 치즈를 먹지 않았다면,
        # 이 치즈는 상한 치즈일 수 없다.
        if not did_eat_before_pain:
            is_rotten = False
            break  # 이 치즈는 상한 치즈가 아니므로, 다음 치즈로 넘어감

    # '몇 명이 아플까?' 계산
    # 이 치즈가 상했을 가능성이 있다고 판단되면
    if is_rotten:
        # 이 치즈를 먹은 사람들을 찾아 총 몇 명인지 계산
        sick_people = set()
        for p_eat, m_eat, t_eat in eats:
            # 현재 가정하는 치즈(i)를 먹은 모든 사람을 sick_people에 추가
            if m_eat == i:
                sick_people.add(p_eat)
        
        # 최대 아픈 사람 수 갱신
        ans = max(ans, len(sick_people))

print(ans)