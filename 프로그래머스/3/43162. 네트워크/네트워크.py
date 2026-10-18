def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def dfs(num):
        visited[num] = True
        for i in range(n):
            if not visited[i] and computers[num][i] == 1:
                    dfs(i)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    
    return answer