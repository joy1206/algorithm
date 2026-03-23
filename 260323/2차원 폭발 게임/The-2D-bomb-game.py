n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 중력
def gravity():
    global grid
    next_grid = [[0] * n for _ in range(n)]
    for j in range(n):
        curr_row = n - 1
        for i in range(n-1, -1, -1):
            if grid[i][j] != 0:
                next_grid[curr_row][j] = grid[i][j]
                curr_row -= 1
    grid = next_grid
# 폭탄 터트리기
def explode():
    global grid
    while True :
        # 터트릴 곳을 표시할 False 지도
        to_delete = [[False] * n for _ in range(n)]
        is_exploded = False
        for j in range(n):
            i = 0
            while (i < n):
                if grid[i][j] == 0:
                    i += 1
                    continue
                # 시작 위치
                start_i = i
                # 시작 값 저장
                num = grid[i][j]
                # 각 열 순회
                while (i< n and grid[i][j] == num) :
                    i +=1 
                length = i - start_i
                if length >= m :
                    is_exploded = True
                    for k in range(start_i, i):
                        to_delete[k][j] = True
        # 만약 True로 바뀐 곳이 하나도 업
        if not is_exploded:
            break

        for r in range(n):
            for c in range(n):
                if to_delete[r][c]:
                    grid[r][c] = 0
        gravity()

# 90회전
def roate():
    global grid
    is_rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            is_rotated[j][n-1-i] = grid[i][j] 
    grid = is_rotated
    gravity()
    
# K번 루프 반복
for _ in range(k):
    explode()
    roate()
# 마지막으로 한 번 더 터트림
explode()

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] !=0:
            ans +=1
print(ans)