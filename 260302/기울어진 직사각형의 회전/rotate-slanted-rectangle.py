n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c, m1, m2, m3, m4, dir = map(int, input().split())

r,c = r-1, c-1

path = []
curr_r, curr_c = r, c

# 1번 방향
for _ in range(m1):
    curr_r -=1
    curr_c +=1
    path.append((curr_r, curr_c))

# 2번 방향
for _ in range(m2):
    curr_r -=1
    curr_c -=1
    path.append((curr_r, curr_c))

# 3번 방향
for _ in range(m3):
    curr_r +=1
    curr_c -=1
    path.append((curr_r, curr_c))

# 4번 방향
for _ in range(m4):
    curr_r +=1
    curr_c +=1
    path.append((curr_r, curr_c))

# 그 좌표에 있는 숫자들을 뽑기
values= [] 
for x, y in path:
    values.append(grid[x][y])

# 한 칸 씩 밀기
if dir == 0:
    # 반시계
    rotated = [values[-1]] + values[:-1]
else:
    # 시계
    rotated = values[1:] + [values[0]]

for i in range(len(path)):
    r, c = path[i]
    grid[r][c] = rotated[i]

for row in grid:
    print(*row)