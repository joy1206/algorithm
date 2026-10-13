def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    i = 0
    while i + m <= len(score):
        new_box = score[i:i+m]
        i += m
        answer += new_box[-1] * m
        
    
    
    return answer