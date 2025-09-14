N, M = map(int, input().split())
arr = [input() for _ in range(N)]

dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

answer = 0

def solution(x, y):
    count = 0 # 이 위치에서 찾은 "LEE"의 개수
    for k in range(8):
        # 첫 번째 'E'의 좌표 계산
        next_x1 = x + dx[k]
        next_y1 = y + dy[k]

        # 두 번째 'E'의 좌표 계산
        next_x2 = x + dx[k] * 2
        next_y2 = y + dy[k] * 2

        # 1. 첫 번째 'E'가 유효한 범위에 있는지 확인
        if 0 <= next_x1 < N and 0 <= next_y1 < M:
            if arr[next_x1][next_y1] == 'E':
                # 3. 두 번째 'E'가 유효한 범위에 있는지 확인
                if 0 <= next_x2 < N and 0 <= next_y2 < M:
                    if arr[next_x2][next_y2] == 'E':
                        count += 1
    return count
        
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            answer += solution(i, j)
print(answer)