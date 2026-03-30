import sys
n, m, t = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

marbles = []
for _ in range(m):
    r, c = map(int, sys.stdin.readline().split())
    marbles.append((r - 1, c - 1))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 어디로 이동할지 탐색
def move(x, y):
    max_num = -1  # 주변 칸 중 가장 큰 값 저장하는 변수
    next_pos = (x, y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if grid[nx][ny] > max_num :
                max_num = grid[nx][ny]
                next_pos = (nx, ny)
    return next_pos
# T초간 시뮬레이션
for _ in range(t):
    count = [[0]*n for _ in range(n)]

    for r, c in marbles:
        nr, nc = move(r, c)
        count[nr][nc] += 1

    # 충돌한 구슬 제거한 새 리스트
    new_marbles = []
    for r, c in marbles:
        nr, nc = move(r,c)
        if count[nr][nc] == 1:
            new_marbles.append((nr,nc))
    marbles = new_marbles

    if not marbles:
        break
print(len(marbles))