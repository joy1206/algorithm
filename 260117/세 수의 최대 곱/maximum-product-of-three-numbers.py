n = int(input())
arr = list(map(int, input().split()))

max_num = -21e8

for i in range(n):
    if arr[i] < 0 : continue
    for j in range(n):
        for k in range(n):
            if i == j or j == k or i == k : continue
            if arr[j] * arr[k] >= 0:
                num = arr[i] * arr[j] * arr[k]
                max_num = max(max_num, num)
print(max_num)
