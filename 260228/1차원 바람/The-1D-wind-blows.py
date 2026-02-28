import sys

n, m, q = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def shift(idx, direction):
    if direction == 'L':
        arr[idx] = [arr[idx][-1]] + arr[idx][:-1]
    else:
        arr[idx] = arr[idx][1:] + [arr[idx][0]]

def same(r1, r2):
    for i in range(m):
        if arr[r1][i] == arr[r2][i]:
            return True
    return False

def flip(d):
    return 'R' if d == 'L' else 'L'

for _ in range(q):
    r, d = sys.stdin.readline().split()
    curr_r = int(r) - 1
    curr_d = d

    shift(curr_r, curr_d)

    # 위쪽으로 전파
    up_r, up_d = curr_r, curr_d
    while (up_r > 0):
        if same(up_r, up_r-1):
            up_d = flip(up_d)
            shift(up_r -1, up_d)
            up_r -= 1
        else: break

    # 아래쪽으로 전파
    down_r, down_d = curr_r, curr_d
    while (down_r < n-1):
        if same(down_r, down_r+1):
            down_d = flip(down_d)
            shift(down_r +1, down_d)
            down_r += 1
        else: break

for row in arr:
    print(*row)