def solution(k, dungeons):
    answer = -1 # 최대 탐험 던전
    # 아직 안 간 던전 + 현재 피로도 -> 방문처리 -> 피로도 깎고 다음 던전 탐색 -> 다 탐색 -> 방문처리 취소 -> 다른 던전 선택
    visited = [False] * len(dungeons)
    def dfs(fatigue, count):
        nonlocal answer
        answer = max(answer, count)
        for i in range(len(dungeons)):
            if not visited[i] and fatigue >= dungeons[i][0]:
                visited[i]=True
                
                dfs (fatigue - dungeons[i][1], count +1)
                visited[i] = False
    dfs(k, 0)      
    return answer