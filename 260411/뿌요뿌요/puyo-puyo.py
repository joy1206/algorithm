n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

boom_cnt, max_block_size = 0, 0
curr_block_size = 0

def dfs(x, y, target_num):
    global curr_block_size
    curr_block_size += 1
    visited[x][y] = True
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny] and grid[nx][ny] == target_num:
                dfs(nx, ny, target_num)

for i in range(n):
    for j in range(n):
        # 아직 조사가 안된 입구를 발견하면
        if not visited[i][j]:
            curr_block_size = 0
            dfs(i, j, grid[i][j])

            # 탐험 끝
            if curr_block_size >= 4:
                boom_cnt += 1

            max_block_size = max(max_block_size, curr_block_size)

print(boom_cnt, max_block_size)