import sys
n, m, r, c = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
dice = [1, 6, 2, 5, 4, 3]
curr_r = r -1
curr_c = c -1
ans = 0

grid = [[0] * n for _ in range(n)]
grid[curr_r][curr_c] = dice[1]

for dir in range(m):
    nr = curr_r
    nc = curr_c
    if arr[dir] == 'L':
        nc -=1
    elif arr[dir] == 'D':
        nr +=1
    elif arr[dir] == 'R':
        nc +=1
    else:
        nr -=1
    
    if not (0<= nc < n and 0<=nr<n):
        continue
    
    curr_r = nr
    curr_c = nc

    if arr[dir] == 'L':
        dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
    elif arr[dir] == 'D':
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]
    elif arr[dir] == 'R':
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
    else:
        dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]

    grid[curr_r][curr_c] = dice[1]

for row in grid:
    ans += sum(row)

print(ans)