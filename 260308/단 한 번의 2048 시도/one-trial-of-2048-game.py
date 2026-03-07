import sys
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]

dir = input()

# 한줄에 숫자 4개를 받아서 처리
def process_line(line):
    temp = [num for num in line if num !=0]

    new_line= [] #같은 숫자 합치기
    i = 0
    while i < len(temp):
        if i+1 < len(temp) and temp[i] == temp[i+1]:
            new_line.append(temp[i]*2)
            i += 2
        else:
            new_line.append(temp[i])
            i += 1

    while len(new_line) < 4:
        new_line.append(0)
    return new_line

next_grid = [[0]*4 for _ in range(4)]

if dir == 'L':
    for i in range(4):
        next_grid[i] = process_line(grid[i])
elif dir == 'R':
    for i in range(4):
        # 뒤집어서 처리한 뒤 다시 뒤집기
        next_grid[i] = process_line(grid[i][::-1])[::-1]
elif dir == 'U':
    for j in range(4):
        col = []
        for i in range(4):
            col.append(grid[i][j])
        process_col = process_line(col)

        for i in range(4):
            next_grid[i][j] = process_col[i]

elif dir == 'D':
    for j in range(4):
        col = []
        for i in range(4):
            col.append(grid[i][j])
        process_col = process_line(col[::-1])[::-1]

        for i in range(4):
            next_grid[i][j] = process_col[i]

for row in next_grid:
    print(*row)
