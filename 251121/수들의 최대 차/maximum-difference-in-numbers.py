N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
ans = 0

for start in range(N):
    for end in range(start+1, N):
        if arr[end] - arr[start] <= K:
            temp = end - start + 1
            ans = max(ans, temp)

print(ans)
