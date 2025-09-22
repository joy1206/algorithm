N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

cost = 21e8

for i in range(N-T+1):
    temp = 0
    for j in range(i, i+T):
        temp += abs(arr[j] - H)
    if temp < cost:
        cost = temp
print(cost)
            
