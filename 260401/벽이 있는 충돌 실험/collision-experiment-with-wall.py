import sys

def moves(n, x, y, d):
    # 상 하 좌 우 
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if d =='U':
        nx = x + dx[0]
        ny = y + dy[0]
    elif d =='D':
        nx = x + dx[1]
        ny = y + dy[1]
    elif d =='L':
        nx = x + dx[2]
        ny = y + dy[2]
    else:
        nx = x + dx[3]
        ny = y + dy[3]
    if 0<=nx<n and 0<=ny<n:
        return nx, ny, d
    
    # 벽에 부딪히면 움직이지 않고 움직이는 방향만 반대로 뒤집힘, 이때 방향을 바꾸는 작업에는 1초의 시간 소요
    else :
        if d =='U':
            nd = 'D'
        elif d =='D':
            nd ='U'
        elif d =='L':
            nd ='R'
        else:
            nd ='L'
    return x, y, nd

t = int(sys.stdin.readline()) # 총 테스트 케이스 수
for _ in range(t) :
    n, m = map(int, sys.stdin.readline().split()) # m개의 구슬
    # 구슬의 정보 (x,y,d)
    marbles = []
    for _ in range(m):
        r, c, d = sys.stdin.readline().split()
        marbles.append([int(r) - 1, int(c) - 1, d])
    
    for _ in range(2*n +1):
        # 이번 초에 모든 구슬이 어디로 갈지 기록할 공용 격자
        temp_grid = [[0]*n for _ in range(n)]
        next_marbels = []

        for x, y, d in marbles:
            nx, ny, nd = moves(n, x, y, d)
            temp_grid[nx][ny] += 1

            next_marbels.append([nx,ny,nd])
        
        survivors = []
        for x, y, d in next_marbels:
            if temp_grid[x][y] == 1:
                # 살아남은
                survivors.append([x, y, d])
        marbles = survivors

        if not marbles:
            break

    print(len(marbles))