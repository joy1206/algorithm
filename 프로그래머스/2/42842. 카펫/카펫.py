def solution(brown, yellow):
    total = brown + yellow
    
    for h in range(1, total):
        if total % h == 0:
            w = total // h
            if w >= h and (w-2)*(h-2) == yellow:
                answer = [w, h]
                break
    return answer 