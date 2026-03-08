import sys
import copy
n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = 0

# 폭탄 터트리기
def boom(x, y, temp_grid):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    bomb_range = temp_grid[x][y]

    # 중심점 터뜨리기
    temp_grid[x][y] = 0

    for i in range(4):
        for j in range(1, bomb_range):
            nx = x + dx[i] * j
            ny = y + dy[i] * j
            if 0<=nx<n and 0<=ny<n:
                # 터트리기
                temp_grid[nx][ny] = 0

# 중력 적용 함수
def gravity(temp_grid):
    gravity_grid = [[0]* n for _ in range(n)]

    for col in range(n):
        current_row = n-1
        for row in range(n-1, -1, -1):
            if temp_grid[row][col] != 0:
                gravity_grid[current_row][col] = temp_grid[row][col]
                current_row -= 1
    return gravity_grid

# 같은 숫자의 2개의 칸 쌍의 개수
def count_pairs(temp_grid):
    cnt = 0
    for r in range(n):
        for c in range(n):
            if temp_grid[r][c] == 0: continue
            if 0<= c+1 < n:
                if temp_grid[r][c] == temp_grid[r][c+1]: cnt +=1
            if 0<= r+1 < n:
                if temp_grid[r][c] == temp_grid[r+1][c] : cnt +=1
    return cnt

for i in range(n):
    for j in range(n):
        temp_grid = copy.deepcopy(grid)
        boom(i, j, temp_grid)
        temp_grid = gravity(temp_grid)
        current_cnt = count_pairs(temp_grid)
        if ans < current_cnt : ans = current_cnt

print(ans)