import sys
n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def find_pos(target):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == target:
                return i, j

for i in range(m):
    for num in range(1, n*n+1):
        x, y = find_pos(num)
        max_val, tx, ty = -1, -1, -1
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if grid[nx][ny] > max_val:
                    max_val = grid[nx][ny]
                    tx = nx
                    ty = ny

        if tx != -1:
            grid[x][y], grid[tx][ty] = grid[tx][ty], grid[x][y]

for row in grid:
    print(*row)