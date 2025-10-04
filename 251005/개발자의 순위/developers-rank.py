k, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]
ans = 0

# (a,b)
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b : continue
        is_higher = True # a가 b보다 항상 높은 순위인지 확인하는 플래그
        for i in range(k):
            # 현재 경기 순위
            current_rank = arr[i]

            rank_a = -1
            rank_b = -1

            for j in range(n):
                if current_rank[j] == a:
                    rank_a = j
                if current_rank[j] == b :
                    rank_b = j

            if rank_a > rank_b :
                is_higher = False
                break

        if is_higher:
            ans += 1
print(ans)
