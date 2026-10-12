def solution(N, stages):
    answer = []
    # 실패율이 높은 스테이즈부터 내림차순으로
    # 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
    # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
    dic = {}  #스테이지 : 실패율
    
    def fail(stage):
        not_clear = 0 # 스테이지에 도달했으나 아직 클리어하지 못함
        reach = 0 # 스테이지에 도달한 플레이어 수
        for i in range(len(stages)):
            if stages[i] >= stage:
                reach += 1
            if stages[i] == stage:
                not_clear += 1
        if reach == 0:
            return 0
        return not_clear/reach
    for i in range(1, N+1):
        if i not in dic:
            dic[i] = fail(i)
    # sorted(리스트, key정렬기준)
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    for key, value in sorted_dic:
        answer.append(key)
    return answer