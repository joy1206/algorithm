n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = -21e8

for i in range(n-k):
    temp = 0
    for j in range(k):
        temp += arr[i+j]
    if temp > answer:
        answer = temp

print(answer)
        