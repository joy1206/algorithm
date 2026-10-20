def solution(n, wires):
    answer = 21e8 # 두 전력망이 가지고 있는 송전탑의 개수의 차이 
    graph =[[] for _ in range(n+1)] # 인접리스트!
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a) #전선은 양방향이라 둘 다 추가해야함
    
    def dfs(node, cut_a, cut_b):
        visited[node] = True
        count = 1 
        
        for next_node in graph[node]:
            if (node == cut_a and next_node == cut_b) or (node == cut_b and next_node == cut_a) : continue
            
            if not visited[next_node]:
                count += dfs(next_node, cut_a, cut_b) 
        return count
        
    for a, b in wires:
        visited = [False] * (n+1) # 분할 후 전체를 돌아야 하니까
        count = dfs(a, a, b)
        answer = min(abs(2*count -n), answer)
    return answer