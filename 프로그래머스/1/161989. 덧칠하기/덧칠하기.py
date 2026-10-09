def solution(n, m, section):
    answer = 0
    next = 0
    for s in section:
        if s >= next:
            next = s + m
            answer += 1
    return answer