import sys
from collections import deque
n, m, k= map(int, sys.stdin.readline().split())

# 사과의 위치 (1-based index 그대로 쓰기 위해 n+1 크기)
apple = [[False] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    r_a, c_a = map(int, sys.stdin.readline().split())
    apple[r_a][c_a] = True

time = 0
game_over = False

directions = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}

# 뱀위 위치
is_snake_body = [[False] * (n + 1) for _ in range(n + 1)]
snake_body_coords = deque([(1, 1)]) # 실제 좌표 순서
is_snake_body[1][1] = True

for _ in range(k):
    d, p = sys.stdin.readline().split()
    p = int(p)

    for _ in range(p):
        # R 4
        time += 1

        # 현재 머리 위치
        head_r, head_c = snake_body_coords[0]
        dr, dc = directions[d]

        # 새로운 머리
        nr, nc = head_r + dr, head_c + dc

        # 범위 check
        if not (1 <= nr <= n and 1<= nc <= n):
            game_over = True
            break

        # 사과가 있다면
        if apple[nr][nc]:
            # 꼬리는 사라지지 않고 몸의 길이가 1 늘어나게 됩니다.
            apple[nr][nc] = False
        else:
            # 꼬리는 사라집니다.
            tail_r, tail_c = snake_body_coords.pop()
            is_snake_body[tail_r][tail_c] = False

        # 내 몸과 부딪히는지 check
        if is_snake_body[nr][nc]:
            game_over = True
            break

        # 새로운 머리 추가
        snake_body_coords.appendleft((nr, nc))
        is_snake_body[nr][nc] = True

        
    if game_over:
        break
print(time)