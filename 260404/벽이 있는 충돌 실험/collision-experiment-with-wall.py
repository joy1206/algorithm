MAX_N = 50
t = int(input())
n, m = 0, 0
marbles = []
marbles_cnt = [
    [0 for _ in range(MAX_N + 1)]
    for _ in range(MAX_N + 1)
]

mapper = {'U':0, 'R':1, 'L': 2, 'D': 3}

def in_range(x, y ):
    return 1<=x and x<=n and 1<=y and y<=n

# 1초 뒤 구슬의 위치와 방향
def move(marbles):
    dxs = [-1, 0, 0, 1]
    dxy = [0, 1, -1, 0]
    x, y, dir = marbles
    nx = x + dxs[dir]
    ny = y + dxy[dir]
    if in_range(nx, ny):
        return (nx, ny, dir)
    else:
        return (x, y, 3-dir)

# 구슬 전부 한 칸씩 움직이기
def move_all():
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble)

# 겹침 확인
def duplicate_marble(target_idx):
    target_x, target_y, _ = marbles[target_idx]
    return marbles_cnt[target_x][target_y] >=2

# 충돌 지우기
def remove():
    global marbles
    for x, y, _ in marbles:
        marbles_cnt[x][y] += 1
    
    remaining_marbels = []
    for i, marble in enumerate(marbles):
        if not duplicate_marble(i):
            remaining_marbels.append(marble)

    for x, y, _ in marbles:
        marbles_cnt[x][y] -= 1
    
    marbles = remaining_marbels

# 조건에 맞춰 시뮬레이션
def simulate():
    move_all()

    remove()

for _ in range(t):
    marbles = []

    n, m = tuple(map(int, input().split()))

    for _ in range(m):
        x, y, dir = tuple(input().split())
        x, y = int(x), int(y)
        marbles.append((x, y, mapper[dir]))
    
    for _ in range(2*n):
        simulate()

    print(len(marbles))