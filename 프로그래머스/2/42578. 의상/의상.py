def solution(clothes):
    answer = 1
    dic = {}

    for i in range(len(clothes)):
        if clothes[i][1] not in dic:
            dic[clothes[i][1]] = 1
        else:
            dic[clothes[i][1]] += 1
    
    for i in dic:
        answer = answer * (dic[i] +1)
        
    return answer -1