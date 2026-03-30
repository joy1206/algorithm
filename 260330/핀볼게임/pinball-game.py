n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# U, D, L, R
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 거울에 따른 방향 변화 매핑 (현재 방향 -> 바뀔 방향)
mirror1 = {0: 3, 1: 2, 2: 1, 3: 0} # / : 상->우, 하->좌, 좌->하, 우->상
mirror2 = {0: 2, 1: 3, 2: 0, 3: 1} # \ : 상->좌, 하->우, 좌->상, 우->하

def simulate(r, c, d):
    time = 0
    curr_r, curr_c, curr_d = r, c, d
    while 0 <= curr_r < n and 0 <= curr_c < n:
        time +=1
        if grid[curr_r][curr_c] == 1:
            curr_d = mirror1[curr_d]
        elif grid[curr_r][curr_c] == 2:
            curr_d = mirror2[curr_d]
        
        curr_r = curr_r + dr[curr_d]
        curr_c = curr_c + dc[curr_d]
    return time + 1

for j in range(n):
    ans = max(ans, simulate(0, j, 1))

for j in range(n):
    ans = max(ans, simulate(n-1, j, 0))

for j in range(n):
    ans = max(ans, simulate(j, n-1, 2))

for j in range(n):
    ans = max(ans, simulate(j, 0, 3))

print(ans)