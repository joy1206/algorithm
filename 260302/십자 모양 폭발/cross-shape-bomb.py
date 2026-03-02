n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

num = grid[r][c]

grid[r][c] = 0

for i in range(4):
    for dist in range(1, num):
        nx, ny = r + dx[i] * dist, c + dy[i] * dist
        if 0 <= nx < n and 0 <= ny < n:
            grid[nx][ny] = 0

# 아래로 떨어트리기
temp = [[0]*n for _ in range(n)]

for col in range(n):
    curr_idx = n-1
    for row in range(n-1, -1, -1):
        if grid[row][col] != 0:
            temp[curr_idx][col] = grid[row][col]
            curr_idx -= 1
 
for row in temp:
    print(*row)