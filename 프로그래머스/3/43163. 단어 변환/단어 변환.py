def solution(begin, target, words):
    answer = 21e8
    visited = [False] * len(words)
    def dfs(current, count):
        nonlocal answer
        if current == target:
            answer = min(answer, count)
            return
        for i in range(len(words)):
            if not visited[i] :
                diff = 0
                for j in range(len(current)):
                    if current[j] != words[i][j]:
                        diff += 1
                if diff == 1:
                    visited[i]= True
                    dfs(words[i], count + 1)
                    visited[i] = False
    
    dfs(begin, 0)
    
    if answer == 21e8:
        answer = 0
    return answer