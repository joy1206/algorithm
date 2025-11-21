n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

ans = 0

for a in range(1, n+1):
    for b in range(a+1, n+1):
        current_pair = 0
        for x, y in pairs:
            if set((x, y)) == set((a, b)): current_pair +=1
        ans = max(ans, current_pair)

print(ans)