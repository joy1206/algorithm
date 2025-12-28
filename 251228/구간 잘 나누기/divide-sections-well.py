n, m = map(int, input().split())
arr = list(map(int, input().split()))

def is_possible(limit):
    count = 1
    current_sum = 0 

    for num in arr:
        if num > limit:
            return False
        if current_sum + num > limit:
            # 새로운 구간 시작
            count += 1
            current_sum = num
        else: current_sum += num

    return (count <= m)


low = max(arr)
high = sum(arr)
ans = high

while low <= high:
    mid = (low + high) // 2

    if is_possible(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)