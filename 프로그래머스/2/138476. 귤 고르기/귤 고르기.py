def solution(k, tangerine):
    answer = 0
    dic = {}
    for t in tangerine:
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] +=1
        
    lst = sorted(dic.values(), reverse = True)
    
    count = 0
    
    for num in lst:
        count += num
        answer += 1
        if count >= k:
            break
        
    return answer
# 1. 크기별 개수를 센다
# 2. 개수를 큰 것부터 정렬
# 3. 큰것부터 더한다
# 4. 합이 k가 되는순간까지 사용한 종류의 수를 센다

