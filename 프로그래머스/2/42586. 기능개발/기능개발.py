from collections import deque
def solution(progresses, speeds):
    q = deque()
    answer = []
    for i in range(len(progresses)):
        if ((100 -progresses[i]) / speeds[i]) > ((100 -progresses[i]) // speeds[i]):
            q.append((100 -progresses[i]) // speeds[i] +1 )
        else:
            q.append((100 -progresses[i]) // speeds[i])
            
    while q:
        first = q.popleft()
        num = 1
        while q and q[0] <= first :
            num += 1
            q.popleft()
        answer.append(num)
    return answer
            
            
    