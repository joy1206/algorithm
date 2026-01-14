board = [list(input()) for _ in range(10)]

lx, ly = 0, 0
rx, ry = 0, 0
bx, by = 0, 0

ans = 0

for x in range(10):
    for y in range(10):
        if board[x][y] == 'L':
            lx, ly = x, y
        elif board[x][y] == 'R':
            rx, ry = x, y
        elif board[x][y] == 'B':
            bx, by = x, y
if lx == rx == bx or ly == ry == by:
    ans = abs(lx-bx) + abs(ly-by) +2
else:
    ans = abs(lx-bx) + abs(ly-by) -1
print(ans)