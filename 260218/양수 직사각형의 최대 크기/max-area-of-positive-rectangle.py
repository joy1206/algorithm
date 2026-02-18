n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def solution(r1, r2, c1, c2):
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            if grid[i][j] <=0:
                return False
    return True
    
max_size = -1

for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                if solution(r1, r2, c1, c2):
                    current_size = (r2-r1+1) * (c2-c1+1)
                    if current_size > max_size:
                        max_size = current_size

print(max_size)