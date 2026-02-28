import sys
n, m, q = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def shift(r1, c1, r2, c2):
    # 빈자리 생성
    temp = arr[r1][c1]

    for i in range(r1, r2):
        # 왼쪽 변
        arr[i][c1] = arr[i+1][c1]
    for j in range(c1, c2):
        # 아래쪽
        arr[r2][j] = arr[r2][j+1]
    for k in range(r2, r1, -1):
        # 오른쪽
        arr[k][c2] = arr[k-1][c2]
    for l in range(c2, c1+1, -1):
        # 위쪽
        arr[r1][l] = arr[r1][l-1]
        
    arr[r1][c1+1] = temp


def average(r1, c1, r2, c2):
    temp_arr = [row[:] for row in arr]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            total = arr[i][j]
            cnt = 1

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0<= ny < m:
                    total += arr[nx][ny]
                    cnt +=1
            
            temp_arr[i][j] = total // cnt 

    for i in range(r1,r2 +1):
        for j in range(c1, c2+1):
            arr[i][j] = temp_arr[i][j]

for _ in range(q):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    shift(r1,c1,r2,c2)
    average(r1,c1,r2,c2)

for row in arr:
    print(*row)