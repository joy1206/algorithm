import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
ans = -1

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)

def dfs(vertex):
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)
dfs(1)
for i in range(n+1):
    if visited[i]:
        ans += 1
print(ans)