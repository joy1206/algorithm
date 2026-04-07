n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

visited = [[False]*m for _ in range(n + 1)]
ans = 0 # (n-1, m-1에 도착하면 성공)

dxs = [1, 0]
dys = [0, 1]
found = False

def in_range(x, y):
    return 1<= x <=n and 1<=y<=n

def dfs(x, y):
    global found
    if x == n-1 and y == m-1 :
        found = True
        return
    for i in range(2):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0 <= nx < n and 0 <= ny < m:
            if edges[nx][ny] !=0 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)
                if found:
                    return
visited[0][0] = True
dfs(0,0)

if found:
    print(1)
else: 
    print(0)