n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_sum = -21e8

for r1 in range(n):
    for c1 in range(m):
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                sum1 = 0   
                for i in range(r1, r2+1):
                    for j in range(c1, c2+1):
                        sum1 += grid[i][j]   

                for R1 in range(n):
                    for C1 in range(m):
                        for R2 in range(R1, n):
                            for C2 in range(C1, m):
                                if (r2<R1) or (R2<r1) or (c2<C1) or (C2<c1):
                                    sum2 = 0
                                    for k in range(R1, R2+1):
                                        for l in range(C1, C2+1):
                                            sum2+= grid[k][l]
                                    if sum1 + sum2 > max_sum:
                                        max_sum = sum1 + sum2

print(max_sum)