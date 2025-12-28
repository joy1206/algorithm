n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 21e8
# 최소부터 최대까지 a, a+k
min_num = min(arr)
max_num = max(arr)
for i in range(min_num, max_num+1):
    current_cost = 0
    for j in range(n):
        num_cost = min(abs(arr[j]-i), abs(arr[j]-(i+k)))
        current_cost += num_cost
    if current_cost < ans:
        ans = current_cost

print(ans)
    