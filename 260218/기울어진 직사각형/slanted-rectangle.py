n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def solution(r, c, w, h):
    total_sum = 0
    curr_r, curr_c = r, c

    for _ in range(w):
        curr_r -= 1
        curr_c += 1
        if not (0 <= curr_r < n and 0 <= curr_c < n):
            return 0
        total_sum += grid[curr_r][curr_c]
    
    for _ in range(h):
        curr_r -= 1
        curr_c -= 1
        if not (0 <= curr_r < n and 0 <= curr_c < n):
            return 0
        total_sum += grid[curr_r][curr_c]
    for _ in range(w):
        curr_r +=1
        curr_c -=1
        if not (0 <= curr_r < n and 0 <= curr_c < n):
            return 0
        total_sum += grid[curr_r][curr_c]
    for _ in range(h):
        curr_r +=1
        curr_c +=1
        if not (0 <= curr_r < n and 0 <= curr_c < n):
            return 0
        total_sum += grid[curr_r][curr_c]
    return total_sum

max_score = 0

for i in range(n):
    for j in range(n):
        for w in range(1, n):
            for h in range(1, n):
                score = solution(i, j, w, h)
                if score > max_score:
                    max_score = score

print(max_score)