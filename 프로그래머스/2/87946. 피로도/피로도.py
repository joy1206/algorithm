def solution(k, dungeons):
    visited = [False] * len(dungeons)
    
    def dfs(fatigue):
        max_result = 0
        for i in range(len(dungeons)):
            if not visited[i] and fatigue >= dungeons[i][0] :
                visited[i] = True
                count = 1 + dfs(fatigue-dungeons[i][1])
                visited[i] = False
                max_result = max(max_result, count)
        return max_result
    return dfs(k)