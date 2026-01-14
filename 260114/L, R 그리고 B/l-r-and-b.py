board = [list(input()) for _ in range(10)]

lx, ly = 0, 0
rx, ry = 0, 0
bx, by = 0, 0

for x in range(10):
    for y in range(10):
        if board[x][y] == 'L':
            lx, ly = x, y
        elif board[x][y] == 'R':
            rx, ry = x, y
        elif board[x][y] == 'B':
            bx, by = x, y
            
ans = abs(lx-bx) + abs(ly-by) -1

if ly == ry == by:
    if (lx < rx < bx) or (bx < rx < lx):
        ans += 2
elif lx == rx == bx:
    if (ly < ry < by) or (by < ry < ly):
        ans += 2

print(ans)