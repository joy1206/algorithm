N, K = map(int, input().split())
max_end = 101
locations = {}
arr = [0] * max_end
answer = 0

for _ in range(N):
    candy, pos = map(int, input().split())
    locations[pos] = candy

for pos, candy in locations.items():
    arr[pos] += candy

for c in range(max_end):
    if c - K > 0 and c + K < max_end:
        temp = 0
        for i in range(c-K, c+K+1):
            temp += arr[i]
        if temp >answer:
            answer = temp
print(answer)

