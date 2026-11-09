def solution(citations):
    citations.sort()
    for h in range(citations[-1], -1, -1):
        count = 0
        for c in citations:
            if c >= h:
                count +=1
        if count >= h:
            return h