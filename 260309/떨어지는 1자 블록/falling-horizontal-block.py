import sys
n, m, k = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

start_y = k -1
end_y = k + m -1

target_row = 0

for x in range(n-1):
    can_go_down = True
    for y in range(start_y, end_y):
        if grid[x+1][y] == 1:
            can_go_down = False
            break
    if can_go_down: 
        target_row +=1
    else: 
        break

for i in range(start_y, end_y):
    grid[target_row][i] = 1
   
for row in grid:
    print(*row)