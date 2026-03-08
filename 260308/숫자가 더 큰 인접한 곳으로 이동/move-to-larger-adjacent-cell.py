import sys

n, r, c = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

curr_x, curr_y = r - 1, c - 1
ans_list = [arr[curr_x][curr_y]]

while True:
    found_next = False
    for i in range(4):
        nx = curr_x + dx[i]
        ny = curr_y + dy[i]
        if 0<= nx < n and 0<= ny< n:
            if arr[curr_x][curr_y] < arr[nx][ny]:
                curr_x = nx
                curr_y = ny
                ans_list.append(arr[curr_x][curr_y])
                found_next = True
                break
    if not found_next:
        break

print(*ans_list)


