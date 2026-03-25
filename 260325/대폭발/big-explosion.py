import sys

n, m, r, c = map(int, sys.stdin.readline().split())
r, c = r - 1, c - 1

bombs= set([(r,c)])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(1, m+1):
    dist = 2**(t-1)
    new_bombs_to_add = set()
    for br, bc in bombs:
        for i in range(4):
            nr, nc = br + dr[i] * dist, bc + dc[i] * dist
            if 0<=nr<n and 0<=nc<n:
                new_bombs_to_add.add((nr, nc))
    bombs.update(new_bombs_to_add)

print(len(bombs))


