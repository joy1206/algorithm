def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
        
    for start in range(len(discount)-9):
        new_list = discount[start:start+10]
        new_dic = dic.copy()
        for fruit in new_list:
            if fruit in new_dic:
                new_dic[fruit] -= 1
                
        possible = True
        for key in new_dic:
            if new_dic[key] != 0:
                possible = False
                break
        if possible:
            answer +=1

    return answer