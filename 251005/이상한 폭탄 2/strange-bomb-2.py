N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

ans = -1 

# 폭탄 쌍 i, j
for i in range(N):
    for j in range(i+1, N):
        if num[i] == num[j]:
        # j - i가 K 이내인지 확인
            if j - i <= K:
                ans = max(ans, num[i])

print(ans)