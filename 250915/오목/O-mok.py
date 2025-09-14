board = [list(map(int, input().split())) for _ in range(19)]

# 검은색 1
# 흰색 2
# 알 없음 0

dx = [1, 1, 0, 1]
dy = [0, -1, 1, 1]

def solution(x, y):
    color = board[x][y]
    for k in range(4):
        count = 1
        for step in range(1, 5):
            next_x = x + dx[k] * step
            next_y = y + dy[k] * step
            if 0<= next_x < 19 and 0<= next_y < 19:
                if board[next_x][next_y] == color:
                    count +=1
                else:
                    break
            else:
                break
        if count == 5:
            return color, (x, y)
    return 0, None


for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            color, coords = solution(i, j)
            if color != 0:
                print(color)
                print(coords[0] + 1, coords[1] + 3)
                exit(0) 

print(0) 



