def solution(k, score):
    answer = []
    reward_list = []
    
    for i in range(len(score)):
        if len(reward_list) < k:
            reward_list.append(score[i])
        else:
            if score[i] > reward_list[0]:
                reward_list[0] = score[i]
                
        reward_list.sort()
        answer.append(reward_list[0])
    return answer
            