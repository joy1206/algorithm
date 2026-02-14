n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def solution(r, c, k):
    count = 0
    for i in range(n):
        for j in range(n):
            if abs(r-i) + abs(c-j) <= k:
                if grid[i][j] == 1:
                    count +=1
    return count

max_gold = 0

for r in range(n):
    for c in range(n):
        for k in range(2 * n + 1):
            gold_cnt = solution(r, c, k)
            cost = k*k + (k+1) * (k+1)
            profit = gold_cnt * m - cost
            
            if profit >= 0:
                if gold_cnt > max_gold:
                    max_gold = gold_cnt

print(max_gold)


