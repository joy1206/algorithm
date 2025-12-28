n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 21e8
current_cost = 0
while ans > current_cost :
    for i in range(n):
        max_arr = max(arr)
        min_arr = min(arr)
        if arr[i] == max_arr:
            arr[i] -= 1
            current_cost +=1
        elif arr[i] == min_arr:
            arr[i] += 1
            current_cost += 1
        ans = current_cost

print(ans)

    