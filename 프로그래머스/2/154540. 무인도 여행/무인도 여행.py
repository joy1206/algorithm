from collections import deque
def solution(maps):
    answer = []
    m = len(maps)
    n = len(maps[0])
    visited = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(False)
        visited.append(row)
        
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
        
    def bfs(sx, sy):
        q = deque()
        q.append((sx, sy))
        visited[sx][sy] = True
        count = 0
        while q:
            x, y = q.popleft()
            count += int(maps[x][y])
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<m and 0<=ny<n:
                    if maps[nx][ny] != 'X' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
        return count
    
    for i in range(m):
        for j in range(n):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i,j))
                
    if len(answer) == 0:
        answer.append(-1)
    else:
        answer.sort()
               
    return answer