N, K = map(int, input().split())
max_end = 301
arr = [0] * max_end
answer = 0

for _ in range(N):
    candy, pos = map(int, input().split())
    arr[pos] += candy

for c in range(max_end):
    temp = 0
    for i in range(max(0, c-K), min(max_end, c+K+1)):
        temp += arr[i]
    if temp > answer:
        answer = temp
print(answer)

