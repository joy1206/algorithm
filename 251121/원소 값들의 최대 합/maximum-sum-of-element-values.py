n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
ans = 0

# 시작위치 start
for start in range(1, n+1):
    num = 0
    current_pos = start
    for _ in range(m):
        value = arr[current_pos]
        num += value
        current_pos = value
    ans = max(ans, num)

print(ans)
