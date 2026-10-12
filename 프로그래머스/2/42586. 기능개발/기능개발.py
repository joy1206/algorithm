from collections import deque
def solution(progresses, speeds):
    q = deque()
    answer = []
    for i in range(len(progresses)):
        if ((100-progresses[i]) / speeds[i]) > ((100-progresses[i]) // speeds[i]):
            q.append((100-progresses[i])//speeds[i] + 1)
        else:
            q.append((100-progresses[i])// speeds[i])
    
    while q:
        count = 1
        first = q.popleft()
        while q and q[0] <= first:
            count += 1
            q.popleft()
        answer.append(count)
            
    return answer
            
            
    