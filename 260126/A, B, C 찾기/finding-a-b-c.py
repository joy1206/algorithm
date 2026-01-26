arr = list(map(int, input().split()))
arr.sort()
print(arr[0], arr[1], max(arr) - arr[1] - arr[0])
