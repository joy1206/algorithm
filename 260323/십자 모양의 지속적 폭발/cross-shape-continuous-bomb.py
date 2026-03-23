n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
commands = [int(input()) for _ in range(m)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def gravity():
    global grid
    next_grid = [[0]* n for _ in range(n)]
    for j in range(n): # 각 열(Column)을 기준으로
        curr_row = n - 1 # 새 격자의 바닥부터 채울 포인터
        for i in range(n - 1, -1, -1): # 기존 격자의 바닥부터 위로 탐색
            if grid[i][j] != 0:
                next_grid[curr_row][j] = grid[i][j]
                curr_row -= 1
    grid = next_grid

# 폭탄이 터지는 시작 위치 찾기
# 선택된 열 c를 위에서부터 훑으며 처음으로 0이 아닌 숫자가 나오는 위치 (r, c)
def bomb(c):
    target_r = -1
    for r in range(n):
        if grid[r][c] != 0 :
            target_r = r
            break

    if target_r == -1 :
        return
# 십자 0으로 만들기
# 그 칸에 적힌 숫자를 V라고 하면, 중심을 포함해 상하좌우 방향으로 V-1만큼의 범위를 모두 0으로 바꿉니다.
    v = grid[target_r][c]
    grid[target_r][c] = 0
    for dist in range(1, v):
        for i in range(4):
            nx = target_r + dist * (dx[i])
            ny = c + dist * (dy[i])
            if 0 <= nx < n and 0 <= ny < n:
                grid[nx][ny] = 0

# 중력 적용하기
for c in commands:
    bomb(c-1)
    gravity()

for row in grid:
    print(*row)