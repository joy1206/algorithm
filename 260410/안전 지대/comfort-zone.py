# 런타임 에러의 이유 = Python에서 기본 재귀 제한이 1000이기 때문
# 문제에서는 N, M이 최대 50 -> 50 * 50 = 2500칸
import sys
sys.setrecursionlimit(10**6) 
# bfs를 활용하면 재귀 제한 걱정 없이 풀 수 있다.

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)] # 각 집의 높이
visited =[[False] * n for _ in range(n)]

# 1. 최대 높이 구하기
max_h = 0
for row in grid:
    max_h = max(max_h, max(row))

safe_cnt = 0 # 최대 영역의 수

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
    
def dfs(x, y, k):
    visited[x][y] = True

    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny] > k:
            dfs(nx, ny, k)

best_k = 1
max_safe_cnt = 0

for k in range(1, max_h+1):
    visited= [[False]* m for _ in range(n)]
    current_safe_areas = 0
    for i in range(n):
        for j in range(m):
            # 아직 안가본 구역의 입구를 찾으면
            if not visited[i][j] and grid[i][j] > k:
                current_safe_areas += 1
                dfs(i, j, k)
    if current_safe_areas > max_safe_cnt:
        max_safe_cnt = current_safe_areas
        best_k = k

print(best_k, max_safe_cnt)