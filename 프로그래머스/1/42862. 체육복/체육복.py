def solution(n, lost, reserve):
    dic = {}
    for i in range(1, n+1):
        dic[i] = 1
        if i in lost:
            dic[i] -=1
        if i in reserve:
            dic[i] +=1
    
    for i in range(1, n+1):
        if dic[i] == 0:
            if i-1 > 0 and dic[i-1] == 2:
                dic[i-1] -=1
                dic[i] += 1
            elif i+1 <=n and dic[i+1] == 2:
                dic[i+1] -=1
                dic[i] +=1        
    
    answer = 0
    for i in range(1, n+1):
        if dic[i] > 0:
            answer +=1
    return answer