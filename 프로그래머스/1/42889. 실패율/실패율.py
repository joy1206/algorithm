def solution(N, stages):
    answer = []
    dic = {} # (스테이지, 실패율)
    def fail(stage):
        not_clear = 0
        reach = 0
        # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        # 스테이지에 도달한 플레이어 수
        for i in range(len(stages)):
            if stages[i] == stage:
                not_clear += 1
            if stages[i] >= stage:
                reach += 1
        if not_clear == 0:
            return 0
        else:
            return (not_clear / reach)
        
    for i in range(1, N+1):
        if i not in dic:
            dic[i] = fail(i)
    
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    for key, value in sorted_dic:
        answer.append(key)
    return answer