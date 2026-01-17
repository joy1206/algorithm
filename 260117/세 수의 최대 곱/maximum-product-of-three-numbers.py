n = int(input())
arr = list(map(int, input().split()))

max_num = -21e8

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            num = arr[i] * arr[j] * arr[k]
            max_num = max(max_num, num)
print(max_num)
            