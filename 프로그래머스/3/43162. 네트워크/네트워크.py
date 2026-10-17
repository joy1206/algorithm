def solution(n, computers):
    visited = [False] * n
    answer = 0
    def dfs(num):
        visited[num] = True
        for i in range(n):
            # 1,2
            if not visited[i] and computers[num][i] == 1:
                dfs(i)
    
    for i in range(n):
        if not visited[i] :
            dfs(i)
            answer += 1
    return answer