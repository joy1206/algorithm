n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

# 각 마을의 사람 수
people_cnt = 0

def in_range(x, y):
    return 0<=x<n and 0<=y<n

def dfs(x, y):
    global people_cnt
    visited[x][y] = True
    people_cnt += 1

    dxs = [-1, 1, 0, 0]
    dxy = [0 , 0, -1, 1]

    for i in range(4):
        nx = x + dxs[i]
        ny = y + dxy[i]
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny)
# 마을별 인원 수 담을 리스트
villages = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            people_cnt = 0
            dfs(i, j)
            villages.append(people_cnt)

print(len(villages))
villages.sort()
for i in villages:
    print (i)