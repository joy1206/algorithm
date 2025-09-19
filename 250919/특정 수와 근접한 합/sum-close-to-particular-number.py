N, S = map(int, input().split())
arr = list(map(int, input().split()))

sum_arr = sum(arr)
value = S

for i in range(N):
    for j in range(i+1, N):
        temp = sum_arr - (arr[i] + arr[j])
        if value > abs(S - temp):
            value = abs(S - temp)
print(value)