n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_sum = 0

# 가로 1*3
for i in range(n):
    for j in range(m-2):
        current_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2]
        max_sum = max(max_sum, current_sum)

# 세로 1*3
for i in range(n-2):
    for j in range(m):
        current_sum = arr[i][j] + arr[i+1][j] + arr[i+2][j]
        max_sum = max(max_sum, current_sum)

# ㄴ자 블럭
for i in range(n-1):
    for j in range(m-1):
        a = arr[i][j]
        b = arr[i][j+1]
        c = arr[i+1][j]
        d = arr[i+1][j+1]

        total_sum = a + b + c + d
        current_sum = total_sum - min(a,b,c,d)
        max_sum = max(max_sum, current_sum)

print(max_sum)