from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque(enumerate(priorities))

    while q:
        current = q.popleft()
        possible = True
        if q:
            for i in range(len(q)):
                if q[i][1] > current[1]:
                    q.append(current)
                    possible = False
                    break
        if possible:
            answer += 1
            
            if current[0] == location:
               return answer