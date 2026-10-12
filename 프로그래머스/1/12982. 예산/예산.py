def solution(d, budget):
    answer = 0 
    d.sort()
    total = 0
    if sum(d) <= budget:
        answer = len(d)
    for i in range(len(d)):
        total += d[i]
        if total > budget:
            answer = i
            break
        
        
    return answer