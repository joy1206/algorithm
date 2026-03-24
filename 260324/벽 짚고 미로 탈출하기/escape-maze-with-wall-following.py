import sys
n = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())
x -= 1
y -= 1
ans = -1
time = 0
grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
curr_dir = 0 # 처음은 우측을 보고 시작
visited = [[[False]*4 for _ in range(n)] for _ in range(n)]

def is_out(r,c):
    return not (0 <= r < n and 0 <= c < n)

while True:
    if visited[x][y][curr_dir]:
        print(-1)
        break
    visited[x][y][curr_dir] = True
    nx = x + dx[curr_dir]
    ny = y + dy[curr_dir]
    # step1: 바라보고 있는 방향으로 이동하는 것이 가능하지 않는 경우 -> 반 시계 방향으로 90도
    if not is_out(nx, ny) and grid[nx][ny] == '#':
        curr_dir = (curr_dir -1) % 4
        continue

    # step2: 바로보고 있는 방향으로 이동하는 것이 가능한 경우
    # -> case1: 바로 앞이 격자 밖이면 탈출
    if is_out(nx, ny):
        time += 1
        print(time)
        break
    
    right_dir = (curr_dir + 1) % 4
    rx = nx + dx[right_dir]
    ry = ny + dy[right_dir]
    # -> case2: 만약 그 방향으로 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 짚을 벽이 있다면 그 방향으로 한 칸 이동
    if not is_out(rx, ry) and grid[rx][ry] == '#':
        x = nx
        y = ny
        time +=1
    # -> case3: 만약 그 방향으로 이동했다 가정했을 때 해당 방향을 기준으로 오른쪽에 짚을 벽이 없다면 현재 방향으로 한 칸 이동 후 방향을 시계 방향으로 90도 틀어 한 칸 더 전진
    else:
        # 1. 일단 현재 방향으로 한 칸 이동 (1초)
        x = nx
        y = ny
        time += 1
        # 2. 방향을 시계 방향(오른쪽)으로 90도 회전
        curr_dir = right_dir
        # 3. 그 방향으로 한 칸 더 전진 (1초)
        x, y = x + dx[curr_dir], y + dy[curr_dir]
        time += 1

        if is_out(x, y):
            print(time)
            break
        